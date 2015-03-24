class Metric:

    def __init__(self, unit=None, refresh_rate=None):
        self.plugin = None
        self.unit = unit
        self.refresh_rate = refresh_rate

        self._val_min = None
        self._val_max = None
        self._val_range = None
        self._val_curr = None
        self._val_frac = None

    @property
    def value(self):
        return self._val_frac

    @property
    def value_raw(self):
        return self._val_curr

    def refresh(self):
        pass


class Widget:

    def __init__(self, length=None, width=None, orientation=None, **kwargs):
        self.plugin = None
        self.length = length
        self.width = width
        self.orientation = orientation

    def redraw(self, ctx):
        pass


class Color:

    def __init__(self, value):
        self.plugin = None
        self.value = value

    def refresh(self, metric_value):
        pass
