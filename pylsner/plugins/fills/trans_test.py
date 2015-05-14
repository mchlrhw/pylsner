import cairo

from pylsner.plugins import Fill


class Transition(Fill):

    def __init__(self, form='rgba', color_stops={0: [1, 1, 1, 1]}):
        if len(color_stops) == 1:
            _, color = color_stops.popitem()
            self.pattern = cairo.SolidPattern(*color)
        elif not color_stops:
            self.pattern = cairo.SolidPattern(1, 1, 1)
        else:
            stop_keys = sorted(color_stops.keys())
            self.color_stops = {}
            for key, value in color_stops.items():
                key = key / stop_keys[-1]
                self.color_stops[key] = value
            self.stop_keys = sorted(self.color_stops.keys())

    def refresh(self, cnt, value):
        if not hasattr(self, 'color_stops'):
            return self._no_trans()
        else:
            return self._trans(value)

    def _trans(self, value):
        for stop_2, key in enumerate(self.stop_keys):
            if value < key:
                break
        stop_1 = stop_2 - 1

        stop_key_1 = self.stop_keys[stop_1]
        stop_key_2 = self.stop_keys[stop_2]
        key_diff = stop_key_2 - stop_key_1

        color_1 = self.color_stops[stop_key_1]
        color_2 = self.color_stops[stop_key_2]

        diff_r = color_2[0] - color_1[0]
        diff_g = color_2[1] - color_1[1]
        diff_b = color_2[2] - color_1[2]
        
        factor = (value - self.stop_keys[stop_1]) * (1 / key_diff)

        if diff_r != 0:
            r = color_1[0] + (diff_r * factor)
        else:
            r = color_1[0]
        if diff_g != 0:
            g = color_1[1] + (diff_g * factor)
        else:
            g = color_1[1]
        if diff_b != 0:
            b = color_1[2] + (diff_b * factor)
        else:
            b = color_1[2]

        self.pattern = cairo.SolidPattern(r, g, b)

    def _no_trans(self):
        return self.pattern


Plugin = Transition
