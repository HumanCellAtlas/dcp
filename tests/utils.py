from datetime import datetime
import os
import sys


class Progress:

    ANSI_MOVE_CURSOR_RIGHT = "\x1b[{count}C"

    start_time = datetime.now()
    cursor_column = 0

    @classmethod
    def report(cls, message):
        if 'TRAVIS' in os.environ:
            cls._simple_output(message)
        else:
            if cls.cursor_column == 0:
                cls._output_and_record_new_cursor_column(cls._elapsed_time() + " ")
            else:
                cls._jump_to_start_of_line_print_time_jump_back()
            cls._output_and_record_new_cursor_column(message)

    @classmethod
    def _simple_output(cls, message):
        """
        Travis does weird things with output, so do dumb line-oriented output only.  No ANSI escape sequences.
        """
        if not message == "":
            sys.stdout.write(cls._elapsed_time() + " " + message)
            if not message.endswith("\n"):
                sys.stdout.write("\n")
            sys.stdout.flush()

    @classmethod
    def _jump_to_start_of_line_print_time_jump_back(cls):
        if sys.stdout.isatty():
            sys.stdout.write(f"\r{cls._elapsed_time()}\r" + cls.ANSI_MOVE_CURSOR_RIGHT.format(count=cls.cursor_column))

    @classmethod
    def _elapsed_time(cls):
        elapsed_delta = datetime.now() - cls.start_time
        return cls._duration_h_mm_ss(elapsed_delta.seconds)

    @classmethod
    def _output_and_record_new_cursor_column(cls, message):
        sys.stdout.write(message)
        sys.stdout.flush()
        if message.find("\n") == -1:
            cls.cursor_column += len(message)
        else:
            cls.cursor_column = len(message.split("\n")[-1])

    @staticmethod
    def _duration_h_mm_ss(duration_secs):
        m, s = divmod(duration_secs, 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d" % (h, m, s)
