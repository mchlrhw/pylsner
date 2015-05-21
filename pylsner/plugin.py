import cairo

from gi.repository import Gtk

from .core import BoundingBox
from .core import Coord


class BasePlugin:

    def __init__(self, **kwargs):

        self.setup(**kwargs)

    def setup(self, **kwargs):

        ...


class StatefulPlugin(BasePlugin):

    @property
    def value(self):

        ...

    def refresh(self, cnt, value):

        ...


class DrawablePlugin(BasePlugin):

    def redraw(self, ctx, value):

        ...


class Metric(StatefulPlugin):

    def __init__(self, **kwargs):

        self.unit = kwargs.pop('unit', '')
        self.raw_max = 0
        self.raw_min = 0
        self.store = SourceStore()
        super().__init__(**kwargs)

    @property
    def raw_range(self):

        if self.raw_max > self.raw_min:
            return self.raw_max - self.raw_min
        else:
            return self.raw_min - self.raw_max

    @property
    def value(self):

        return (self.raw_value - self.raw_min) / self.raw_range

    def source(self, *args):

        ...

    def stored_source(self, cnt, *args):

        return self.store.source(self, cnt, *args)


class SourceStore:

    registry = {}

    def register(self, plugin, *args):

        key = type(plugin)
        if key not in self.registry:
            new_entry = {
                'refresh_cnt': 0,
                'stored_source': plugin.source(*args),
            }
            self.registry[key] = new_entry

    def source(self, plugin, cnt, *args):

        key = type(plugin)
        if key not in self.registry:
            self.register(plugin, *args)
        if cnt != self.registry[key]['refresh_cnt']:
            self.registry[key]['refresh_cnt'] = cnt
            self.registry[key]['stored_source'] = plugin.source(*args)
        return self.registry[key]['stored_source']


class Indicator(DrawablePlugin):

    def __init__(self, **kwargs):

        self.length = kwargs.pop('length', 100)
        self.width = kwargs.pop('width', 10)
        self.orientation = kwargs.pop('orientation', 0)
        self.position = Coord(*kwargs.pop('position', (0, 0)))
        self.background = kwargs.pop('background', True)
        super().__init__(**kwargs)

    @property
    def boundary(self):

        return BoundingBox()

    def redraw(self, ctx, value):

        ...


class Fill(StatefulPlugin):

    def setup(self):

        self.pattern = cairo.SolidPattern(1, 1, 1)

    @property
    def value(self):

        return self.pattern
