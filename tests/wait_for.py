import time

from . import logger
from .utils import progress


class WaitFor:

    EXPONENTIAL_BACKOFF_FACTOR = 1.618
    DURATION_DISPLAY_WIDTH = 7  # "0:00:00"
    ASCII_MOVE_CURSOR_LEFT = "\x1b[{count}D"
    ASCII_MOVE_CURSOR_RIGHT = "\x1b[{count}C"

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
                progress(self.ASCII_MOVE_CURSOR_RIGHT.format(count=self.DURATION_DISPLAY_WIDTH))
                return retval
            progress(".")
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
                progress(self.ASCII_MOVE_CURSOR_RIGHT.format(count=self.DURATION_DISPLAY_WIDTH))
                return retval
            progress(".")
            self._display_duration_until_next_check_time()
        else:
            raise RuntimeError(f"Function {self.func.__name__} did not return a non-{other_than_value} value " +
                               f"within {timeout_seconds} seconds")

    def _display_duration_until_next_check_time(self):
        next_check_at = time.time() + self.backoff_seconds
        while time.time() < next_check_at:
            time.sleep(1)
            self._display_duration()
        self.backoff_seconds = min(60.0, self.backoff_seconds * self.EXPONENTIAL_BACKOFF_FACTOR)

    def _display_duration(self):
        duration = time.time() - self.start_time
        message = self._duration_h_mm_ss(duration)
        message += self.ASCII_MOVE_CURSOR_LEFT.format(count=self.DURATION_DISPLAY_WIDTH)
        progress(message)

    @staticmethod
    def _duration_h_mm_ss(duration_secs):
        m, s = divmod(duration_secs, 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d" % (h, m, s)
