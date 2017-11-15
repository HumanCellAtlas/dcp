from datetime import datetime
import sys


class Progress:

    ANSI_MOVE_CURSOR_RIGHT = "\x1b[{count}C"

    start_time = datetime.now()
    cursor_column = 0

    @classmethod
    def report(cls, message):
        if cls.cursor_column == 0:
            cls.output_and_record_new_cursor_column(cls.elapsed_time() + " ")
        else:
            cls.jump_to_start_of_line_print_time_jump_back()
        cls.output_and_record_new_cursor_column(message)
        sys.stdout.flush()

    @classmethod
    def jump_to_start_of_line_print_time_jump_back(cls):
        sys.stdout.write(f"\r{cls.elapsed_time()}\r" + cls.ANSI_MOVE_CURSOR_RIGHT.format(count=cls.cursor_column))

    @classmethod
    def elapsed_time(cls):
        elapsed_delta = datetime.now() - cls.start_time
        return cls._duration_h_mm_ss(elapsed_delta.seconds)

    @classmethod
    def output_and_record_new_cursor_column(cls, message):
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
