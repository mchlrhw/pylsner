from datetime import datetime

from pylsner.plugin import Metric

class Plugin(Metric):

    def __init__(self, plugin='time', unit='seconds', refresh_rate=1):
        super().__init__(plugin, unit, refresh_rate)

        self._val_min = 0
        if self.unit in ['seconds', 'seconds_tick']:
            self._val_max = 60
        elif self.unit == 'minutes':
            self._val_max = 60
        elif self.unit == 'hours':
            self._val_max = 12
        elif self.unit == 'hours_24':
            self._val_max = 24

        self._val_range = self._val_max - self._val_min
        self._val_curr = self._val_min
        self._val_frac = (self._val_curr - self._val_min) / self._val_range

    def refresh(self):
        now = datetime.now()
        if self.unit == 'seconds':
            self._val_curr = now.second + (now.microsecond / 1000000)
        elif self.unit == 'seconds_tick':
            self._val_curr = now.second
        elif self.unit == 'minutes':
            self._val_curr = (
                now.minute
                + now.second / 60
                + (now.microsecond / 60000000)
            )
        elif self.unit == 'hours':
            self._val_curr = (
                (now.hour % 12)
                + now.minute / 60
                + now.second / 3600
            )
        elif self.unit == 'hours_24':
            self._val_curr = (
                now.hour
                + now.minute / 60
                + now.second / 3600
            )
        self._val_frac = (self._val_curr - self._val_min) / self._val_range
