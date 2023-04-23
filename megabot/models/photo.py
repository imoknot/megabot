from typing import Any, ForwardRef

from pydantic import FilePath

from .base import ExcludeNone
from .file import InputFile
from .keyboards import ForceReply, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove


class SendPhoto(ExcludeNone):
    chat_id: int | str
    message_thread_id: int | None = None
    photo: str | None = None
    caption: str | None = (None,)
    parse_mode: str | None = (None,)
    caption_entities: list | None = (None,)
    has_spoiler: bool | None = (None,)
    disable_notification: bool | None = (None,)
    protect_content: bool | None = (None,)
    reply_to_message_id: int | None = (None,)
    allow_sending_without_reply: bool | None = (None,)
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
