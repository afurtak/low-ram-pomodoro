import time
from enum import Enum


class SessionType(Enum):
    FOCUS = (1, 0)
    BREAK = (0, 30)


def start_session(session_type: SessionType, print_clock=None):
    minutes, seconds = session_type.value

    while minutes > 0 or (minutes == 0 and seconds >= 0):
        if print_clock is not None:
            print_clock(minutes, seconds)

        seconds -= 1
        if seconds < 0:
            minutes -= 1
            seconds = 59
        time.sleep(1)
