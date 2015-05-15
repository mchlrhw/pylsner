import cairo

from collections import namedtuple
from gi.repository import Gtk
from gi.repository import Gdk

from pylsner import plugins


Coord = namedtuple('Coord', ['x', 'y'])


class Window(Gtk.Window):

    def __init__(self, name='default', position=[0, 0]):
        super().__init__(skip_pager_hint=True, skip_taskbar_hint=True)

        self.name = name
        self.set_title('Pylsner - ' + self.name)
        self.position = Coord(*position)
        self.width, self.height = self.get_size()
        self.origin = Coord(self.width / 2, self.height / 2)

        screen = self.get_screen()
        o_x = screen.width() / 2
        o_y = screen.height() / 2
        self._screen_origin = Coord(o_x, o_y)

        rgba = screen.get_rgba_visual()
        self.set_visual(rgba)
        self.override_background_color(Gtk.StateFlags.NORMAL,
                                       Gdk.RGBA(0, 0, 0, 0),
                                      )

        self.set_wmclass('pylsner', 'pylsner')
        self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.stick()
        self.set_keep_below(True)

        drawing_area = Gtk.DrawingArea()
        self.add(drawing_area)

        self.connect('destroy', lambda q: Gtk.main_quit())
        self.connect('draw', self.redraw)

    def move(self, x, y):
        x += self._screen_origin.x - (self.width / 2)
        y = -y
        y += self._screen_origin.y - (self.height / 2)
        super().move(x, y)

    def resize(self, width, height):
        super().resize(width, height)
        self.width = width
        self.height = height
        self.origin = Coord(self.width / 2, self.height / 2)
        self.move(*self.position)

    def redraw(self, _, ctx):
        ...

    def refresh(self, cnt):
        ...


class BoundingBox:

    def __init__(self, top_left=[-1, 1], btm_rght=[1, -1]):
        self.top_left = Coord(*top_left)
        self.btm_rght = Coord(*btm_rght)

    @property
    def width(self):
        return self.btm_rght.x - self.top_left.x

    @property
    def height(self):
        return self.top_left.y - self.btm_rght.y

    @property
    def dimensions(self):
        return self.width, self.height

    def encompass(self, other):
        if self.top_left.x > other.top_left.x:
            top_left_x = other.top_left.x
        else:
            top_left_x = self.top_left.x
        if self.top_left.y < other.top_left.y:
            top_left_y = other.top_left.y
        else:
            top_left_y = self.top_left.y
        if self.btm_rght.x < other.btm_rght.x:
            btm_rght_x = other.btm_rght.x
        else:
            btm_rght_x = self.btm_rght.x
        if self.btm_rght.y > other.btm_rght.y:
            btm_rght_y = other.btm_rght.y
        else:
            btm_rght_y = self.btm_rght.y

        self.top_left = Coord(top_left_x, top_left_y)
        self.btm_rght = Coord(btm_rght_x, btm_rght_y)

    def __repr__(self):
        rep = 'BoundingBox({} x {} @ {})'
        return rep.format(self.width, self.height, self.top_left)


class Widget(Window):

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', 'default')
        self.refresh_rate = kwargs.pop('refresh_rate', 500)
        self.position = Coord(*kwargs.pop('position', [0, 0]))
        super().__init__(self.name, self.position)

        self.plugins = []
        self.drawable_plugins = []
        self.stateful_plugins = []
        for plugin_type, plugin_spec in kwargs.items():
            plugin_dir = plugin_type + 's'
            Plugin = plugins.load_plugin(plugin_dir, plugin_spec.pop('plugin'))
            plugin = Plugin(**plugin_spec)
            self.plugins.append(plugin)

            if hasattr(plugin, 'redraw'):
                self.drawable_plugins.append(plugin)
            if plugin_type in ['metric', 'fill']:
                setattr(self, plugin_type, plugin)
                if plugin_type == 'fill':
                    self.stateful_plugins.append(plugin)
            elif hasattr(plugin, 'refresh'):
                self.stateful_plugins.append(plugin)

        boundary = BoundingBox()
        for plugin in self.drawable_plugins:
            if hasattr(plugin, 'boundary'):
                boundary.encompass(plugin.boundary)
        self.resize(*boundary.dimensions)

        for plugin in self.plugins:
            if hasattr(plugin, 'position'):
                x = plugin.position.x + self.origin.x
                y = plugin.position.y + self.origin.y
                plugin.position = Coord(x, y)

        self.show_all()

    @property
    def value(self):
        try:
            return self.metric.value
        except AttributeError:
            return 0

    @property
    def pattern(self):
        try:
            return self.fill.pattern
        except AttributeError:
            return cairo.SolidPattern(1, 1, 1)

    def refresh(self, cnt=0):
        if cnt % self.refresh_rate == 0:
            try:
                self.metric._refresh(cnt, self.value)
            except AttributeError:
                self.metric.refresh(cnt, self.value)
            for plugin in self.stateful_plugins:
                try:
                    plugin._refresh(cnt, self.value)
                except AttributeError:
                    plugin.refresh(cnt, self.value)
            self.queue_draw()

    def redraw(self, _, ctx):
        ctx.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
        ctx.set_source(self.pattern)
        for plugin in self.drawable_plugins:
            plugin.redraw(ctx, self.value)
