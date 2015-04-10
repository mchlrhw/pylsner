import cairo

from pylsner.plugin import Fill, Stateful


class Plugin(Fill, Stateful):

    def __init__(self, form='rgba', color_stops={0: [0, 0, 0, 1]}):
        self.color_stops = color_stops

    def refresh(self, parent):
        value = parent.metric.value
        sector = value * 6
        if sector < 1:
            self.pattern = cairo.SolidPattern(1, 0, sector, 1)
        elif sector < 2:
            self.pattern = cairo.SolidPattern(2 - sector, 0, 1, 1)
        elif sector < 3:
            self.pattern = cairo.SolidPattern(0, sector - 2, 1, 1)
        elif sector < 4:
            self.pattern = cairo.SolidPattern(0, 1, 4 - sector, 1)
        elif sector < 5:
            self.pattern = cairo.SolidPattern(sector - 4, 1, 0, 1)
        elif sector < 6:
            self.pattern = cairo.SolidPattern(1, 6 - sector, 0, 1)
