from threading import Timer
from typing import Any

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def setattrs(cls: object, **kwargs: Any):
  for attr, val in kwargs.items():
    setattr(cls, attr, val)
