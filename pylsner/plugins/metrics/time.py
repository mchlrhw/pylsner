from datetime import datetime

from pylsner.plugin import Metric


class Plugin(Metric):

    def __init__(self, unit='seconds', refresh_rate=1, **kwargs):
        super().__init__(unit, refresh_rate)

        self._set_value = getattr(self, '_set_{}'.format(unit))

        self._min = 0
        if self.unit in ['seconds', 'seconds_tick', 'minutes']:
            self._max = 60
        elif self.unit == 'hours':
            self._max = 12
        elif self.unit == 'hours_24':
            self._max = 24

        self.set_limits()
        self._curr = self._min

    def _set_seconds(self, now):
        self._curr = now.second + (now.microsecond / 1000000)

    def _set_seconds_tick(self, now):
        self._curr = now.second

    def _set_minutes(self, now):
        self._curr = (
            now.minute
            + now.second / 60
            + (now.microsecond / 60000000)
        )

    def _set_hours(self, now):
        self._curr = (
            (now.hour % 12)
            + now.minute / 60
            + now.second / 3600
        )

    def _set_hours_24(self, now):
        self._curr = (
            now.hour
            + now.minute / 60
            + now.second / 3600
        )

    def refresh(self, parent):
        now = datetime.now()
        self._set_value(now)
