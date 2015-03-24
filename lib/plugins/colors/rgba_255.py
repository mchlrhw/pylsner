from .. import Color

class RGBA_255(Color):

    def __init__(self, value=(0, 0, 0, 255)):
        value = (
            value[0] / 255,
            value[1] / 255,
            value[2] / 255,
            value[3] / 255,
        )
        super().__init__(value)
        self.plugin = 'rgba_255'
