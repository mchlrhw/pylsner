#!/usr/bin/python
# -*- coding: utf-8 -*-


'''\
A module to perform quick and easy-to-use color conversions

Code for this module originates from the grapefruit color manipulation
package by Xavier Basty and Christian Oudard (xav and christian-oudard
on Github respectively).
The code presented here represents a fork of the original module.
The original license is presented below:

# Copyright (c) 2008, Xavier Basty
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''


NAMED_COLOR = {
    'aliceblue':            '#f0f8ff',
    'antiquewhite':         '#faebd7',
    'aqua':                 '#00ffff',
    'aquamarine':           '#7fffd4',
    'azure':                '#f0ffff',
    'beige':                '#f5f5dc',
    'bisque':               '#ffe4c4',
    'black':                '#000000',
    'blanchedalmond':       '#ffebcd',
    'blue':                 '#0000ff',
    'blueviolet':           '#8a2be2',
    'brown':                '#a52a2a',
    'burlywood':            '#deb887',
    'cadetblue':            '#5f9ea0',
    'chartreuse':           '#7fff00',
    'chocolate':            '#d2691e',
    'coral':                '#ff7f50',
    'cornflowerblue':       '#6495ed',
    'cornsilk':             '#fff8dc',
    'crimson':              '#dc143c',
    'cyan':                 '#00ffff',
    'darkblue':             '#00008b',
    'darkcyan':             '#008b8b',
    'darkgoldenrod':        '#b8860b',
    'darkgray':             '#a9a9a9',
    'darkgrey':             '#a9a9a9',
    'darkgreen':            '#006400',
    'darkkhaki':            '#bdb76b',
    'darkmagenta':          '#8b008b',
    'darkolivegreen':       '#556b2f',
    'darkorange':           '#ff8c00',
    'darkorchid':           '#9932cc',
    'darkred':              '#8b0000',
    'darksalmon':           '#e9967a',
    'darkseagreen':         '#8fbc8f',
    'darkslateblue':        '#483d8b',
    'darkslategray':        '#2f4f4f',
    'darkslategrey':        '#2f4f4f',
    'darkturquoise':        '#00ced1',
    'darkviolet':           '#9400d3',
    'deeppink':             '#ff1493',
    'deepskyblue':          '#00bfff',
    'dimgray':              '#696969',
    'dimgrey':              '#696969',
    'dodgerblue':           '#1e90ff',
    'firebrick':            '#b22222',
    'floralwhite':          '#fffaf0',
    'forestgreen':          '#228b22',
    'fuchsia':              '#ff00ff',
    'gainsboro':            '#dcdcdc',
    'ghostwhite':           '#f8f8ff',
    'gold':                 '#ffd700',
    'goldenrod':            '#daa520',
    'gray':                 '#808080',
    'grey':                 '#808080',
    'green':                '#008000',
    'greenyellow':          '#adff2f',
    'honeydew':             '#f0fff0',
    'hotpink':              '#ff69b4',
    'indianred':            '#cd5c5c',
    'indigo':               '#4b0082',
    'ivory':                '#fffff0',
    'khaki':                '#f0e68c',
    'lavender':             '#e6e6fa',
    'lavenderblush':        '#fff0f5',
    'lawngreen':            '#7cfc00',
    'lemonchiffon':         '#fffacd',
    'lightblue':            '#add8e6',
    'lightcoral':           '#f08080',
    'lightcyan':            '#e0ffff',
    'lightgoldenrodyellow': '#fafad2',
    'lightgray':            '#d3d3d3',
    'lightgrey':            '#d3d3d3',
    'lightgreen':           '#90ee90',
    'lightpink':            '#ffb6c1',
    'lightsalmon':          '#ffa07a',
    'lightseagreen':        '#20b2aa',
    'lightskyblue':         '#87cefa',
    'lightslategray':       '#778899',
    'lightslategrey':       '#778899',
    'lightsteelblue':       '#b0c4de',
    'lightyellow':          '#ffffe0',
    'lime':                 '#00ff00',
    'limegreen':            '#32cd32',
    'linen':                '#faf0e6',
    'magenta':              '#ff00ff',
    'maroon':               '#800000',
    'mediumaquamarine':     '#66cdaa',
    'mediumblue':           '#0000cd',
    'mediumorchid':         '#ba55d3',
    'mediumpurple':         '#9370db',
    'mediumseagreen':       '#3cb371',
    'mediumslateblue':      '#7b68ee',
    'mediumspringgreen':    '#00fa9a',
    'mediumturquoise':      '#48d1cc',
    'mediumvioletred':      '#c71585',
    'midnightblue':         '#191970',
    'mintcream':            '#f5fffa',
    'mistyrose':            '#ffe4e1',
    'moccasin':             '#ffe4b5',
    'navajowhite':          '#ffdead',
    'navy':                 '#000080',
    'oldlace':              '#fdf5e6',
    'olive':                '#808000',
    'olivedrab':            '#6b8e23',
    'orange':               '#ffa500',
    'orangered':            '#ff4500',
    'orchid':               '#da70d6',
    'palegoldenrod':        '#eee8aa',
    'palegreen':            '#98fb98',
    'paleturquoise':        '#afeeee',
    'palevioletred':        '#db7093',
    'papayawhip':           '#ffefd5',
    'peachpuff':            '#ffdab9',
    'peru':                 '#cd853f',
    'pink':                 '#ffc0cb',
    'plum':                 '#dda0dd',
    'powderblue':           '#b0e0e6',
    'purple':               '#800080',
    'rebeccapurple':        '#663399',
    'red':                  '#ff0000',
    'rosybrown':            '#bc8f8f',
    'royalblue':            '#4169e1',
    'saddlebrown':          '#8b4513',
    'salmon':               '#fa8072',
    'sandybrown':           '#f4a460',
    'seagreen':             '#2e8b57',
    'seashell':             '#fff5ee',
    'sienna':               '#a0522d',
    'silver':               '#c0c0c0',
    'skyblue':              '#87ceeb',
    'slateblue':            '#6a5acd',
    'slategray':            '#708090',
    'slategrey':            '#708090',
    'snow':                 '#fffafa',
    'springgreen':          '#00ff7f',
    'steelblue':            '#4682b4',
    'tan':                  '#d2b48c',
    'teal':                 '#008080',
    'thistle':              '#d8bfd8',
    'tomato':               '#ff6347',
    'turquoise':            '#40e0d0',
    'violet':               '#ee82ee',
    'wheat':                '#f5deb3',
    'white':                '#ffffff',
    'whitesmoke':           '#f5f5f5',
    'yellow':               '#ffff00',
    'yellowgreen':          '#9acd32',
}

WHITE_REFERENCE = {
    'std_A'   : (1.09847, 1.00000, 0.35582),
    'std_B'   : (0.99093, 1.00000, 0.85313),
    'std_C'   : (0.98071, 1.00000, 1.18225),
    'std_D50' : (0.96421, 1.00000, 0.82519),
    'std_D55' : (0.95680, 1.00000, 0.92148),
    'std_D65' : (0.95043, 1.00000, 1.08890),
    'std_D75' : (0.94972, 1.00000, 1.22639),
    'std_E'   : (1.00000, 1.00000, 1.00000),
    'std_F1'  : (0.92834, 1.00000, 1.03665),
    'std_F2'  : (0.99145, 1.00000, 0.67316),
    'std_F3'  : (1.03753, 1.00000, 0.49861),
    'std_F4'  : (1.09147, 1.00000, 0.38813),
    'std_F5'  : (0.90872, 1.00000, 0.98723),
    'std_F6'  : (0.97309, 1.00000, 0.60191),
    'std_F7'  : (0.95017, 1.00000, 1.08630),
    'std_F8'  : (0.96413, 1.00000, 0.82333),
    'std_F9'  : (1.00365, 1.00000, 0.67868),
    'std_F10' : (0.96174, 1.00000, 0.81712),
    'std_F11' : (1.00899, 1.00000, 0.64262),
    'std_F12' : (1.08046, 1.00000, 0.39228),
    'sup_A'   : (1.11142, 1.00000, 0.35200),
    'sup_B'   : (0.99178, 1.00000, 0.84349),
    'sup_C'   : (0.97286, 1.00000, 1.16145),
    'sup_D50' : (0.96721, 1.00000, 0.81428),
    'sup_D55' : (0.95797, 1.00000, 0.90925),
    'sup_D65' : (0.94810, 1.00000, 1.07305),
    'sup_D75' : (0.94417, 1.00000, 1.20643),
    'sup_E'   : (1.00000, 1.00000, 1.00000),
    'sup_F1'  : (0.94791, 1.00000, 1.03191),
    'sup_F2'  : (1.03245, 1.00000, 0.68990),
    'sup_F3'  : (1.08968, 1.00000, 0.51965),
    'sup_F4'  : (1.14961, 1.00000, 0.40963),
    'sup_F5'  : (0.93369, 1.00000, 0.98636),
    'sup_F6'  : (1.02148, 1.00000, 0.62074),
    'sup_F7'  : (0.95780, 1.00000, 1.07618),
    'sup_F8'  : (0.97115, 1.00000, 0.81135),
    'sup_F9'  : (1.02116, 1.00000, 0.67826),
    'sup_F10' : (0.99001, 1.00000, 0.83134),
    'sup_F11' : (1.03820, 1.00000, 0.65555),
    'sup_F12' : (1.11428, 1.00000, 0.40353),
}

# The default white reference, use 2° Standard Observer, D65 (daylight)
DEFAULT_WREF = WHITE_REFERENCE['std_D65']

SRGB_GAMMA_CORR_INV = 0.03928 / 12.92

RYB_WHEEL = (
    0,  26,  52, 83, 120,
    130, 141, 151, 162, 177,
    190, 204, 218, 232, 246,
    261, 275, 288, 303, 317,
    330, 338, 345, 352, 360,
)

RGB_WHEEL = (
    0,   8,  17, 26,  34,
    41, 48,  54,  60, 81,
    103, 123, 138, 155, 171,
    187, 204, 219, 234, 251,
    267, 282, 298, 329, 360,
)


class Color:

    '''\
    A class to hold the RGBA representation of a color.
    The internal representation of the color is always stored as RGBA floats;
    however, intances of Color have a number of properties that enable easy
    conversion to other formats.
    It is also possible to create new Color instances from other formats by
    specifying them at creation time.

    Example usage:

    To create an instance of a Color from RGB values:

      >>> from color import Color
      >>> rgb = 1, 0.5, 0
      >>> clr_1 = Color(rgb)
      >>> clr_1
      (1.0, 0.5, 0.0, 1)

    To create an instance from another format, for example hsl:

      >>> hsl = 30, 1, 0.5
      >>> clr_1 = Color(hsl, mode='hsl')
      >>> clr_1
      (1.0, 0.5, 0.0, 1)

    To get the values of the color in another colorspace:

      >>> clr_1.hsv
      (30.0, 1.0, 1.0)
      >>> clr_1.lab
      (66.95182379630494, 0.4308396497520478, 0.7396923149088841)

    To find the difference between one color and another:

      >>> clr_2 = Color((0.6, 0.6, 0.6), 0.6)
      >>> clr_1 - clr_2
      (0.4, -0.09999999999999998, -0.6, 0.4)

    There are also methods to darken, lighten, saturate, desaturate and
    change the hue of a Color instance, as well as copy existing Color
    instances.
    '''

    def __init__(self, color, alpha=1, *, mode='rgb', wref=DEFAULT_WREF):

        '''\
        Instantiate a new Color object.

        Parameters:
          :color:
            The value of this color, in the specified mode (default rgb).
          :alpha:
            The alpha value (transparency) of this color.
          :mode:
            The representation mode used for the color.
          :wref:
            The whitepoint reference (default 2° D65).
        '''

        if mode == 'rgb':
            if not len(color) == 3:
                raise TypeError('color must be a 3-tuple')
            try:
                color = tuple(float(c) for c in color)
            except (TypeError, ValueError):
                raise TypeError(
                    'invalid color tuple: {}'.format(color)
                )
            rgb_tuple = color
        elif mode in ('hex', 'html', 'name', 'web'):
            if mode == 'hex':
                color = str(color)
                color = color.lstrip('#')
                try:
                    int(color, 16)
                except ValueError:
                    raise TypeError('color must be a valid hex code')
            elif mode == 'name':
                color = color.lower()
                if color not in NAMED_COLOR:
                    raise TypeError('color must be a valid html color name')
            rgb_tuple = html_to_rgb(color)
        elif mode == 'cmy':
            rgb_tuple = cmy_to_rgb(*color)
        elif mode == 'cmyk':
            rgb_tuple = cmyk_to_rgb(*color)
        elif mode == 'hsl':
            rgb_tuple = hsl_to_rgb(*color)
        elif mode == 'hsv':
            rgb_tuple = hsv_to_rgb(*color)
        elif mode == 'int':
            rgb_tuple = int_to_rgb(*color)
        elif mode == 'lab':
            rgb_tuple = lab_to_rgb(*color, wref=wref)
        elif mode == 'pil':
            rgb_tuple = pil_to_rgb(color)
        elif mode == 'xyz':
            rgb_tuple = xyz_to_rgb(*color)
        elif mode == 'yiq':
            rgb_tuple = yiq_to_rgb(*color)
        elif mode == 'yuv':
            rgb_tuple = yuv_to_rgb(*color)
        else:
            raise ValueError('invalid color mode: ' + mode)

        self.r, self.g, self.b = rgb_tuple
        self.a = alpha
        self._wref = wref

    def __ne__(self, other):

        return not self.__eq__(other)

    def __eq__(self, other):

        try:
            if isinstance(other, Color):
                return (self.rgb == other.rgb) and (self.a == other.a)
            if len(other) != 4:
                return False
            return list(self.rgba) == list(other)
        except TypeError:
            return False
        except AttributeError:
            return False

    def __sub__(self, other):

        dr = self.r - other.r
        dg = self.g - other.g
        db = self.b - other.b
        da = self.a - other.a
        return dr, dg, db, da

    def __repr__(self):

        return str(self.rgba)

    def __str__(self):

        '''\
        A string representing this Color instance

        Returns:
          The RGBA representation of this Color instance
        '''

        return '({}, {}, {}, {})'.format(*self.rgba)

    def __iter__(self):

        '''\
        Iterate over the RGBA elements of this color

        Returns:
          An iterator over the RGBA elements
        '''

        return iter(self.rgba)

    def __len__(self):

        '''\
        Get the length of this Color

        Returns:
          The length of this color, which is always 4 (RGBA)
        '''

        return 4

    def __copy__(self):

        '''\
        Create a new Color instance from this one

        Parameters:
          :color:
            The color to be copied

        Returns:
          A new Color instance with the same interal RGBA
          representation as this one
        '''

        return Color(self.rgb, self.a, wref=self.wref)

    @property
    def rgb(self):

        return self.r, self.g, self.b

    @rgb.setter
    def rgb(self, rgb_tuple):
        
        self.r, self.g, self.b = rgb_tuple

    @property
    def rgba(self):

        return self.rgb + (self.a,)

    @rgba.setter
    def rgba(self, rgba_tuple):
        
        self.r, self.g, self.b, self.a = rgba_tuple

    @property
    def red(self):

        return self.r

    @red.setter(self, r):

        self.r = r

    @property
    def blue(self):

        return self.b

    @blue.setter
    def blue(self, b):

        self.b = b

    @property
    def green(self):

        return self.g

    @green.setter
    def green(self, g):

        self.g = g

    @property
    def alpha(self):

        return self.a

    @alpha.setter
    def alpha(self, a):
        self.a = a

    @property
    def wref(self):

        return self._wref

    @wref.setter
    def wref(self, wref):

        l, a, b = rgb_to_lab(*self.rgb, wref=self._wref)
        self.rgb = lab_to_rgb(l, a, b, wref=wref)
        self._wref = wref

    @property
    def hsl(self):

        return rgb_to_hsl(*self.rgb)

    @hsl.setter
    def hsl(self, hsl_tuple):

        self.rgb = hsl_to_rgb(*hsl_tuple)

    @property
    def h(self):

        h, _, _ = self.hsl
        return h

    @h.setter
    def h(self, h):

        _, s, l = rgb_to_hsl(*self.rgb)
        self.rgb = hsl_to_rgb(h, s, l)

    @property
    def s(self):

        _, s, _ = self.hsl
        return s

    @s.setter
    def s(self, s):

        h, _, l = rgb_to_hsl(*self.rgb)
        self.rgb = hsl_to_rgb(h, s, l)

    @property
    def l(self):

        _, _, l = self.hsl
        return l

    @l.setter
    def l(self, l):

        h, s, _ = rgb_to_hsl(*self.rgb)
        self.rgb = hsl_to_rgb(h, s, l)

    @property
    def hue(self):

        return self.h

    @hue.setter
    def hue(self, h):

        self.h = h

    @property
    def saturation(self):

        return self.s

    @saturation.setter
    def saturation(self, s):

        self.s = s

    @property
    def lightness(self):

        return self.l

    @lightness.setter
    def lightness(self, l):

        self.l = l

    @property
    def cmy(self):
        return rgb_to_cmy(*self.rgb)

    @property
    def cmyk(self):
        return rgb_to_cmyk(*self.rgb)

    @property
    def hex(self):
        return self.html

    @property
    def hsv(self):
        return rgb_to_hsv(*self.rgb)

    @property
    def html(self):
        return rgb_to_html(*self.rgb)

    @property
    def int(self):
        return rgb_to_int(*self.rgb)

    @property
    def lab(self):
        return rgb_to_lab(*self.rgb, wref=self.wref)

    @property
    def pil(self):
        return rgb_to_pil(*self.rgb)

    @property
    def xyz(self):
        return rgb_to_xyz(*self.rgb)

    @property
    def yiq(self):
        return rgb_to_yiq(*self.rgb)

    @property
    def yuv(self):
        return rgb_to_yuv(*self.rgb)

    def is_legal(self):

        '''\
        Determine whether the color is legal

        Returns:
          A boolean indicating whether the color is within the legal gamut
        '''

        return all(0 <= v <= 1 for v in self)

    def make_legal(self):

        '''\
        Ensure this Color instance is legal

        If it isn't, set its r, g, b and a attributes to
        the nearest legal values
        '''

        def clamp(x, lo, hi):
            if x < lo:
                return lo
            elif x > hi:
                return hi
            else:
                return x

        if not self.is_legal():
            *rgb, a = tuple(clamp(v, 0, 1) for v in self)
            self.rgba = rgb + (a,)
            
    def darken(self, level):

        '''\
        '''

        level = abs(level)
        l = self.lightness
        self.lightness = max(l - level, 0)

    def lighten(self, level):

        '''\
        '''

        level = abs(level)
        l = self.lightness
        self.lightness = min(l + level, 1)

    def saturate(self, level):

        '''\
        '''

        level = abs(level)
        s = self.saturation
        self.saturation = min(s + level, 1)

    def desaturate(self, level):

        '''\
        '''

        level = abs(level)
        s = self.saturation
        self.saturation = max(s - level, 0)


def rgb_to_hsl(r, g, b):

    '''\
    Convert the color from RGB coordinates to HSL.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      The color as an (h, s, l) tuple in the range:
        h[0...360],
        s[0...1],
        l[0...1],

    >>> Color.RgbToHsl(1, 0.5, 0)
    (30.0, 1.0, 0.5)
    '''

    min_val = min(r, g, b)
    max_val = max(r, g, b)

    l = (max_val + min_val) / 2
    if min_val == max_val:
        return (0, 0, l) # achromatic (gray)

    d = max_val - min_val # delta RGB value
    if l < 0.5:
        s = d / (max_val + min_val)
    else:
        s = d / (2 - max_val - min_val)
    dr, dg, db = [(max_val - val) / d for val in (r, g, b)]

    if r == max_val:
        h = db - dg
    elif g == max_val:
        h = 2 + dr - db
    else:
        h = 4 + dg - dr
    h = (h * 60) % 360

    return (h, s, l)


def _hue_to_rgb(n1, n2, h):

    h %= 6
    if h < 1:
        return n1 + ((n2 - n1) * h)
    if h < 3:
        return n2
    if h < 4:
        return n1 + ((n2 - n1) * (4 - h))
    return n1


def hsl_to_rgb(h, s, l):

    '''\
    Convert from HSL to RGB coordinates.

    Parameters:
      :h:
        The Hue component value [0...360]
      :s:
        The Saturation component value [0...1]
      :l:
        The Lightness component value [0...1]

    Returns:
      The color as an (r, g, b) tuple in the range:
        r[0...1],
        g[0...1],
        b[0...1],

    >>> Color.HslToRgb(30.0, 1.0, 0.5)
    (1.0, 0.5, 0.0)
    '''

    if s == 0:
        return (l, l, l) # achromatic (gray)

    if l < 0.5:
        n2 = l * (1 + s)
    else:
        n2 = (l + s) - (l * s)
    n1 = (2 * l) - n2
    h /= 60

    r = _hue_to_rgb(n1, n2, h + 2)
    g = _hue_to_rgb(n1, n2, h)
    b = _hue_to_rgb(n1, n2, h - 2)

    return r, g, b


def rgb_to_hsv(r, g, b):

    '''\
    Convert the color from RGB coordinates to HSV.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      The color as an (h, s, v) tuple in the range:
        h[0...360],
        s[0...1],
        v[0...1],

    >>> Color.RgbToHsv(1, 0.5, 0)
    (30.0, 1.0, 1.0)
    '''

    v = max(r, g, b)
    d = v - min(r, g, b)
    if d == 0:
        return (0, 0, v)
    s = d / v

    dr, dg, db = [(v - val) / d for val in (r, g, b)]

    if r == v:
        h = db - dg # between yellow & magenta
    elif g == v:
        h = 2 + dr - db # between cyan & yellow
    else:
        h = 4 + dg - dr # between magenta & cyan

    h = (h*60.0) % 360.0
    return (h, s, v)


def hsv_to_rgb(h, s, v):

    '''\
    Convert the color from RGB coordinates to HSV.

    Parameters:
      :h:
        The Hue component value [0...360]
      :s:
        The Saturation component value [0...1]
      :v:
        The Value component [0...1]

    Returns:
      The color as an (r, g, b) tuple in the range:
        r[0...1],
        g[0...1],
        b[0...1],

    >>> Color.HslToRgb(30.0, 1.0, 0.5)
    (1.0, 0.5, 0.0)
    '''

    if s == 0:
        return (v, v, v) # achromatic (gray)

    h /= 60
    h = h % 6

    i = int(h)
    f = h - i
    # if i is even
    if not(i & 1):
        f = 1 - f

    m = v * (1 - s)
    n = v * (1 - (s * f))

    if i == 0:
        return (v, n, m)
    if i == 1:
        return (n, v, m)
    if i == 2:
        return (m, v, n)
    if i == 3:
        return (m, n, v)
    if i == 4:
        return (n, m, v)
    return (v, m, n)


def rgb_to_yiq(r, g, b):

    '''\
    Convert the color from RGB to YIQ.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      The color as an (y, i, q) tuple in the range:
      y[0...1],
      i[0...1],
      q[0...1]

    >>> '(%g, %g, %g)' % Color.RgbToYiq(1, 0.5, 0)
    '(0.592263, 0.458874, -0.0499818)'
    '''

    y = (r * 0.29895808) + (g * 0.58660979) + (b * 0.11443213)
    i = (r * 0.59590296) - (g * 0.27405705) - (b * 0.32184591)
    q = (r * 0.21133576) - (g * 0.52263517) + (b * 0.31129940)
    return (y, i, q)


def yiq_to_rgb(y, i, q):

    '''\
    Convert the color from YIQ coordinates to RGB.

    Parameters:
      :y:
        Tte Y component value [0...1]
      :i:
        The I component value [0...1]
      :q:
        The Q component value [0...1]

    Returns:
      The color as an (r, g, b) tuple in the range:
      r[0...1],
      g[0...1],
      b[0...1]

    >>> '(%g, %g, %g)' % Color.YiqToRgb(0.592263, 0.458874, -0.0499818)
    '(1, 0.5, 5.442e-07)'
    '''

    r = y + (i * 0.9562) + (q * 0.6210)
    g = y - (i * 0.2717) - (q * 0.6485)
    b = y - (i * 1.1053) + (q * 1.7020)
    return (r, g, b)


def rgb_to_yuv(r, g, b):

    '''\
    Convert the color from RGB coordinates to YUV.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      The color as an (y, u, v) tuple in the range:
      y[0...1],
      u[-0.436...0.436],
      v[-0.615...0.615]

    >>> '(%g, %g, %g)' % Color.RgbToYuv(1, 0.5, 0)
    '(0.5925, -0.29156, 0.357505)'
    '''

    y =  (r * 0.29900) + (g * 0.58700) + (b * 0.11400)
    u = -(r * 0.14713) - (g * 0.28886) + (b * 0.43600)
    v =  (r * 0.61500) - (g * 0.51499) - (b * 0.10001)
    return (y, u, v)


def yuv_to_rgb(y, u, v):

    '''\
    Convert the color from YUV coordinates to RGB.

    Parameters:
      :y:
        The Y component value [0...1]
      :u:
        The U component value [-0.436...0.436]
      :v:
        The V component value [-0.615...0.615]

    Returns:
      The color as an (r, g, b) tuple in the range:
      r[0...1],
      g[0...1],
      b[0...1]

    >>> '(%g, %g, %g)' % Color.YuvToRgb(0.5925, -0.2916, 0.3575)
    '(0.999989, 0.500015, -6.3276e-05)'
    '''

    r = y + (v * 1.13983)
    g = y - (u * 0.39465) - (v * 0.58060)
    b = y + (u * 2.03211)
    return (r, g, b)


def rgb_to_xyz(r, g, b):

    '''\
    Convert the color from sRGB to CIE XYZ.

    The methods assumes that the RGB coordinates are given in the sRGB
    colorspace (D65).

    .. note::

       Compensation for the sRGB gamma correction is applied before converting.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      The color as an (x, y, z) tuple in the range:
      x[0...1],
      y[0...1],
      z[0...1]

    >>> '(%g, %g, %g)' % Color.RgbToXyz(1, 0.5, 0)
    '(0.488941, 0.365682, 0.0448137)'
    '''

    r, g, b = [((v <= 0.03928) and [v / 12.92] or [((v + 0.055) / 1.055) ** 2.4])[0] for v in (r, g, b)]

    x = (r * 0.4124) + (g * 0.3576) + (b * 0.1805)
    y = (r * 0.2126) + (g * 0.7152) + (b * 0.0722)
    z = (r * 0.0193) + (g * 0.1192) + (b * 0.9505)
    return (x, y, z)


def xyz_to_rgb(x, y, z):

    '''\
    Convert the color from CIE XYZ coordinates to sRGB.

    .. note::

       Compensation for sRGB gamma correction is applied before converting.

    Parameters:
      :x:
        The X component value [0...1]
      :y:
        The Y component value [0...1]
      :z:
        The Z component value [0...1]

    Returns:
      The color as an (r, g, b) tuple in the range:
      r[0...1],
      g[0...1],
      b[0...1]

    >>> '(%g, %g, %g)' % Color.XyzToRgb(0.488941, 0.365682, 0.0448137)
    '(1, 0.5, 6.81883e-08)'
    '''

    r =  (x * 3.2406255) - (y * 1.5372080) - (z * 0.4986286)
    g = -(x * 0.9689307) + (y * 1.8757561) + (z * 0.0415175)
    b =  (x * 0.0557101) - (y * 0.2040211) + (z * 1.0569959)
    return tuple((((v <= SRGB_GAMMA_CORR_INV) and [v * 12.92] or [(1.055 * (v ** (1 / 2.4))) - 0.055])[0] for v in (r, g, b)))


def xyz_to_lab(x, y, z, wref=DEFAULT_WREF):

    '''\
    Convert the color from CIE XYZ to CIE L*a*b*.

    Parameters:
      :x:
        The X component value [0...1]
      :y:
        The Y component value [0...1]
      :z:
        The Z component value [0...1]
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      The color as an (L, a, b) tuple in the range:
      L[0...100],
      a[-1...1],
      b[-1...1]

    >>> '(%g, %g, %g)' % Color.XyzToLab(0.488941, 0.365682, 0.0448137)
    '(66.9518, 0.43084, 0.739692)'

    >>> '(%g, %g, %g)' % Color.XyzToLab(0.488941, 0.365682, 0.0448137, Color.WHITE_REFERENCE['std_D50'])
    '(66.9518, 0.411663, 0.67282)'
    '''

    # White point correction
    x /= wref[0]
    y /= wref[1]
    z /= wref[2]

    # Nonlinear distortion and linear transformation
    x, y, z = [((v > 0.008856) and [v ** (1 / 3)] or [(7.787 * v) + (16 / 116)])[0] for v in (x, y, z)]

    # Vector scaling
    l = (116 * y) - 16
    a = 5 * (x - y)
    b = 2 * (y - z)

    return (l, a, b)


def lab_to_xyz(l, a, b, wref=DEFAULT_WREF):

    '''\
    Convert the color from CIE L*a*b* to CIE 1931 XYZ.

    Parameters:
      :l:
        The L component [0...100]
      :a:
        The a component [-1...1]
      :b:
        The a component [-1...1]
      :wref:
        The whitepoint reference, default is 2° D65.

    Returns:
      The color as an (x, y, z) tuple in the range:
      x[0...q],
      y[0...1],
      z[0...1]

    >>> '(%g, %g, %g)' % Color.LabToXyz(66.9518, 0.43084, 0.739692)
    '(0.488941, 0.365682, 0.0448137)'

    >>> '(%g, %g, %g)' % Color.LabToXyz(66.9518, 0.411663, 0.67282, Color.WHITE_REFERENCE['std_D50'])
    '(0.488941, 0.365682, 0.0448138)'
    '''

    y = (l + 16) / 116
    x = (a / 5) + y
    z = y - (b / 2)
    return tuple((((v > 0.206893) and [v ** 3] or [(v - (16 / 116)) / 7.787])[0] * w for v, w in zip((x, y, z), wref)))


def rgb_to_lab(r, g, b, wref=DEFAULT_WREF):

    return xyz_to_lab(*rgb_to_xyz(r, g, b), wref=wref)


def lab_to_rgb(l, a, b, wref=DEFAULT_WREF):

    return xyz_to_rgb(*lab_to_xyz(l, a, b, wref=wref))


def rgb_to_cmy(r, g, b):

    '''\
    Convert the color from RGB coordinates to CMY.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      The color as an (c, m, y) tuple in the range:
      c[0...1],
      m[0...1],
      y[0...1]

    >>> Color.RgbToCmy(1, 0.5, 0)
    (0, 0.5, 1)
    '''

    return (1 - r, 1 - g, 1 - b)


def cmy_to_rgb(c, m, y):

    '''\
    Convert the color from CMY coordinates to RGB.

    Parameters:
      :c:
        The Cyan component value [0...1]
      :m:
        The Magenta component value [0...1]
      :y:
        The Yellow component value [0...1]

    Returns:
      The color as an (r, g, b) tuple in the range:
      r[0...1],
      g[0...1],
      b[0...1]

    >>> Color.CmyToRgb(0, 0.5, 1)
    (1, 0.5, 0)
    '''

    return (1 - c, 1 - m, 1 - y)


def cmyk_to_cmy(c, m, y, k):

    '''\
    Convert the color from CMYK coordinates to CMY.

    Parameters:
      :c:
        The Cyan component value [0...1]
      :m:
        The Magenta component value [0...1]
      :y:
        The Yellow component value [0...1]
      :k:
        The Black component value [0...1]

    Returns:
      The color as an (c, m, y) tuple in the range:
      c[0...1],
      m[0...1],
      y[0...1]

    >>> '(%g, %g, %g)' % Color.CmykToCmy(1, 0.32, 0, 0.5)
    '(1, 0.66, 0.5)'
    '''

    mk = 1 - k
    return (((c * mk) + k), ((m * mk) + k), ((y * mk) + k))


def cmy_to_cmyk(c, m, y):

    '''\
    Convert the color from CMY coordinates to CMYK.

    Parameters:
      :c:
        The Cyan component value [0...1]
      :m:
        The Magenta component value [0...1]
      :y:
        The Yellow component value [0...1]

    Returns:
      The color as an (c, m, y, k) tuple in the range:
      c[0...1],
      m[0...1],
      y[0...1],
      k[0...1]

    >>> '(%g, %g, %g, %g)' % Color.CmyToCmyk(1, 0.66, 0.5)
    '(1, 0.32, 0, 0.5)'
    '''

    k = min(c, m, y)
    if k == 1:
        return (0, 0, 0, 1)
    mk = 1 - k
    return ((c - k) / mk, (m - k) / mk, (y - k) / mk, k)


def rgb_to_cmyk(r, g, b):

    return cmy_to_cmyk(rgb_to_cmy(r, g, b))


def cmyk_to_rgb(c, m, y, k):

    return cmy_to_rgb(cmyk_to_cmy(c, m, y, k))


def rgb_to_int(r, g, b):

    '''\
    Convert the color from (r, g, b) to an int tuple.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      The color as an (r, g, b) tuple in the range:
      r[0...255],
      g[0...255],
      b[0...255]

    >>> Color.RgbToIntTuple(1, 0.5, 0)
    (255, 128, 0)
    '''

    return tuple(int(round(v * 255)) for v in (r, g, b))


def int_to_rgb(r, g, b):

    '''\
    Convert a tuple of ints to (r, g, b).

    Parameters:
      The color as an (r, g, b) integer tuple in the range:
      r[0...255],
      g[0...255],
      b[0...255]

    Returns:
      The color as an (r, g, b) tuple in the range:
      r[0...1],
      g[0...1],
      b[0...1]

    >>> '(%g, %g, %g)' % Color.IntTupleToRgb((255, 128, 0))
    '(1, 0.501961, 0)'
    '''

    return tuple(v / 255 for v in (r, g, b))


def rgb_to_html(r, g, b):

    '''\
    Convert the color from (r, g, b) to #RRGGBB.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      A CSS string representation of this color (#RRGGBB).

    >>> Color.RgbToHtml(1, 0.5, 0)
    '#ff8000'
    '''

    return '#%02x%02x%02x' % tuple((min(round(v * 255), 255) for v in (r, g, b)))


def html_to_rgb(html):

    '''\
    Convert the HTML color to (r, g, b).

    Parameters:
      :html:
        the HTML definition of the color (#RRGGBB or #RGB or a color name).

    Returns:
      The color as an (r, g, b) tuple in the range:
      r[0...1],
      g[0...1],
      b[0...1]

    Throws:
      :ValueError:
        If html is neither a known color name or a hexadecimal RGB
        representation.

    >>> '(%g, %g, %g)' % Color.HtmlToRgb('#ff8000')
    '(1, 0.501961, 0)'
    >>> '(%g, %g, %g)' % Color.HtmlToRgb('ff8000')
    '(1, 0.501961, 0)'
    >>> '(%g, %g, %g)' % Color.HtmlToRgb('#f60')
    '(1, 0.4, 0)'
    >>> '(%g, %g, %g)' % Color.HtmlToRgb('f60')
    '(1, 0.4, 0)'
    >>> '(%g, %g, %g)' % Color.HtmlToRgb('lemonchiffon')
    '(1, 0.980392, 0.803922)'
    '''

    html = str(html)
    html = html.strip().lower()
    if html[0] == '#':
        html = html[1:]
    elif html in NAMED_COLOR:
        html = NAMED_COLOR[html][1:]

    if len(html) == 6:
        rgb = html[:2], html[2:4], html[4:]
    elif len(html) == 3:
        rgb = ['%c%c' % (v, v) for v in html]
    else:
        raise ValueError('{} is not in valid hex format or is not a valid color name'.format(html))

    return tuple(((int(n, 16) / 255) for n in rgb))


def rgb_to_pil(r, g, b):

    '''\
    Convert the color from RGB to a PIL-compatible integer.

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      A PIL compatible integer (0xBBGGRR).

    >>> '0x%06x' % Color.RgbToPil(1, 0.5, 0)
    '0x0080ff'
    '''

    r, g, b = [min(int(round(v * 255)), 255) for v in (r, g, b)]
    return (b << 16) + (g << 8) + r


def pil_to_rgb(pil):

    '''\
    Convert the color from a PIL-compatible integer to RGB.

    Parameters:
      pil: a PIL compatible color representation (0xBBGGRR)
    Returns:
      The color as an (r, g, b) tuple in the range:
      the range:
      r: [0...1]
      g: [0...1]
      b: [0...1]

    >>> '(%g, %g, %g)' % Color.PilToRgb(0x0080ff)
    '(1, 0.501961, 0)'
    '''

    try:
        int(pil, 16)
    except ValueError:
        raise TypeError('cannot convert pil to hex integer: {}'.format(pil))

    r = 0xff & pil
    g = 0xff & (pil >> 8)
    b = 0xff & (pil >> 16)
    return tuple((v / 255 for v in (r, g, b)))


def _web_safe_component(c, alt=False):

    '''\
    Convert a color component to its web safe equivalent.

    Parameters:
      :c:
        The component value [0...1]
      :alt:
        If True, return the alternative value instead of the nearest one.

    Returns:
      The web safe equivalent of the component value.
    '''

    try:
        c = float(c)
    except ValueError:
        raise TypeError('cannot convert c to a float: {}'.format(c))

    # This sucks, but floating point between 0 and 1 is quite fuzzy...
    # So we just change the scale a while to make the equality tests
    # work, otherwise it gets wrong at some decimal far to the right.
    sc = c * 100

    # If the color is already safe, return it straight away
    d = sc % 20
    if d == 0:
        return c

    # Get the lower and upper safe values
    l = sc - d
    u = l + 20

    # Return the 'closest' value according to the alt flag
    if alt:
        if (sc - l) >= (u - sc):
            return l / 100
        else:
            return u / 100
    else:
        if (sc - l) >= (u - sc):
            return u / 100
        else:
            return l / 100


def rgb_to_websafe(r, g, b, alt=False):

    '''\
    Convert the color from RGB to 'web safe' RGB

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]
      :alt:
        If True, use the alternative color instead of the nearest one.
        Can be used for dithering.

    Returns:
      The color as an (r, g, b) tuple in the range:
      the range:
      r[0...1],
      g[0...1],
      b[0...1]

    >>> '(%g, %g, %g)' % Color.RgbToWebSafe(1, 0.55, 0.0)
    '(1, 0.6, 0)'
    '''

    return tuple((_web_safe_component(v, alt) for v in (r, g, b)))


def rgb_to_greyscale(r, g, b):

    '''\
    Convert the color from RGB to its greyscale equivalent

    Parameters:
      :r:
        The Red component value [0...1]
      :g:
        The Green component value [0...1]
      :b:
        The Blue component value [0...1]

    Returns:
      The color as an (r, g, b) tuple in the range:
      the range:
      r[0...1],
      g[0...1],
      b[0...1]

    >>> '(%g, %g, %g)' % Color.RgbToGreyscale(1, 0.8, 0)
    '(0.6, 0.6, 0.6)'
    '''

    v = (r + g + b) / 3
    return (v, v, v)


def rgb_to_ryb(hue):

    '''\
    Maps a hue on the RGB color wheel to Itten's RYB wheel.

    Parameters:
      :hue:
        The hue on the RGB color wheel [0...360]

    Returns:
      An approximation of the corresponding hue on Itten's RYB wheel.

    >>> Color.RgbToRyb(15)
    26.0
    '''

    try:
        hue = float(hue)
    except ValueError:
        raise TypeError('cannot convert hue to a float: {}'.format(hue))

    d = hue % 15
    i = int(hue / 15)
    x0 = RYB_WHEEL[i]
    x1 = RYB_WHEEL[i + 1]
    return x0 + (x1 - x0) * d / 15


def ryb_to_rgb(hue):

    '''\
    Maps a hue on Itten's RYB color wheel to the standard RGB wheel.

    Parameters:
      :hue:
        The hue on Itten's RYB color wheel [0...360]

    Returns:
      An approximation of the corresponding hue on the standard RGB wheel.

    >>> Color.RybToRgb(15)
    8.0
    '''

    try:
        hue = float(hue)
    except ValueError:
        raise TypeError('cannot convert hue to a float: {}'.format(hue))

    d = hue % 15
    i = int(hue / 15)
    x0 = RGB_WHEEL[i]
    x1 = RGB_WHEEL[i + 1]
    return x0 + (x1 - x0) * d / 15


def websafe_dither(color):

    '''\
    Return the two websafe colors nearest to this one.

    Returns:
      A tuple of two grapefruit.Color instances which are the two
      web safe colors closest this one.

    >>> c = Color.NewFromRgb(1.0, 0.45, 0.0)
    >>> c1, c2 = c.WebSafeDither()
    >>> str(c1)
    '(1, 0.4, 0, 1)'
    >>> str(c2)
    '(1, 0.6, 0, 1)'
    '''

    return (
        Color(rgb_to_websafe(*color.rgb), color.a, wref=color.wref),
        Color(rgb_to_websafe(*color.rgb, alt=True), color.a, wref=color.wref),
    )


def gradient(c1, c2, steps=100):

    '''\
    Create a list with the gradient colors between this and the other color.

    Parameters:
      :target:
        The grapefruit.Color at the other end of the gradient.
      :steps:
        The number of gradients steps to create.


    Returns:
      A list of grapefruit.Color instances.

    >>> c1 = Color.NewFromRgb(1.0, 0.0, 0.0, alpha=1)
    >>> c2 = Color.NewFromRgb(0.0, 1.0, 0.0, alpha=0)
    >>> c1.Gradient(c2, 3)
    [(0.75, 0.25, 0.0, 0.75), (0.5, 0.5, 0.0, 0.5), (0.25, 0.75, 0.0, 0.25)]
    '''

    gradient = []
    rgba1 = c1.rgb + (c1.a,)
    rgba2 = c2.rgb + (c2.a,)

    steps += 1
    for n in range(1, steps):
        d = n / steps
        r = (rgba1[0] * (1 - d)) + (rgba2[0] * d)
        g = (rgba1[1] * (1 - d)) + (rgba2[1] * d)
        b = (rgba1[2] * (1 - d)) + (rgba2[2] * d)
        a = (rgba1[3] * (1 - d)) + (rgba2[3] * d)

        gradient.append(Color((r, g, b), a, wref=c1.wref))
    return gradient


def complement(color, mode='ryb'):

    '''\
    Create a new instance which is the complementary color of this one.

    Parameters:
      :mode:
        Select which color wheel to use for the generation (ryb/rgb).


    Returns:
      A grapefruit.Color instance.

    >>> Color.NewFromHsl(30, 1, 0.5).ComplementaryColor(mode='rgb')
    (0.0, 0.5, 1.0, 1.0)
    >>> Color.NewFromHsl(30, 1, 0.5).ComplementaryColor(mode='rgb').hsl
    (210, 1, 0.5)
    '''

    h, s, l = rgb_to_hsl(color.rgb)

    if mode == 'ryb':
        h = rgb_to_ryb(h)
    h = (h + 180) % 360
    if mode == 'ryb':
        h = ryb_to_rgb(h)

    return Color((h, s, l), color.a, mode='hsl', wref=color.wref)


def monochrome_scheme(color):

    '''\
    Return 4 colors in the same hue with varying saturation/lightness.

    Returns:
      A tuple of 4 grapefruit.Color in the same hue as this one,
      with varying saturation/lightness.

    >>> c = Color.NewFromHsl(30, 0.5, 0.5)
    >>> ['(%g, %g, %g)' % clr.hsl for clr in c.MonochromeScheme()]
    ['(30, 0.2, 0.8)', '(30, 0.5, 0.3)', '(30, 0.2, 0.6)', '(30, 0.5, 0.8)']
    '''

    def _wrap(x, minimum, threshold, extra):
        if (x - minimum) < threshold:
            return x + extra
        else:
            return x - minimum

    h, s, l = rgb_to_hsl(color.rgb)

    s1 = _wrap(s, 0.3, 0.1, 0.3)
    l1 = _wrap(l, 0.5, 0.2, 0.3)

    s2 = s
    l2 = _wrap(l, 0.2, 0.2, 0.6)

    s3 = s1
    l3 = max(0.2, l + ((1 - l) * 0.2))

    s4 = s
    l4 = _wrap(l, 0.5, 0.2, 0.3)

    return (
        Color((h, s1,  l1), color.a, mode='hsl', wref=color.wref),
        Color((h, s2,  l2), color.a, mode='hsl', wref=color.wref),
        Color((h, s3,  l3), color.a, mode='hsl', wref=color.wref),
        Color((h, s4,  l4), color.a, mode='hsl', wref=color.wref),
    )


def triadic_scheme(color, angle=120, mode='ryb'):

    '''\
    Return two colors forming a triad or a split complementary with this one.

    Parameters:
      :angle:
        The angle between the hues of the created colors.
        The default value makes a triad.
      :mode:
        Select which color wheel to use for the generation (ryb/rgb).

    Returns:
      A tuple of two grapefruit.Color forming a color triad with
      this one or a split complementary.

    >>> c1 = Color.NewFromHsl(30, 1, 0.5)

    >>> c2, c3 = c1.TriadicScheme(mode='rgb')
    >>> c2.hsl
    (150.0, 1, 0.5)
    >>> c3.hsl
    (270.0, 1, 0.5)

    >>> c2, c3 = c1.TriadicScheme(angle=40, mode='rgb')
    >>> c2.hsl
    (190.0, 1, 0.5)
    >>> c3.hsl
    (230.0, 1, 0.5)
    '''

    h, s, l = rgb_to_hsl(color.rgb)
    angle = min(angle, 120) / 2.0

    if mode == 'ryb':
        h = ryb_to_rgb(h)
    h += 180
    h1 = (h - angle) % 360
    h2 = (h + angle) % 360
    if mode == 'ryb':
        h1 = ryb_to_rgb(h1)
        h2 = ryb_to_rgb(h2)

    return (
        Color((h1, s,  l), color.a, mode='hsl', wref=color.wref),
        Color((h2, s,  l), color.a, mode='hsl', wref=color.wref),
    )


def tetradic_scheme(color, angle=30, mode='ryb'):

    '''\
    Return three colors froming a tetrad with this one.

    Parameters:
      :angle:
        The angle to substract from the adjacent colors hues [-90...90].
        You can use an angle of zero to generate a square tetrad.
      :mode:
        Select which color wheel to use for the generation (ryb/rgb).

    Returns:
      A tuple of three grapefruit.Color forming a color tetrad with
      this one.

    >>> col = Color.NewFromHsl(30, 1, 0.5)
    >>> [c.hsl for c in col.TetradicScheme(mode='rgb', angle=30)]
    [(90, 1, 0.5), (210, 1, 0.5), (270, 1, 0.5)]
    '''

    h, s, l = rgb_to_hsl(color.rgb)

    if mode == 'ryb':
        h = rgb_to_ryb(h)
    h1 = (h + 90 - angle) % 360
    h2 = (h + 180) % 360
    h3 = (h + 270 - angle) % 360
    if mode == 'ryb':
        h1 = ryb_to_rgb(h1)
        h2 = ryb_to_rgb(h2)
        h3 = ryb_to_rgb(h3)

    return (
        Color((h1, s,  l), color.a, mode='hsl', wref=color.wref),
        Color((h2, s,  l), color.a, mode='hsl', wref=color.wref),
        Color((h3, s,  l), color.a, mode='hsl', wref=color.wref),
    )


def analogous_scheme(color, angle=30, mode='ryb'):

    '''\
    Return two colors analogous to this one.

    Args:
      :angle:
        The angle between the hues of the created colors and this one.
      :mode:
        Select which color wheel to use for the generation (ryb/rgb).

    Returns:
      A tuple of grapefruit.Colors analogous to this one.

    >>> c1 = Color.NewFromHsl(30, 1, 0.5)

    >>> c2, c3 = c1.AnalogousScheme(angle=60, mode='rgb')
    >>> c2.hsl
    (330, 1, 0.5)
    >>> c3.hsl
    (90, 1, 0.5)

    >>> c2, c3 = c1.AnalogousScheme(angle=10, mode='rgb')
    >>> c2.hsl
    (20, 1, 0.5)
    >>> c3.hsl
    (40, 1, 0.5)
    '''

    h, s, l = color.hsl

    if mode == 'ryb':
        h = rgb_to_ryb(h)
    h += 360
    h1 = (h - angle) % 360
    h2 = (h + angle) % 360

    if mode == 'ryb':
        h1 = ryb_to_rgb(h1)
        h2 = ryb_to_rgb(h2)

    return (
        Color((h1, s,  l), color.a, mode='hsl', wref=color.wref),
        Color((h2, s,  l), color.a, mode='hsl', wref=color.wref),
    )


def alpha_blend(c1, c2):

    '''\
    Alpha-blend this color on the other one.

    Args:
      :other:
        The grapefruit.Color to alpha-blend with this one.

    Returns:
      A grapefruit.Color instance which is the result of alpha-blending
      this color on the other one.

    >>> c1 = Color.NewFromRgb(1, 0.5, 0, 0.2)
    >>> c2 = Color.NewFromRgb(1, 1, 1, 0.8)
    >>> c3 = c1.AlphaBlend(c2)
    >>> str(c3)
    '(1, 0.875, 0.75, 0.84)'
    '''

    # get final alpha channel
    fa = c1.a + c2.a - (c1.a * c2.a)

    # get percentage of source alpha compared to final alpha
    if fa == 0:
        sa = 0
    else:
        sa = min(1, c1.a / c2.a)

    # destination percentage is just the additive inverse
    da = 1 - sa

    sr, sg, sb = [v * sa for v in c1.rgb]
    dr, dg, db = [v * da for v in c2.rgb]

    return Color((sr + dr, sg + dg, sb + db), fa)


def blend(c1, c2, percent=0.5):

    '''Blend this color with the other one.

    Args:
      :other:
        the grapefruit.Color to blend with this one.

    Returns:
      A grapefruit.Color instance which is the result of blending
      this color on the other one.

    >>> c1 = Color.NewFromRgb(1, 0.5, 0, 0.2)
    >>> c2 = Color.NewFromRgb(1, 1, 1, 0.6)
    >>> c3 = c1.Blend(c2)
    >>> str(c3)
    '(1, 0.75, 0.5, 0.4)'
    '''

    dest = 1 - percent
    rgb = tuple(((u * percent) + (v * dest) for u, v in zip(c1.rgb, c2.rgb)))
    a = (c1.a * percent) + (c2.a * dest)
    return Color(rgb, a)


def _test():
    import importlib
    import doctest
    importlib.reload(doctest)
    doctest.testmod()


if __name__=='__main__':
    _test()
