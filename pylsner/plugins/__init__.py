import cairo


class Metric():

    def __init__(self, unit):
        self.unit = unit
        self.refresh_cnt = 0
        self.store = MetricStore()

    def set_limits(self, minimum=None, maximum=None):
        if minimum or minimum == 0:
            self._min = minimum
        if maximum or maximum == 0:
            self._max = maximum
        assert(self._max >= self._min)
        self._range = self._max - self._min

    def refresh(self, cnt):
        if cnt != self.refresh_cnt:
            self._refresh()
            self.refresh_cnt = cnt

    @property
    def value(self):
        return (self._curr - self._min) / self._range


class MetricStore:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Indicator(Gtk.DrawingArea):

    def __init__(self, length, width, orientation, position):
        self.length = length
        self.width = width
        self.orientation = orientation
        self.position = position

    def redraw(self, ctx):
        pass


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
