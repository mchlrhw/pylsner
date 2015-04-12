import os
import signal
import yaml

from gi.repository import Gtk
from gi.repository import GLib

from pylsner import gui


class Loader(yaml.Loader):

    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)


Loader.add_constructor('!include', Loader.include)


def main():
    main_win = gui.Window()
    load_config(main_win)

    GLib.timeout_add(1, main_win.refresh)
    GLib.timeout_add(1000, load_config, main_win)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()


def load_config(window):
    reload_required = check_config()
    if reload_required:
        reload_config(window)
    return True


def check_config():
    if 'mtime' not in check_config.__dict__:
        check_config.mtime = 0
    config_dir_path = 'etc/pylsner'
    for filename in os.listdir(config_dir_path):
        file_path = os.path.join(config_dir_path, filename)
        mtime = os.path.getmtime(file_path)
        if mtime > check_config.mtime:
            check_config.mtime = mtime
            return True
    return False


def reload_config(window):
    config_path = 'etc/pylsner/config.yml'
    with open(config_path) as config_file:
        config = yaml.load(config_file, Loader)
    window.init_widgets(config)
    window.refresh(True)
