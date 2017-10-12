import time

from . import logger
from .utils import progress


class WaitFor:

    EXPONENTIAL_BACKOFF_FACTOR = 1.618

    @classmethod
    def function_to_return_value(cls, func, *args, value=None, timeout_seconds=60):
        logger.debug(f"Waiting for {func.__name__}")
        timeout = time.time() + timeout_seconds
        wait = 1.0
        while time.time() < timeout:
            retval = func(*args)
            if retval == value:
                return retval
            logger.debug(f"Sleeping for {wait}")
            progress(".")
            time.sleep(wait)
            wait = min(60.0, wait * cls.EXPONENTIAL_BACKOFF_FACTOR)
        else:
            raise RuntimeError(f"Function {func.__name__} did not return {value} value within {timeout_seconds} seconds")


    @classmethod
    def function_to_return_a_value_other_than(cls, func, *args, other_than_value=None, timeout_seconds=60):
        logger.debug(f"Waiting for {func.__name__}")
        timeout = time.time() + timeout_seconds
        wait = 1.0
        while time.time() < timeout:
            retval = func(*args)
            if not retval == other_than_value:
                return retval
            logger.debug(f"Sleeping for {wait}")
            progress(".")
            time.sleep(wait)
            wait = min(60.0, wait * cls.EXPONENTIAL_BACKOFF_FACTOR)
        else:
            raise RuntimeError(f"Function {func.__name__} did not return a non-{other_than_value} value " +
                               f"within {timeout_seconds} seconds")
