import cairo

from pylsner.plugin import Fill


class Plugin(Fill):

    def __init__(self, form='rgba', color=[0, 0, 0, 1], **kwargs):
        if form == 'rgba':
            assert(len(color) == 4)
        elif form == 'rgb':
            assert(len(color) == 3)
            color.append(1)
        elif form == 'rgba_255':
            assert(len(color) == 4)
            for elem in color:
                elem = elem / 255
        elif form == 'rgb_255':
            assert(len(color) == 3)
            for elem in color:
                elem = elem / 255
            color.append(1)

        self.pattern = cairo.SolidPattern(*color)
