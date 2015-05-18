import cairo

from pylsner.color import Color
from pylsner.plugin import Fill


class Solid(Fill):

    '''\
    A solid colored fill that isn't dependent on the value of a widget
    '''

    def __init__(self, color=[1, 1, 1], mode='rgb'):

        '''\
        Create a new Solid fill instance

        Parameters:
          :color:
            The value of this color in the specified mode(default rgb)
          :mode:
            The color format mode (e.g. rgb, hsl, html, etc.)
        '''

        color = Color(color, mode=mode)
        self.pattern = cairo.SolidPattern(*color.rgb, alpha=color.a)


Plugin = Solid
