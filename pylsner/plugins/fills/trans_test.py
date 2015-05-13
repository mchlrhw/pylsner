import cairo

from pylsner.plugins import Fill


class Transition(Fill):

    def __init__(self, form='rgba', color_stops={0: [0, 0, 0, 1]}):
        stop_keys = sorted(color_stops.keys())
        self.color_stops = {}
        for key, value in color_stops.items():
            key = key / stop_keys[-1]
            self.color_stops[key] = value
        if len(self.color_stops) == 1:
            _, color = self.color_stops.popitem()
            self.pattern = cairo.SolidPattern(*color)
        elif not self.color_stops:
            self.pattern = cairo.SolidPattern(1, 1, 1)

    def refresh(self, cnt, value):
        if not self.color_stops or len(self.color_stops) == 1:
            return self._no_trans()
        else:
            return self._trans(value)

    def _trans(self, value):
        sector = value * 6
        if sector < 1:
            self.pattern = cairo.SolidPattern(1, 0, sector)
        elif sector < 2:
            self.pattern = cairo.SolidPattern(2 - sector, 0, 1)
        elif sector < 3:
            self.pattern = cairo.SolidPattern(0, sector - 2, 1)
        elif sector < 4:
            self.pattern = cairo.SolidPattern(0, 1, 4 - sector)
        elif sector < 5:
            self.pattern = cairo.SolidPattern(sector - 4, 1, 0)
        elif sector < 6:
            self.pattern = cairo.SolidPattern(1, 6 - sector, 0)

    def _no_trans(self):
        return self.pattern


Plugin = Transition
