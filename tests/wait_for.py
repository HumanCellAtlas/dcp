import time

from . import logger
from .utils import Progress


class WaitFor:

    EXPONENTIAL_BACKOFF_FACTOR = 1.618

    def __init__(self, func, *args):
        self.func = func
        self.func_args = args
        self.start_time = None
        self.backoff_seconds = 1.0
        logger.debug(f"WaitFor {self.func.__name__}")

    def to_return_value(self, value=None, timeout_seconds=60):
        self.start_time = time.time()
        timeout_at = self.start_time + timeout_seconds

        while time.time() < timeout_at:
            retval = self.func(*self.func_args)
            if retval == value:
                return retval
            Progress.report(".")
            self._display_duration_until_next_check_time()
        else:
            raise RuntimeError(f"Function {self.func.__name__} did not return value {value} " +
                               f" within {timeout_seconds} seconds")

    def to_return_a_value_other_than(self, other_than_value=None, timeout_seconds=60):
        self.start_time = time.time()
        timeout_at = self.start_time + timeout_seconds

        while time.time() < timeout_at:
            retval = self.func(*self.func_args)
            if not retval == other_than_value:
                return retval
            Progress.report(".")
            self._display_duration_until_next_check_time()
        else:
            raise RuntimeError(f"Function {self.func.__name__} did not return a non-{other_than_value} value " +
                               f"within {timeout_seconds} seconds")

    def _display_duration_until_next_check_time(self):
        next_check_at = time.time() + self.backoff_seconds
        while time.time() < next_check_at:
            time.sleep(1)
            Progress.report("")  # update clock
        self.backoff_seconds = min(60.0, self.backoff_seconds * self.EXPONENTIAL_BACKOFF_FACTOR)
