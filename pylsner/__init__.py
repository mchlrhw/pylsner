import os
import signal
import yaml

from gi.repository import Gtk
from gi.repository import GLib

from pylsner import gui


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
    config_path = 'config.yml'
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
        ind = gui.Indicator(**ind_spec)
        ind.position[0] = (window.width / 2) + ind.position[0]
        ind.position[1] = (window.height / 2) + (ind.position[1] * -1)
        indicators.append(ind)
    return indicators
