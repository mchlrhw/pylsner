import cairo

from pylsner.color import Color
from pylsner.plugins import Fill


class Transition(Fill):

    def __init__(self, colors={0: [1, 1, 1]}, mode='rgb'):
        for stop, color in colors.items():
            color = Color(color, mode=mode)
            colors[stop] = color

        if len(colors) == 1:
            _, color = colors.popitem()
            self.pattern = cairo.SolidPattern(*color.rgb, alpha=color.alpha)
        elif not colors:
            self.pattern = cairo.SolidPattern(1, 1, 1)
        else:
            stop_keys = sorted(colors.keys())
            self.colors = {}
            for key, value in colors.items():
                key = key / stop_keys[-1]
                self.colors[key] = value
            self.stop_keys = sorted(self.colors.keys())

    def refresh(self, cnt, value):
        if not hasattr(self, 'colors'):
            return self._no_trans()
        else:
            return self._trans(value)

    def _trans(self, value):
        # TODO need to make this search more efficient
        for stop_2, key in enumerate(self.stop_keys):
            if value < key:
                break
        stop_1 = stop_2 - 1
        stop_1 = stop_2 if stop_1 < 0 else stop_1

        stop_key_1 = self.stop_keys[stop_1]
        stop_key_2 = self.stop_keys[stop_2]
        key_diff = stop_key_2 - stop_key_1
        key_diff = 1 if key_diff <= 0 else key_diff

        color_1 = self.colors[stop_key_1]
        color_2 = self.colors[stop_key_2]

        diff_r = color_2.r - color_1.r
        diff_g = color_2.g - color_1.g
        diff_b = color_2.b - color_1.b
        
        factor = (value - self.stop_keys[stop_1]) * (1 / key_diff)

        if diff_r != 0:
            r = color_1.r + (diff_r * factor)
        else:
            r = color_1.r
        if diff_g != 0:
            g = color_1.g + (diff_g * factor)
        else:
            g = color_1.g
        if diff_b != 0:
            b = color_1.b + (diff_b * factor)
        else:
            b = color_1.b

        self.pattern = cairo.SolidPattern(r, g, b)

    def _no_trans(self):
        return self.pattern


Plugin = Transition
