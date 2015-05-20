import cairo

from gi.repository import Gtk

from .core import BoundingBox
from .core import Coord


class BasePlugin:

    ...


class StatefulPlugin(BasePlugin):

    def refresh(self, cnt, value):

        ...


class DrawablePlugin(BasePlugin):

    def redraw(self, ctx, value):

        ...


class Metric(StatefulPlugin):

    def __init__(self, **kwargs):

        self.unit = kwargs.pop('unit')
        self.raw_max = 0
        self.raw_min = 0
        self.store = MetricStore()
        self.store.register(self)
        self.setup(kwargs)

    @property
    def raw_range(self):

        if self.raw_max > self.raw_min:
            return self.raw_max - self.raw_min
        else:
            return self.raw_min - self.raw_max

    @property
    def value(self):

        return (self.raw_value - self.raw_min) / self.raw_range

    def setup(self, **kwargs):

        ...

    def source(self):

        ...

    def get_source(self, cnt):

        return self.store.get_source(self, cnt)


class MetricStore:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        self.registry = {}

    def register(self, plugin):
        if plugin.__name__ not in self.registry:
            new_entry = {'refresh_cnt': 0, 'source': plugin.source}
            self.registry[plugin.__name__] = new_entry

    def get_source(self, plugin, cnt):
        if cnt != self.registry[plugin.__name__]['refresh_cnt']:
            self.registry[plugin.__name__]['refresh_cnt'] = cnt
            return self.registry[plugin.__name__]['source']


class Indicator:

    def __init__(self, length, width, orientation, position, background):
        self.length = length
        self.width = width
        self.orientation = orientation
        self.position = Coord(*position)
        self.background = background

    @property
    def boundary(self):
        return BoundingBox()

    def redraw(self, ctx, value):
        ...


class Fill:

    def __init__(self):
        self.pattern = cairo.SolidPattern(1, 1, 1)

    def refresh(self, cnt, value):
        ...


def load_plugin(plugin_type, plugin_name):
    mod_str = 'pylsner.plugins.{}.{}'.format(plugin_type, plugin_name)
    module = __import__(mod_str, locals(), globals(), ['Plugin'])
    return module.Plugin
