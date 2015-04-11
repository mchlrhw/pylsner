import cairo

from numbers import Number


class Drawable:

    def redraw(self, ctx, window, parent):
        raise NotImplementedError


class Stateful:

    def refresh(self, parent, refresh_cnt):
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


class MetricStore:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        self.value = None
        self.refresh_cnt = None

    def get_value(self, refresh_cnt):
        if refresh_cnt != self.refresh_cnt:
            self.refresh()
            self.refresh_cnt = refresh_cnt
        return self.value

    def refresh(self):
        raise NotImplementedError


class Indicator(Drawable):

    def __init__(self, length, width, orientation, position):
        self.length = length
        self.width = width
        self.orientation = orientation
        self.position = position


class Fill:

    def __init__(self):
        self._pattern = cairo.SolidPattern(1, 1, 1)

    @property
    def pattern(self):
        return self._pattern


def load_plugin(plugin_type, plugin_name):
    mod_str = 'pylsner.plugins.{}.{}'.format(plugin_type, plugin_name)
    _temp_mod = __import__(mod_str, globals(), locals(), ['Plugin'])
    return _temp_mod.Plugin
