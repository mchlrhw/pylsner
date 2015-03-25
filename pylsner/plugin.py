class Metric:

    def __init__(self, plugin=None, unit=None, refresh_rate=None):
        self.plugin = plugin
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


class Widget:

    def __init__(self, plugin=None, length=None, width=None, orientation=None):
        self.plugin = plugin
        self.length = length
        self.width = width
        self.orientation = orientation

    def redraw(self, ctx):
        pass


class Color:

    def __init__(self, plugin=None, value=None):
        self.plugin = plugin
        self.value = value

    def refresh(self, metric_value):
        pass


def load_plugin(plugin_type, plugin_name):
    mod_str = 'pylsner.plugins.{}.{}'.format(plugin_type, plugin_name)
    _temp_mod = __import__(mod_str, globals(), locals(), ['Plugin'])
    return _temp_mod.Plugin
