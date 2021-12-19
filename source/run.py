from timer import start_session, SessionType
from display import print_clock
from notificaiton import notify_break_end, notify_focus_time_end
import time


SESSIONS_NUMBER = 1


def run():
    for i in range(SESSIONS_NUMBER):
        notify_break_end()
        start_session(SessionType.FOCUS, print_clock)
        notify_focus_time_end()
        start_session(SessionType.BREAK, print_clock)
    time.sleep(10)


if __name__ == "__main__":
    run()
