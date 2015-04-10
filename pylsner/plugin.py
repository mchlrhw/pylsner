from numbers import Number


class Drawable:

    def redraw(self, ctx, window, parent):
        raise NotImplementedError


class Stateful:

    def refresh(self, parent):
        raise NotImplementedError


class Metric(Stateful):

    def __init__(self, unit, refresh_rate):
        self.unit = unit
        self.refresh_rate = refresh_rate

    def set_limits(self, minimum=None, maximum=None):
        if isinstance(minimum, Number):
            self._min = minimum
        if isinstance(maximum, Number):
            self._max = maximum
        assert(self._max >= self._min)
        self._range = self._max - self._min

    @property
    def value(self):
        return (self._curr - self._min) / self._range


class Indicator(Drawable):

    def __init__(self, length, width, orientation, position):
        self.length = length
        self.width = width
        self.orientation = orientation
        self.position = position


class Fill(Stateful):
    pass


def load_plugin(plugin_type, plugin_name):
    mod_str = 'pylsner.plugins.{}.{}'.format(plugin_type, plugin_name)
    _temp_mod = __import__(mod_str, globals(), locals(), ['Plugin'])
    return _temp_mod.Plugin
