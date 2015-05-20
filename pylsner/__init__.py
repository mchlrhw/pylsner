import os

from . import core
from . import color
from . import plugin


user_plugin_root = os.path.expanduser('~/.pylsner')
if os.path.isdir(os.path.join(user_plugin_root, 'plugins')):
    __path__.append(user_plugin_root)
