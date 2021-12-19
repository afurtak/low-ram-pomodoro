import time


def count_down(minutes=0, seconds=0, print_clock=None):
    while minutes > 0 or (minutes == 0 and seconds >= 0):
        if print_clock is not None:
            print_clock(minutes, seconds)

        seconds -= 1
        if seconds < 0:
            minutes -= 1
            seconds = 59
        time.sleep(1)
