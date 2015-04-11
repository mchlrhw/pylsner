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
                 clockwise=True,
                 background=False,
                ):
        length = math.radians(360) * (length / 100)
        super().__init__(length, width, orientation, position)

        self.radius = radius
        self.clockwise = clockwise
        self.background = background

        self._angle_start = (math.radians(-90)
                             + math.radians(self.orientation)
                            )
        if not self.clockwise:
            self._angle_start += self.length
        self._angle_end = self._angle_start

    def redraw(self, ctx, window, parent):
        value = parent.value
        origin = [window.width / 2, window.height / 2]

        if self.clockwise:
            self._angle_end = self._angle_start + (value * self.length)
            define_arc = ctx.arc
        else:
            self._angle_end = self._angle_start - (value * self.length)
            define_arc = ctx.arc_negative

        ctx.set_line_width(self.width)
        define_arc(
            origin[0] + self.position[0],
            origin[1] - self.position[1],
            self.radius,
            self._angle_start,
            self._angle_end,
        )
        ctx.stroke()

        if self.background:
            source = ctx.get_source()

            if isinstance(source, cairo.SolidPattern):
                r, g, b, a = ctx.get_source().get_rgba()
                a = a / 3
            else:
                r, g, b, a = 0, 0, 0, 0.333

            ctx.set_source_rgba(r, g, b, a)

            if self._angle_end != self._angle_start:
                if self.clockwise:
                    bkgnd_end = self._angle_start + self.length
                else:
                    bkgnd_end = self._angle_start - self.length
                define_arc(
                    origin[0] + self.position[0],
                    origin[1] - self.position[1],
                    self.radius,
                    self._angle_end,
                    bkgnd_end,
                )
            else:
                define_arc(
                    origin[0] + self.position[0],
                    origin[1] - self.position[1],
                    self.radius,
                    self._angle_start,
                    bkgnd_end,
                )
            ctx.stroke()
