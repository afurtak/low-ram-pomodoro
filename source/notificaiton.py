from enum import Enum
from notifypy import Notify


class NotificationType(Enum):
    FOCUS_TIME_END = ("Time to break", "You've just completed another focus sesssion")
    BREAK_END = ("Time to focus", "")


def notify_break_end():
    _send_notification(NotificationType.BREAK_END)


def notify_focus_time_end():
    _send_notification(NotificationType.FOCUS_TIME_END)


def _send_notification(type: NotificationType):
    title, message = type.value
    _build_simple_notification(title=title, message=message).send()


def _build_simple_notification(title: str, message: str):
    notification = Notify()
    notification.title = title
    notification.message = message
    return notification
