from datetime import datetime

from pylsner.plugin import Metric


class Plugin(Metric):

    def __init__(self, plugin='time', unit='seconds', refresh_rate=1):
        super().__init__(plugin, unit, refresh_rate)

        self.set_value = getattr(self, '_set_{}'.format(unit))

        self._val_min = 0
        if self.unit in ['seconds', 'seconds_tick', 'minutes']:
            self._val_max = 60
        elif self.unit == 'hours':
            self._val_max = 12
        elif self.unit == 'hours_24':
            self._val_max = 24

        self._val_range = self._val_max - self._val_min
        self._val_curr = self._val_min
        self._val_frac = (self._val_curr - self._val_min) / self._val_range

    def _set_seconds(self, now):
        self._val_curr = now.second + (now.microsecond / 1000000)

    def _set_seconds_tick(self, now):
        self._val_curr = now.second

    def _set_minutes(self, now):
        self._val_curr = (
            now.minute
            + now.second / 60
            + (now.microsecond / 60000000)
        )

    def _set_hours(self, now):
        self._val_curr = (
            (now.hour % 12)
            + now.minute / 60
            + now.second / 3600
        )

    def _set_hours_24(self, now):
        self._val_curr = (
            now.hour
            + now.minute / 60
            + now.second / 3600
        )

    def refresh(self):
        now = datetime.now()
        self.set_value(now)
        self._val_frac = (self._val_curr - self._val_min) / self._val_range
