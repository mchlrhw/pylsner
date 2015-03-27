from pylsner.plugin import Color


class Plugin(Color):

    def __init__(self, plugin='trans_test', value=(0, 0, 0, 1)):
        super().__init__(plugin, value)

    def refresh(self, metric_value):
        sector = metric_value * 6
        if sector < 1:
            self.value = (1, 0, sector, 1)
        elif sector < 2:
            self.value = (2 - sector, 0, 1, 1)
        elif sector < 3:
            self.value = (0, sector - 2, 1, 1)
        elif sector < 4:
            self.value = (0, 1, 4 - sector, 1)
        elif sector < 5:
            self.value = (sector - 4, 1, 0, 1)
        elif sector < 6:
            self.value = (1, 6 - sector, 0, 1)
