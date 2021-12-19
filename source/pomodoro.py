import time

from timer import count_down
from display import print_clock
from notificaiton import notify_break_end, notify_focus_time_end


class PomodoroTimer:
    def __init__(
        self,
        focus_time: int,
        break_time: int,
        number_of_sessions: int,
    ) -> None:
        self.focus_time = focus_time
        self.break_time = break_time
        self.number_of_sessions = number_of_sessions

    def start(self, wait_after_last_session_in_seconds=0):
        for i in range(self.number_of_sessions):
            self.notify_break_time_end()
            self.start_focus_time()
            self.notify_focus_time_end()
            self.start_break_time()
        self.notify_focus_time_end()
        time.sleep(wait_after_last_session_in_seconds)

    def start_focus_time(self):
        count_down(
            minutes=self.focus_time,
            print_clock=print_clock,
        )

    def start_break_time(self):
        count_down(
            minutes=self.break_time,
            print_clock=print_clock,
        )

    def notify_break_time_end(self):
        notify_break_end()

    def notify_focus_time_end(self):
        notify_focus_time_end()
