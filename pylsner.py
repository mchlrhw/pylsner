#!/usr/bin/python3


import os
import signal
import yaml

from gi.repository import Gtk
from gi.repository import GLib

from lib import gui
from lib.plugins.metrics.time import Time
from lib.plugins.widgets.arc import Arc
from lib.plugins.colors.rgba_255 import RGBA_255


def main():
    main_win = gui.Window()
    reload_config(main_win)

    GLib.timeout_add(1, main_win.refresh)
    GLib.timeout_add(1000, reload_config, main_win)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()


def reload_config(window):
    if 'mtime' not in reload_config.__dict__:
        reload_config.mtime = 0
    config_path = 'etc/pylsner/config.yml'
    config_mtime = os.path.getmtime(config_path)
    if config_mtime > reload_config.mtime:
        reload_config.mtime = config_mtime
        with open(config_path) as config_file:
            config = yaml.load(config_file)
        window.indicators = init_indicators(config, window)
        window.refresh(True)
    return True


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
        position[1] = (window.height / 2) + (position[1] * -1)
        if ind_spec['color']['plugin'] == 'rgba_255':
            value = ind_spec['color']['value']
            color = RGBA_255(value)
        ind = gui.Indicator(name, metric, widget, position, color)
        indicators.append(ind)
    return indicators


if __name__ == '__main__':
    main()
