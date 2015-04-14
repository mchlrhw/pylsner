import cairo

from pylsner.plugins import Fill


class Plugin(Fill):

    def __init__(self, form='rgba', color=[1, 1, 1, 1]):
        if form == 'rgba':
            assert(len(color) == 4)
        elif form == 'rgb':
            assert(len(color) == 3)
            color.append(1)
        elif form == 'rgba_255':
            assert(len(color) == 4)
            color = _reduce_to_frac(color)
        elif form == 'rgb_255':
            assert(len(color) == 3)
            color = _reduce_to_frac(color)
            color.append(1)
        elif form == 'hex':
            assert(len(color) == 6 or len(color) == 7)
            color = _hex_to_rgb(color)

        self._pattern = cairo.SolidPattern(*color)


def _reduce_to_frac(color):
    color = [x / 255 for x in color]
    return color


def _hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    str_len = len(hex_str)
    color = []
    for i in range(0, str_len, str_len // 3):
        color.append(int(hex_str[i:i + (str_len // 3)], 16))
    color = _reduce_to_frac(color)
    return color
