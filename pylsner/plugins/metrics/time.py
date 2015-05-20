import calendar

from datetime import datetime

from pylsner.plugin import Metric, MetricStore


class Time(Metric):

    def __init__(self, unit='seconds'):
        super().__init__(unit)

        self.store = TimeStore()

        self._set_value = getattr(self, '_set_{}'.format(unit))

        self._min = 0
        now = datetime.now()
        if self.unit in ['seconds', 'seconds_tick', 'minutes']:
            self._max = 60
        elif self.unit == 'hours':
            self._max = 12
        elif self.unit == 'day':
            self._max = 24
        elif self.unit == 'week':
            self._max = 7
        elif self.unit == 'month':
            self._max = calendar.monthrange(now.year, now.month)[1]
        elif self.unit == 'year':
            if not calendar.isleap(now.year):
                self._max = 365
            else:
                self._max = 366
        elif self.unit == 'century':
            self._max = 100

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

    def _set_day(self, now):
        self._curr = (
            now.hour
            + now.minute / 60
            + now.second / 3600
        )

    def _set_week(self, now):
        self._curr = (
            now.weekday()
            + now.hour / 24
            + now.minute / 1440
        )

    def _set_month(self, now):
        self._curr = (
            (now.day - 1)
            + now.hour / 24
            + now.minute / 1440
        )

    def _set_year(self, now):
        self._curr = (
            (now.timetuple().tm_yday - 1)
            + now.hour / 24
            + now.minute / 1440
        )

    def _set_century(self, now):
        self._curr = (
            now.year % 100
            + ((now.timetuple().tm_yday - 1) / 365)
        )

    def refresh(self, value):
        self._set_value(self.store.now)


class TimeStore(MetricStore):

    _shared_state = {}

    def refresh(self, cnt):
        self.now = datetime.now()


Plugin = Time
