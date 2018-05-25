import time

from . import logger
from .utils import Progress


class TimedOut(RuntimeError):
    pass


class WaitFor:

    EXPONENTIAL_BACKOFF_FACTOR = 1.618

    def __init__(self, func, *args):
        self.func = func
        self.func_args = args
        self.start_time = None
        self.backoff_seconds = 1.0
        logger.debug(f"WaitFor {self.func.__name__}")

    def to_return_value(self, value=None, timeout_seconds=None):
        self.start_time = time.time()
        timeout_at = self.start_time + timeout_seconds if timeout_seconds else None

        while True:
            retval = self.func(*self.func_args)
            Progress.report(f"  {self.func.__name__} returned {retval}")
            if retval == value:
                return retval
            if timeout_at and time.time() > timeout_at:
                raise TimedOut(f"Function {self.func.__name__} did not return value {value} " +
                               f" within {timeout_seconds} seconds")
            self._sleep_until_next_check_time()

    def to_return_a_value_other_than(self, other_than_value=None, timeout_seconds=None):
        self.start_time = time.time()
        timeout_at = self.start_time + timeout_seconds if timeout_seconds else None

        while True:
            retval = self.func(*self.func_args)
            Progress.report(f"  {self.func.__name__} returned {retval}")
            if not retval == other_than_value:
                return retval
            if timeout_at and time.time() > timeout_at:
                raise TimedOut(f"Function {self.func.__name__} did not return a non-{other_than_value} value " +
                               f"within {timeout_seconds} seconds")
            self._sleep_until_next_check_time()

    def _sleep_until_next_check_time(self):
        time.sleep(self.backoff_seconds)
        self.backoff_seconds = min(60.0, self.backoff_seconds * self.EXPONENTIAL_BACKOFF_FACTOR)
