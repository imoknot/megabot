from pydantic import Field

from .base import ExcludeNone
from .users import User
from .message import Message


class CallbackQuery(ExcludeNone):
    id: str
    from_user: User = Field(None, alias='from')
    message: Message | None = None
    inline_message_id: str | None = None
    chat_instance: str | None = None
    data: str | dict | None = None
    game_short_name: str | None = None


class AnswerCallbackQuery(ExcludeNone):
    callback_query_id: str
    text: str | None = None
    show_alert: bool | None = None
    url: str | None = None
    cache_time: str | None = None

