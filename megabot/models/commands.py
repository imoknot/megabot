from typing import ForwardRef

from .base import ExcludeNone, Location

Message = ForwardRef('Message')


class BotCommand(ExcludeNone):
    is_anonymous: bool
    can_manage_chat: bool
