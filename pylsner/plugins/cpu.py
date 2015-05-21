import psutil

from pylsner.plugin import Metric


class CPU(Metric):

    def setup(self, core=1):
        if self.unit == 'overall':
            self.per_core = False
        elif self.unit == 'per_core':
            self.per_core = True
        self.core = core
        self.raw_max = 100

    def refresh(self, cnt, value):
        self.raw_value = self.stored_source(cnt)

    def source(self, *args):
        if self.per_core:
            return psutil.cpu_percent(0, self.per_core)[self.core]
        else:
            return psutil.cpu_percent(0, self.per_core)

Plugin = CPU
