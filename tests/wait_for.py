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

    def to_return_any_value(self, timeout_seconds=None):
        def assert_non_empty_value(returned_value): return returned_value

        def handle_timeout(returned_value):
            raise TimedOut(f"Function {self.func.__name__} only returned a non-empty value " +
                           f"{returned_value} within {timeout_seconds} seconds")

        self._do_expect_function_to_return(assert_non_empty_value, handle_timeout)

    def _do_expect_function_to_return(self, assertion_on_returned_value, timeout_handler,
                                      timeout_seconds=None):
        self.start_time = time.time()
        timeout_at = self.start_time + timeout_seconds if timeout_seconds else None

        while True:
            returned_value = self.func(*self.func_args)
            Progress.report(f"  {self.func.__name__} returned {returned_value}")
            if assertion_on_returned_value(returned_value):
                return returned_value
            if timeout_at and time.time() > timeout_at:
                timeout_handler(returned_value)
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
