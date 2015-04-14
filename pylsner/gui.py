import cairo

from gi.repository import Gtk
from gi.repository import Gdk

from pylsner import plugins


class Window(Gtk.Window):

    def __init__(self, name):
        super().__init__(skip_pager_hint=True, skip_taskbar_hint=True)
        self.set_title('Pylsner - {}'.format(name))

        screen = self.get_screen()
        origin = [screen.width() / 2, screen.height() / 2]

        rgba = screen.get_rgba_visual()
        self.set_visual(rgba)
        self.override_background_color(Gtk.StateFlags.NORMAL,
                                       Gdk.RGBA(0, 0, 0, 0),
                                      )

        self.set_wmclass('pylsner', 'pylsner')
        self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.stick()
        self.set_keep_below(True)

        self.connect('destroy', lambda q: Gtk.main_quit())


class Desklet(Window):

    def __init__(self, name='default', position=[0, 0], widgets=[]):
        self.name = name
        self.position = position
        self.bounding_box = BoundingBox()

        self.init_widgets(widgets)

        super().__init__(self.name)
        self.connect('draw', self.redraw)

        self.show_all()

    def init_widgets(self, config):
        self.bounding_box = BoundingBox()

        self.widgets = []
        for widget_spec in config:
            widget = Widget(**widget_spec)
            self.widgets.append(widget)

        for widget in self.widgets:
            if hasattr(widget, 'indicator'):
                if isinstance(widget.indicator, Gtk.DrawingArea):
                    self.add(widget.indicator)
                self.bounding_box.encompass(widget.bounding_box)

        self.resize(self.bounding_box.get_dimensions())

    def refresh(self, cnt=0):
        redraw_required = False
        for widget in self.widgets:
            redraw_required = widget.refresh(cnt)
        if redraw_required:
            self.queue_draw()

    def redraw(self, gtk_widget, ctx):
        ctx.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
        for widget in self.widgets:
            widget.redraw(ctx)


class BoundingBox:

    def __init__(self, top_left=[0, 0], btm_rght=[0, 0]):
        self.top_left = top_left
        self.btm_rght = btm_rght

        self.resize()

    def resize(self, absolute=False, width=0, height=0):
        if absolute:
            self.width = width
            self.height = height
        else:
            self.width = btm_rght[0] - top_left[0]
            self.height = top_left[1] - btm_rght[1]

    def get_dimensions(self):
        return self.width, self.height

    def encompass(self, bounding_box=None, top_left=[0, 0], btm_rght=[0, 0]):
        if not bounding_box:
            bounding_box = BoundingBox(top_left, btm_rght)
        if self.top_left[0] > bounding_box.top_left[0]:
            self.top_left[0] = bounding_box.top_left[0]
        if self.top_left[1] < bounding_box.top_left[1]:
            self.top_left[1] = bounding_box.top_left[1]
        if self.btm_rght[0] < bounding_box.btm_rght[0]:
            self.btm_rght[0] = bounding_box.btm_rght[0]
        if self.btm_rght[1] > bounding_box.btm_rght[1]:
            self.btm_rght[1] = bounding_box.btm_rght[1]

        self.resize()


class Widget:

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', 'default')
        self.refresh_rate = kwargs.pop('refresh_rate', 10)
        for plugin_type, plugin_spec in kwargs.items():
            plugin_dir = plugin_type + 's'
            Plugin = plugins.load_plugin(plugin_dir, plugin_spec.pop('plugin'))
            setattr(self, plugin_type, Plugin(**plugin_spec))
        try:
            assert(hasattr(self, 'metric'))
        except AssertionError:
            print('Error: Widget must have a metric plugin as a minimum')
        drawables = []
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if isinstance(attr, plugins.Drawable):
                drawables.append(attr)
        self.bounding_box = BoundingBox()
        for drawable in drawables:
            self.bounding_box.encompass(drawable.bounding_box)

    @property
    def value(self):
        return self.metric.value

    @property
    def refresh_rate(self):
        return self.metric.refresh_rate

    @property
    def pattern(self):
        try:
            return self.fill.pattern
        except AttributeError:
            return cairo.SolidPattern(1, 1, 1)

    def refresh(self, cnt):
        if cnt % self.refresh_rate == 0:
            self.metric.refresh(self, cnt)
            for attr_name in dir(self):
                if attr_name == 'metric' or attr_name.startswith('__'):
                    continue
                attr = getattr(self, attr_name)
                if isinstance(attr, plugins.Stateful):
                    attr.refresh(self, refresh_cnt)
            return True
        else:
            return False

    def redraw(self, ctx, window):
        ctx.set_source(self.pattern)
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if isinstance(attr, plugins.Drawable):
                attr.redraw(ctx, window, self)
