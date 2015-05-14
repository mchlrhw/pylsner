import cairo

from grapefruit.grapefruit import Color
from pylsner.plugins import Fill


class Solid(Fill):

    def __init__(self, color=[1, 1, 1], mode='rgb'):
        if mode == 'rgb' or mode == 'rgba':
            color = Color.NewFromRgb(*color)
        elif mode == 'rgb_255' or mode == 'rgba_255':
            raw_color = color[:]
            color = []
            for comp in raw_color:
                color.append(comp / 255)
            color = Color.NewFromRgb(*color)
        elif mode == 'hex' or mode == 'web' or mode == 'html':
            color = Color.NewFromHtml(color)

        self.pattern = cairo.SolidPattern(*color.rgb, alpha=color.alpha)


Plugin = Solid
