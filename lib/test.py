#!/usr/bin/python3


import cairo
import math
import os
import signal
import yaml

from datetime import datetime
from gi.repository import Gdk
from gi.repository import Gtk
from gi.repository import GLib


class Window(Gtk.Window):

    def __init__(self):
        super(Window, self).__init__(skip_pager_hint=True,
                                     skip_taskbar_hint=True,
                                    )
        self.set_title('Pylsner')

        screen = self.get_screen()
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.set_size_request(self.width, self.height)
        self.set_position(Gtk.WindowPosition.CENTER)
        rgba = screen.get_rgba_visual()
        self.set_visual(rgba)
        self.override_background_color(Gtk.StateFlags.NORMAL,
                                       Gdk.RGBA(0, 0, 0, 0),
                                      )

        self.set_wmclass('pylsner', 'pylsner')
        self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.stick()
        self.set_keep_below(True)

        drawing_area = Gtk.DrawingArea()
        drawing_area.connect('draw', self.redraw)
        self.refresh_cnt = 0
        self.add(drawing_area)

        self.connect('destroy', lambda q: Gtk.main_quit())

        self.indicators = []

        self.show_all()

    def refresh(self, force=False):
        self.refresh_cnt += 1
        refresh_list = []
        if self.refresh_cnt >= 10000:
            self.refresh_cnt = 0
        for ind in self.indicators:
            if (self.refresh_cnt % ind.metric.refresh_rate == 0) or force:
                refresh_list.append(ind)
        for ind in refresh_list:
            ind.refresh()
        if refresh_list:
            self.queue_draw()
        return True

    def redraw(self, widget, ctx):
        ctx.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
        for ind in self.indicators:
            ind.redraw(ctx)


def init_indicators(config, window):
    indicators = []
    for ind_spec in config['indicators']:
        name = ind_spec['name']
        if ind_spec['metric']['plugin'] == 'time':
            unit = ind_spec['metric']['unit']
            refresh_rate = ind_spec['metric']['refresh_rate']
            metric = Time(unit, refresh_rate)
        if ind_spec['widget']['plugin'] == 'arc':
            length = ind_spec['widget']['length']
            width = ind_spec['widget']['width']
            orientation = ind_spec['widget']['orientation']
            radius = ind_spec['widget']['radius']
            widget = Arc(length, width, orientation, radius=radius)
        position = ind_spec['position']
        position[0] = (window.width / 2) + position[0]
        position[1] = (window.height / 2) + position[1]
        if ind_spec['color']['plugin'] == 'rgba_255':
            value = ind_spec['color']['value']
            color = RGBA_255(value)
        ind = Indicator(name, metric, widget, position, color)
        indicators.append(ind)
    return indicators


class Metric:

    def __init__(self, unit=None, refresh_rate=None):
        self.plugin = None
        self.unit = unit
        self.refresh_rate = refresh_rate

        self._val_min = None
        self._val_max = None
        self._val_range = None
        self._val_curr = None
        self._val_frac = None

    @property
    def value(self):
        return self._val_frac

    @property
    def value_raw(self):
        return self._val_curr

    def refresh(self):
        pass


class Time(Metric):

    def __init__(self, unit='seconds', refresh_rate=1):
        super().__init__(unit, refresh_rate)
        self.plugin = 'time'

        self._val_min = 0
        if self.unit in ['seconds', 'seconds_tick']:
            self._val_max = 60
        elif self.unit == 'minutes':
            self._val_max = 60
        elif self.unit == 'hours':
            self._val_max = 12
        elif self.unit == 'hours_24':
            self._val_max = 24

        self._val_range = self._val_max - self._val_min
        self._val_curr = self._val_min
        self._val_frac = (self._val_curr - self._val_min) / self._val_range

    def refresh(self):
        now = datetime.now()
        if self.unit == 'seconds':
            self._val_curr = now.second + (now.microsecond / 1000000)
        elif self.unit == 'seconds_tick':
            self._val_curr = now.second
        elif self.unit == 'minutes':
            self._val_curr = (
                now.minute
                + now.second / 60
                + (now.microsecond / 60000000)
            )
        elif self.unit == 'hours':
            self._val_curr = (
                (now.hour % 12)
                + now.minute / 60
                + now.second / 3600
            )
        elif self.unit == 'hours_24':
            self._val_curr = (
                now.hour
                + now.minute / 60
                + now.second / 3600
            )
        self._val_frac = (self._val_curr - self._val_min) / self._val_range


class Widget:

    def __init__(self, length=None, width=None, orientation=None, **kwargs):
        self.plugin = None
        self.length = length
        self.width = width
        self.orientation = orientation

    def redraw(self, ctx):
        pass


class Arc(Widget):

    def __init__(self, length=100, width=10, orientation=0, **kwargs):
        length = math.radians(360) * (length / 100)
        super().__init__(length, width, orientation)
        self.plugin = 'arc'
        self.radius = kwargs['radius']
        self._angle_start = math.radians(-90) + math.radians(self.orientation)
        self._angle_end = self._angle_start
        
    def redraw(self, ctx, position, value):
        self._angle_end = self._angle_start + (value * self.length)
        ctx.set_line_width(self.width)
        ctx.arc(
            position[0],
            position[1],
            self.radius,
            self._angle_start,
            self._angle_end,
        )
        ctx.stroke()


class Color:

    def __init__(self, value):
        self.plugin = None
        self.value = value

    def refresh(self, metric_value):
        pass


class RGBA_255(Color):

    def __init__(self, value=(0, 0, 0, 255)):
        value = (
            value[0] / 255,
            value[1] / 255,
            value[2] / 255,
            value[3] / 255,
        )
        super().__init__(value)
        self.plugin = 'rgba_255'


class Indicator:

    def __init__(self, name, metric, widget, position, color):
        self.name = name
        self.metric = metric
        self.widget = widget
        self.position = position
        self.color = color

    def refresh(self):
        self.metric.refresh()
        self.color.refresh(self.metric.value)

    def redraw(self, ctx):
        r, g, b, a = self.color.value
        ctx.set_source_rgba(r, g, b, a)
        self.widget.redraw(ctx, self.position, self.metric.value)


def reload_config(window):
    if 'mtime' not in reload_config.__dict__:
        reload_config.mtime = 0
    config_path = '/home/mike/Code/python/pylsner/etc/pylsner/config.yml'
    config_mtime = os.path.getmtime(config_path)
    if config_mtime > reload_config.mtime:
        reload_config.mtime = config_mtime
        with open(config_path) as config_file:
            config = yaml.load(config_file)
        window.indicators = init_indicators(config, window)
        window.refresh(True)
    return True


def main():
    main_win = Window()
    reload_config(main_win)

    GLib.timeout_add(1, main_win.refresh)
    GLib.timeout_add(1000, reload_config, main_win)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()


if __name__ == '__main__':
    main()
