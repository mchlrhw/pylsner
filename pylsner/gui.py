import cairo

from gi.repository import Gtk
from gi.repository import Gdk

from pylsner import plugin


class Window(Gtk.Window):

    def __init__(self):
        super(Window, self).__init__(skip_pager_hint=True,
                                     skip_taskbar_hint=True,
                                    )
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

        self.indicators = []

        self.show_all()

    def refresh(self, force=False):
        self.refresh_cnt += 1
        refresh_list = []
        if self.refresh_cnt >= 10000:
            self.refresh_cnt = 0
        for ind in self.indicators:
            if (self.refresh_cnt % ind.metric.refresh_rate == 0) or force:
                refresh_list.append(ind)
        for ind in refresh_list:
            ind.refresh()
        if refresh_list:
            self.queue_draw()
        return True

    def redraw(self, widget, ctx):
        ctx.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
        for ind in self.indicators:
            ind.redraw(ctx)


class Indicator:

    def __init__(self,
                 name='default',
                 metric={'plugin': 'time'},
                 widget={'plugin': 'arc'},
                 position=[0, 0],
                 color={'plugin': 'rgba_255'},
                ):
        self.name = name
        MetricPlugin = plugin.load_plugin('metrics', metric['plugin'])
        self.metric = MetricPlugin(**metric)
        WidgetPlugin = plugin.load_plugin('widgets', widget['plugin'])
        self.widget = WidgetPlugin(**widget)
        self.position = position
        ColorPlugin = plugin.load_plugin('colors', color['plugin'])
        self.color = ColorPlugin(**color)

    def refresh(self):
        self.metric.refresh()
        self.color.refresh(self.metric.value)

    def redraw(self, ctx):
        r, g, b, a = self.color.value
        ctx.set_source_rgba(r, g, b, a)
        self.widget.redraw(ctx, self.position, self.metric.value)
