import click

from pomodoro import PomodoroTimer


@click.command()
@click.option("--sessions", default=1, help="number of pomodoro sessions")
@click.option("--focus_time", default=25, help="focus time")
@click.option("--break_time", default=5, help="break time")
def run(sessions, focus_time, break_time):
    PomodoroTimer(
        focus_time=focus_time,
        break_time=break_time,
        number_of_sessions=sessions,
    ).start(
        wait_after_last_session_in_seconds=10,
    )


if __name__ == "__main__":
    run()
