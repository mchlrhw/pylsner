import cairo
import math

from pylsner.plugin import Widget


class Plugin(Widget):

    def __init__(self,
                 plugin='arc',
                 length=100,
                 width=10,
                 orientation=0,
                 radius=100,
                 background=False,
                ):
        length = math.radians(360) * (length / 100)
        super().__init__(plugin, length, width, orientation)
        self.radius = radius
        self.background = background

        self._angle_start = math.radians(-90) + math.radians(self.orientation)
        self._angle_end = self._angle_start

    def redraw(self, ctx, position, value):
        self._angle_end = self._angle_start + (value * self.length)
        ctx.set_line_width(self.width)
        ctx.arc(
            position[0],
            position[1],
            self.radius,
            self._angle_start,
            self._angle_end,
        )
        ctx.stroke()
        if self.background:
            source = ctx.get_source()
            if isinstance(source, cairo.SolidPattern):
                r, g, b, a = ctx.get_source().get_rgba()
                a = a / 2
            else:
                r, g, b, a = 0, 0, 0, 0.5
            ctx.set_source_rgba(r, g, b, a)
            ctx.arc(
                position[0],
                position[1],
                self.radius,
                self._angle_end,
                self._angle_start,
            )
            ctx.stroke()
