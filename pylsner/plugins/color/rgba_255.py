from pylsner.plugin import Color

class Plugin(Color):

    def __init__(self, plugin='rgba_255', value=(0, 0, 0, 255)):
        value = (
            value[0] / 255,
            value[1] / 255,
            value[2] / 255,
            value[3] / 255,
        )
        super().__init__(plugin, value)
