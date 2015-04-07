import cairo
import math

from pylsner.plugin import Indicator


class Plugin(Indicator):

    def __init__(self,
                 length=100,
                 width=10,
                 orientation=0,
                 position=[0, 0],
                 radius=100,
                 background=False,
                 **kwargs
                ):
        length = math.radians(360) * (length / 100)
        super().__init__(length, width, orientation, position)

        self.radius = radius
        self.background = background

        self._angle_start = math.radians(-90) + math.radians(self.orientation)
        self._angle_end = self._angle_start

    def redraw(self, ctx, metric_value):
        self._angle_end = self._angle_start + (metric_value * self.length)
        ctx.set_line_width(self.width)

        ctx.arc(
            self.position[0],
            self.position[1],
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

            if self._angle_end != self._angle_start:
                ctx.arc(
                    self.position[0],
                    self.position[1],
                    self.radius,
                    self._angle_end,
                    self._angle_start,
                )
            else:
                ctx.arc(
                    self.position[0],
                    self.position[1],
                    self.radius,
                    self._angle_start,
                    self._angle_start + self.length,
                )
            ctx.stroke()
