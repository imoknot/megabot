
from .base import ExcludeNone
from .users import User


class WriteAccessAllowed(ExcludeNone):
    start_date: int


class VideoChatScheduled(ExcludeNone):
    start_date: int


class VideoChatStarted(ExcludeNone):
    pass


class VideoChatEnded(ExcludeNone):
    duration: int


class VideoChatParticipantsInvited(ExcludeNone):
    users: list[User]
