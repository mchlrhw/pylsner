import cairo

from gi.repository import Gtk
from gi.repository import Gdk

from pylsner import plugin


class Window(Gtk.Window):

    def __init__(self):
        super().__init__(skip_pager_hint=True, skip_taskbar_hint=True)
        self.set_title('Pylsner')

        screen = self.get_screen()
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.set_size_request(self.width, self.height)
        self.set_position(Gtk.WindowPosition.CENTER)
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
        drawing_area.connect('draw', self.redraw)
        self.refresh_cnt = 0
        self.add(drawing_area)

        self.connect('destroy', lambda q: Gtk.main_quit())

        self.widgets = []

        self.show_all()

    def init_widgets(self, config):
        self.widgets = []
        for widget_spec in config['widgets']:
            widget = Widget(**widget_spec)
            self.widgets.append(widget)

    def refresh(self, force=False):
        self.refresh_cnt += 1
        if self.refresh_cnt >= 60000:
            self.refresh_cnt = 0
        redraw_required = False
        for widget in self.widgets:
            if (self.refresh_cnt % widget.refresh_rate == 0) or force:
                widget.refresh(self.refresh_cnt)
                redraw_required = True
        if redraw_required:
            self.queue_draw()
        return True

    def redraw(self, _, ctx):
        ctx.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
        for widget in self.widgets:
            widget.redraw(ctx, self)


class Widget:

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name')
        for plugin_type, plugin_spec in kwargs.items():
            plugin_dir = plugin_type + 's'
            Plugin = plugin.load_plugin(plugin_dir, plugin_spec.pop('plugin'))
            setattr(self, plugin_type, Plugin(**plugin_spec))
        assert(hasattr(self, 'metric'))

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

    def refresh(self, refresh_cnt):
        self.metric.refresh(self, refresh_cnt)
        for attr_name in dir(self):
            if attr_name == 'metric' or attr_name.startswith('__'):
                continue
            attr = getattr(self, attr_name)
            if isinstance(attr, plugin.Stateful):
                attr.refresh(self, refresh_cnt)

    def redraw(self, ctx, window):
        ctx.set_source(self.pattern)
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if isinstance(attr, plugin.Drawable):
                attr.redraw(ctx, window, self)
