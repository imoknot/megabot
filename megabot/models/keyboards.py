from typing import List, Tuple

from pydantic import Field

from .base import ExcludeNone
from .chats import ChatAdministratorRights



class WebAppInfo(ExcludeNone):
    pass


class LoginUrl(ExcludeNone):
    pass


class CallbackGame(ExcludeNone):
    pass


class InlineKeyboardButton(ExcludeNone):
    text: str
    url: str | None = None
    callback_data: str | None = None
    web_app: WebAppInfo | None = None
    login_url: LoginUrl | None = None
    switch_inline_query: str | None = None
    switch_inline_query_current_chat: str | None = None
    callback_game: CallbackGame | None = None
    pay: bool | None = None


class InlineKeyboardMarkup(ExcludeNone):
    inline_keyboard: List[List[InlineKeyboardButton] | InlineKeyboardButton]


class KeyboardButtonRequestChat(ExcludeNone):
    request_id: int
    chat_is_channel: bool = True
    chat_is_forum: bool | None = None
    chat_has_username: bool | None = None
    chat_is_created: bool | None = None
    user_administrator_rights: ChatAdministratorRights | None = None
    bot_administrator_rights: ChatAdministratorRights | None = None
    bot_is_member: bool | None = None


class KeyboardButtonRequestUser(ExcludeNone):
    request_id: int
    user_is_bot: bool | None = None
    user_is_premium: bool | None = None


class KeyboardButtonPollType(ExcludeNone):
    type: str | None = None  # quiz


class KeyboardButton(ExcludeNone):
    text: str
    request_user: KeyboardButtonRequestUser | None = None
    request_chat: KeyboardButtonRequestChat | None = None
    request_contact: bool | None = None
    request_location: bool | None = None
    request_poll: KeyboardButtonPollType | None = None
    web_app: WebAppInfo | None = None


class ReplyKeyboardMarkup(ExcludeNone):
    keyboard: List[List[KeyboardButton] | KeyboardButton]
    is_persistent: bool | None = None
    resize_keyboard: bool | None = None
    one_time_keyboard: bool | None = None
    input_field_placeholder: bool | None = None
    selective: bool | None = None


class ReplyKeyboardRemove(ExcludeNone):
    remove_keyboard: bool
    selective: bool | None = None


class ForceReply(ExcludeNone):
    pass
