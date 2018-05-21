from datetime import datetime
import sys


class Progress:

    start_time = datetime.now()
    cursor_column = 0

    @classmethod
    def report(cls, message):
        if not message == "":
            sys.stdout.write(cls._elapsed_time() + " " + message)
            if not message.endswith("\n"):
                sys.stdout.write("\n")
            sys.stdout.flush()

    @classmethod
    def _elapsed_time(cls):
        elapsed_delta = datetime.now() - cls.start_time
        return cls._duration_h_mm_ss(elapsed_delta.seconds)

    @staticmethod
    def _duration_h_mm_ss(duration_secs):
        m, s = divmod(duration_secs, 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d" % (h, m, s)
