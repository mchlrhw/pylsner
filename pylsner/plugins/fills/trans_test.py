import cairo

from pylsner.plugins import Fill


class Plugin(Fill):

    def __init__(self, form='rgba', color_stops={0: [0, 0, 0, 1]}):
        self.color_stops = color_stops

    def _refresh(self, parent):
        value = parent.value
        sector = value * 6
        if sector < 1:
            self._pattern = cairo.SolidPattern(1, 0, sector, 1)
        elif sector < 2:
            self._pattern = cairo.SolidPattern(2 - sector, 0, 1, 1)
        elif sector < 3:
            self._pattern = cairo.SolidPattern(0, sector - 2, 1, 1)
        elif sector < 4:
            self._pattern = cairo.SolidPattern(0, 1, 4 - sector, 1)
        elif sector < 5:
            self._pattern = cairo.SolidPattern(sector - 4, 1, 0, 1)
        elif sector < 6:
            self._pattern = cairo.SolidPattern(1, 6 - sector, 0, 1)
