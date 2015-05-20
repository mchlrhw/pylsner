import cairo
import math

from pylsner.core import BoundingBox
from pylsner.core import Coord
from pylsner.plugin import Indicator


class Arc(Indicator):

    def __init__(self,
                 length=100,
                 width=10,
                 orientation=0,
                 position=[0, 0],
                 radius=100,
                 clockwise=True,
                 background=True,
                ):
        length = math.radians(360) * (length / 100)
        super().__init__(length, width, orientation, position, background)

        self.radius = radius
        self.clockwise = clockwise

        self._angle_start = (math.radians(-90)
                             + math.radians(self.orientation)
                            )
        if not self.clockwise:
            self._angle_start += self.length
        self._angle_end = self._angle_start

    @property
    def boundary(self):
        max_radius = self.radius + (self.width / 2)
        top_left = Coord(self.position.x - max_radius,
                         self.position.y + max_radius,
                        )
        btm_rght = Coord(self.position.x + max_radius,
                         self.position.y - max_radius,
                        )
        return BoundingBox(top_left, btm_rght)

    def redraw(self, ctx, value):
        if self.clockwise:
            self._angle_end = self._angle_start + (value * self.length)
            arc = ctx.arc
        else:
            self._angle_end = self._angle_start - (value * self.length)
            arc = ctx.arc_negative

        ctx.set_line_width(self.width)
        arc(
            self.position.x,
            self.position.y,
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
                bkgnd_start = self._angle_end
            else:
                bkgnd_start = self._angle_start
            if self.clockwise:
                bkgnd_end = self._angle_start + self.length
            else:
                bkgnd_end = self._angle_start - self.length
            arc(
                self.position.x,
                self.position.y,
                self.radius,
                bkgnd_start,
                bkgnd_end,
            )
            ctx.stroke()


Plugin = Arc
