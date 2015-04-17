import cairo

from gi.repository import Gtk
from gi.repository import Gdk

from pylsner import plugins


class Window(Gtk.Window):

    def __init__(self):
        super().__init__(skip_pager_hint=True, skip_taskbar_hint=True)
        self.set_title('Pylsner - {}'.format(self.name))

        screen = self.get_screen()
        self.origin = [screen.width() / 2, screen.height() / 2]

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

        super().__init__()
        self.init_widgets(widgets)

        self.connect('draw', self.redraw)
        self.show_all()

    def init_widgets(self, config):
        self.bounding_box = BoundingBox()

        self.widgets = []
        for widget_spec in config:
            widget = Widget(**widget_spec)
            self.widgets.append(widget)

        for widget in self.widgets:
            self.bounding_box.encompass(widget.bounding_box)
        for widget in self.widgets:
            widget.bounding_box.resize(*self.bounding_box.dimensions,
                                       absolute=True
                                      )
        

        self.resize(*self.bounding_box.dimensions)
        self.move(self.position[0] + self.origin[0] - (self.width / 2),
                  self.position[1] + self.origin[1] - (self.height / 2),
                 )

    @property
    def width(self):
        return self.bounding_box.width

    @property
    def height(self):
        return self.bounding_box.height

    def refresh(self, cnt=0):
        redraw_required = False
        for widget in self.widgets:
            refreshed = widget.refresh(cnt)
            if refreshed:
                redraw_required = True
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

    def resize(self, width=0, height=0, absolute=False):
        if absolute:
            self.width = width
            self.height = height
        else:
            self.width = self.btm_rght[0] - self.top_left[0]
            self.height = self.top_left[1] - self.btm_rght[1]

    @property
    def dimensions(self):
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
            if attr_name.startswith('__') or attr_name in ['width', 'height']:
                continue
            attr = getattr(self, attr_name)
            if hasattr(attr, 'bounding_box'):
                drawables.append(attr)

        self.bounding_box = BoundingBox()
        for drawable in drawables:
            self.bounding_box.encompass(drawable.bounding_box)
        for drawable in drawables:
            drawable.bounding_box.resize(*self.bounding_box.dimensions,
                                         absolute=True
                                        )

    @property
    def width(self):
        return self.bounding_box.width

    @property
    def height(self):
        return self.bounding_box.height

    @property
    def value(self):
        return self.metric.value

    @property
    def pattern(self):
        try:
            return self.fill.pattern
        except AttributeError:
            return cairo.SolidPattern(1, 1, 1)

    def refresh(self, cnt):
        if cnt % self.refresh_rate == 0:
            self.metric.refresh(cnt)
            for attr_name in dir(self):
                if attr_name == 'metric' or attr_name.startswith('__'):
                    continue
                attr = getattr(self, attr_name)
                if hasattr(attr, 'refresh'):
                    attr.refresh(cnt, self)
            return True
        else:
            return False

    def redraw(self, ctx):
        ctx.set_source(self.pattern)
        for attr_name in dir(self):
            if attr_name.startswith('__'):
                continue
            attr = getattr(self, attr_name)
            if hasattr(attr, 'redraw'):
                attr.redraw(ctx, self)
