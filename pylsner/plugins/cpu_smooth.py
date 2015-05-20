import psutil

from pylsner.plugin import Metric, MetricStore


class Plugin(Metric):

    def __init__(self, unit='overall', refresh_rate=100, core=1):
        self._refresh_rate = refresh_rate
        super().__init__(unit, self._refresh_rate)

        if self.unit == 'overall':
            per_core = False
            self.store = CPUStore(per_cpu)
        elif self.unit == 'per_core':
            per_core = True
            self.store = CPUStore(per_core, core)

        self.set_limits(0, 100)
        self._curr = self._min
        self._intervals = 10
        self._locked = False

    def refresh(self, parent, refresh_cnt):
        if self._locked:
            if self._countdown > 2:
                self._curr += self._diff / self.refresh_rate
                self._countdown -= 1
            else:
                self._curr = self._new
                self.refresh_rate = self._refresh_rate
                self._locked = False
        else:
            self._new = self.store.get_value(refresh_cnt)
            self._diff = self._new - self._curr
            if self._diff:
                self.refresh_rate = self._intervals
                self._countdown = self.refresh_rate
                self._curr += self._diff / self.refresh_rate
                self._locked = True
            else:
                self._curr = self._new


class CPUStore(MetricStore):

    _shared_state = {}

    def __init__(self, per_core=False, core=1):
        super().__init__()
        self.per_core = per_core
        self.core = core - 1

    def refresh(self):
        if self.per_core:
            self.value = psutil.cpu_percent(0, self.per_core)[self.core]
        else:
            self.value = psutil.cpu_percent(0, self.per_core)
