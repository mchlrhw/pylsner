import cairo

from pylsner.plugin import Fill


class Plugin(Fill):

    def __init__(self, color=(0, 0, 0, 1), **kwargs):
        super().__init__(**kwargs)

        self.pattern = cairo.SolidPattern(*color)
