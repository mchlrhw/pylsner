import cairo

from gi.repository import Gtk

import pylsner


class Metric:

    def __init__(self, unit):
        self.unit = unit
        self.store = MetricStore()

    def set_limits(self, minimum=None, maximum=None):
        if minimum or minimum == 0:
            self._min = minimum
        if maximum or maximum == 0:
            self._max = maximum
        assert(self._max >= self._min)
        self._range = self._max - self._min

    def _refresh(self, cnt, value):
        self.store._refresh(cnt)
        self.refresh(value)

    def refresh(self, value):
        ...

    @property
    def value(self):
        return (self._curr - self._min) / self._range


class MetricStore:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        self.refresh_cnt = 0
        self.refresh(self.refresh_cnt)

    def _refresh(self, cnt):
        if cnt != self.refresh_cnt:
            self.refresh_cnt = cnt
            self.refresh(cnt)

    def refresh(self, cnt):
        ...


class Indicator:

    def __init__(self, length, width, orientation, position, background):
        self.length = length
        self.width = width
        self.orientation = orientation
        self.position = pylsner.gui.Coord(*position)
        self.background = background

    @property
    def boundary(self):
        return pylsner.gui.BoundingBox()

    def redraw(self, ctx, value):
        ...


class Fill:

    def __init__(self):
        self.pattern = cairo.SolidPattern(1, 1, 1)

    def refresh(self, cnt, value):
        ...


def load_plugin(plugin_type, plugin_name):
    mod_str = 'pylsner.plugins.{}.{}'.format(plugin_type, plugin_name)
    _temp_mod = __import__(mod_str, globals(), locals(), ['Plugin'])
    return _temp_mod.Plugin
