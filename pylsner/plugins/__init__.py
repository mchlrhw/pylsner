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

    def refresh(self, cnt, parent=None):
        self.store.refresh(cnt)
        self._refresh()

    def _refresh(self):
        pass

    @property
    def value(self):
        return (self._curr - self._min) / self._range


class MetricStore:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        self.refresh_cnt = 0
        self._refresh()

    def refresh(self, cnt, parent=None):
        if cnt != self.refresh_cnt:
            self.refresh_cnt = cnt
            self._refresh()

    def _refresh(self):
        pass    


class Indicator(Gtk.DrawingArea):

    def __init__(self, length, width, orientation, position):
        self.length = length
        self.width = width
        self.orientation = orientation
        self.position = position
        self.bounding_box = pylsner.gui.BoundingBox()

    def redraw(self, ctx):
        pass


class Fill:

    def __init__(self):
        self._pattern = cairo.SolidPattern(1, 1, 1)

    @property
    def pattern(self):
        return self._pattern

    def refresh(self, cnt=None, parent=None):
        self._refresh(parent)

    def _refresh(self, parent=None):
        pass


def load_plugin(plugin_type, plugin_name):
    mod_str = 'pylsner.plugins.{}.{}'.format(plugin_type, plugin_name)
    _temp_mod = __import__(mod_str, globals(), locals(), ['Plugin'])
    return _temp_mod.Plugin
