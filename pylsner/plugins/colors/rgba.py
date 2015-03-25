from pylsner.plugin import Color


class Plugin(Color):

    def __init__(self, plugin='rgba', value=(0, 0, 0, 1)):
        super().__init__(plugin, value)
