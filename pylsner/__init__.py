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


class Pylsner:

    def __init__(self):
        self.desklets = []
        self.tick_cnt = 0
        self.config_mtime = 0

    def main(self):
        self.load_config()

        GLib.timeout_add(1, self.tick)
        GLib.timeout_add(1000, self.load_config)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        Gtk.main()

    def tick(self):
        self.tick_cnt += 1
        if self.tick_cnt >= 60000:
            self.tick_cnt = 0
        for desklet in self.desklets:
            desklet.refresh(self.tick_cnt)
        return True

    def load_config(self):
        reload_required = self.check_config()
        if reload_required:
            self.reload_config()
        return True

    def check_config(self):
        config_dir_path = 'etc/pylsner'
        for filename in os.listdir(config_dir_path):
            file_path = os.path.join(config_dir_path, filename)
            mtime = os.path.getmtime(file_path)
            if mtime > self.config_mtime:
                self.config_mtime = mtime
                return True
        return False

    def reload_config(self):
        config_path = 'etc/pylsner/config.yml'
        with open(config_path) as config_file:
            config = yaml.load(config_file, Loader)
        self.desklets = self.init_desklets(config)
        for desklet in self.desklets:
            desklet.refresh()

    def init_desklets(self, config):
        desklets = []
        for desklet_spec in config['desklets']:
            desklet = gui.Desklet(**desklet_spec)
            desklets.append(desklet)
        return desklets
