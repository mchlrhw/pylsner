import calendar

from datetime import datetime

from pylsner.plugin import Metric


class Time(Metric):

    def setup(self, **kwargs):
        self._set_raw_val = getattr(self, '_set_{}'.format(self.unit))

        now = datetime.now()
        if self.unit in ['seconds', 'seconds_tick', 'minutes']:
            self.raw_max = 60
        elif self.unit == 'hours':
            self.raw_max = 12
        elif self.unit == 'day':
            self.raw_max = 24
        elif self.unit == 'week':
            self.raw_max = 7
        elif self.unit == 'month':
            self.raw_max = calendar.monthrange(now.year, now.month)[1]
        elif self.unit == 'year':
            if not calendar.isleap(now.year):
                self.raw_max = 365
            else:
                self.raw_max = 366
        elif self.unit == 'century':
            self.raw_max = 100

    def _set_seconds(self, now):
        self.raw_value = now.second + (now.microsecond / 1000000)

    def _set_seconds_tick(self, now):
        self.raw_value = now.second

    def _set_minutes(self, now):
        self.raw_value = (
            now.minute
            + now.second / 60
            + (now.microsecond / 60000000)
        )

    def _set_hours(self, now):
        self.raw_value = (
            (now.hour % 12)
            + now.minute / 60
            + now.second / 3600
        )

    def _set_day(self, now):
        self.raw_value = (
            now.hour
            + now.minute / 60
            + now.second / 3600
        )

    def _set_week(self, now):
        self.raw_value = (
            now.weekday()
            + now.hour / 24
            + now.minute / 1440
        )

    def _set_month(self, now):
        self.raw_max = calendar.monthrange(now.year, now.month)[1]
        self.raw_value = (
            (now.day - 1)
            + now.hour / 24
            + now.minute / 1440
        )

    def _set_year(self, now):
        if not calendar.isleap(now.year):
            self.raw_max = 365
        else:
            self.raw_max = 366
        self.raw_value = (
            (now.timetuple().tm_yday - 1)
            + now.hour / 24
            + now.minute / 1440
        )

    def _set_century(self, now):
        self.raw_value = (
            now.year % 100
            + ((now.timetuple().tm_yday - 1) / 365)
        )

    def source(self, *args):
        return datetime.now()

    def refresh(self, cnt, value):
        now = self.stored_source(cnt)
        self._set_raw_val(now)


Plugin = Time
