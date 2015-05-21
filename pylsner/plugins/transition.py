import cairo

from bisect import bisect_right

from pylsner.color import Color
from pylsner.plugin import Fill


class Transition(Fill):

    def setup(self, colors={0: [1, 1, 1]}, mode='rgb'):
        for stop, color in colors.items():
            color = Color(color, mode=mode)
            colors[stop] = color

        if not colors:
            self._pattern = cairo.SolidPattern(1, 1, 1)
        elif len(colors) == 1:
            _, color = colors.popitem()
            self.pattern = cairo.SolidPattern(*color.rgba)
        else:
            stop_keys = sorted(colors.keys())
            self.colors = {}
            for key, value in colors.items():
                key = key / stop_keys[-1]
                self.colors[key] = value
            self.stop_keys = sorted(self.colors.keys())

    def refresh(self, cnt, value):
        if hasattr(self, 'colors'):
            self._trans(value)

    def _trans(self, value):
        stop_2 = bisect_right(self.stop_keys, value)
        stop_1 = stop_2 - 1
        stop_1 = stop_2 if stop_1 < 0 else stop_1

        stop_key_1 = self.stop_keys[stop_1]
        stop_key_2 = self.stop_keys[stop_2]
        key_diff = stop_key_2 - stop_key_1
        key_diff = 1 if key_diff <= 0 else key_diff

        color_1 = self.colors[stop_key_1]
        color_2 = self.colors[stop_key_2]

        d_r, d_g, d_b, d_a = color_2 - color_1
        
        factor = (value - self.stop_keys[stop_1]) * (1 / key_diff)

        if d_r != 0:
            r = color_1.r + (d_r * factor)
        else:
            r = color_1.r
        if d_g != 0:
            g = color_1.g + (d_g * factor)
        else:
            g = color_1.g
        if d_b != 0:
            b = color_1.b + (d_b * factor)
        else:
            b = color_1.b
        if d_a != 0:
            a = color_1.a + (d_a * factor)
        else:
            a = color_1.a

        self.pattern = cairo.SolidPattern(r, g, b, a)


Plugin = Transition
