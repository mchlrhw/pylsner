#!/usr/bin/python3


import cairo
import math
import signal

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
        scr_w = screen.get_width()
        scr_h = screen.get_height()
        self.set_size_request(scr_w, scr_h)
        self.set_position(Gtk.WindowPosition.CENTER)
        rgba = screen.get_rgba_visual()
        self.set_visual(rgba)
        self.override_background_color(Gtk.StateFlags.NORMAL,
                                       Gdk.RGBA(0, 0, 0, 0),
                                      )

        self.set_wmclass('pylsnerwidget', 'pylsnerwidget')
        self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.stick()
        self.set_keep_below(True)

        drawing_area = Gtk.DrawingArea()
        drawing_area.connect('draw', self.redraw)
        self.add(drawing_area)

        self.connect('destroy', lambda q: Gtk.main_quit())

        self.indicators = []

        self.show_all()

    def update(self):
        for ind in self.indicators:
            ind.update()
            self.queue_draw()
        return True

    def redraw(self, widget, ctx):
        for ind in self.indicators:
            ctx.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
            red, grn, blu, alf = ind.color
            ctx.set_source_rgba(red, grn, blu, alf)
            x, y = ind.pos
            ctx.arc(x, y, ind.size, ind.start, ind.end)
            ctx.set_line_width(ind.thick)
            ctx.stroke()


class Indicator:

    def __init__(self, parent):
        self.color = (0, 0, 0, 0.5)
        parent_w, parent_h = parent.get_size()
        self.pos = (parent_w / 2, parent_h / 2)
        self.size = 100
        self.thick = 10
        
        self.val_min = 0
        self.val_max = 60
        self.val_range = self.val_max - self.val_min
        self.val_curr = self.val_min
        
        self.len_min = 0
        self.len_max = math.radians(360)
        self.len_range = self.len_max - self.len_min
        self.len_curr = self.len_min

        self.start = math.radians(-90)
        self.end = self.start

    def set_len_limits(self, len_min, len_max):
        self.len_min = len_min
        self.len_max = len_max
        self.len_range = len_max - len_min

    def set_val_limits(self, val_min, val_max):
        self.val_min = val_min
        self.val_max = val_max
        self.val_range = val_max - val_min

    def update(self):
        pass


class Clock(Indicator):

    def __init__(self, parent, unit):
        super(Clock, self).__init__(parent)
        self.unit = unit

    def update(self):
        now = datetime.now()
        if self.unit == 'seconds':
            self.set_val_limits(0, 60)
            self.val_curr = now.second + (now.microsecond / 1000000)
        elif self.unit == 'minutes':
            self.set_val_limits(0, 60)
            self.val_curr = (now.minute + 
                             (now.second / 60) +
                             (now.microsecond / 60000000)
                            )
        elif self.unit == 'hours':
            self.set_val_limits(0, 12)
            self.val_curr = ((now.hour % 12) + 
                             (now.minute / 60) +
                             (now.second / 3600)
                            )
        else:
            raise Exception('Unrecognised unit')
        val_percent = self.val_curr / self.val_range
        self.end = self.start + (val_percent * self.len_range)
        


def main():
    pyl_win = Window()

    secs = Clock(pyl_win, 'seconds')
    pyl_win.indicators.append(secs)

    mins = Clock(pyl_win, 'minutes')
    mins.size = 120
    pyl_win.indicators.append(mins)

    hrs = Clock(pyl_win, 'hours')
    hrs.size = 140
    pyl_win.indicators.append(hrs)

    GLib.timeout_add(10, pyl_win.update)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()


if __name__ == '__main__':
    main()
