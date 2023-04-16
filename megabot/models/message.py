from typing import ForwardRef

from pydantic import Field

from .base import ExcludeNone, Location, Venue
from .chats import Chat, ChatShared
from .emodj import Dice
from .forum import (
    ForumTopicClosed,
    ForumTopicCreated,
    ForumTopicEdited,
    ForumTopicReopened,
    GeneralForumTopicHidden,
    GeneralForumTopicUnhidden
)
from .game import Game
from .keyboards import ForceReply, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from .media import Animation, Audio, Document, PhotoSize, Video, VideoNote, Voice
from .payment import Invoice, SuccessfulPayment
from .poll import Poll
from .sticker import Sticker
from .users import Contact, PassportData, ProximityAlertTriggered, User, UserShared
from .video import (
    VideoChatEnded,
    VideoChatParticipantsInvited,
    VideoChatScheduled,
    VideoChatStarted,
    WriteAccessAllowed
)
from .web_app import WebAppData

Message = ForwardRef('Message')


class MessageAutoDeleteTimerChanged(ExcludeNone):
    message_auto_delete_time: int


class MessageEntity(ExcludeNone):
    type: str
    offset: int
    length: int
    url: str | None = None
    user: User | None = None
    language: str | None = None
    custom_emoji_id: str | None = None


class SendMessage(ExcludeNone):
    chat_id: int | str = 12345
    message_thread_id: int | None = None
    text: str = 'Hi, peoples!'
    parse_mode: str | None = None
    entities: list | None = None
    disable_web_page_preview: bool | None = None
    disable_notification: bool | None = None
    protect_content: bool | None = None
    reply_to_message_id: int | None = None
    allow_sending_without_reply: bool | None = None
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None


class Message(ExcludeNone):
    message_id: int
    message_thread_id: int | None = None
    from_user: User = Field(None, alias='from')
    sender_chat: Chat | None = None
    date: int
    chat: Chat
    forward_from: User | None = None
    forward_from_chat: Chat | None = None
    forward_from_message_id: int | None = None
    forward_signature: str | None = None
    forward_sender_name: str | None = None
    forward_date: int | None = None
    is_topic_message: bool | None = None
    is_automatic_forward: bool | None = None
    reply_to_message: Message | None = None
    via_bot: User | None = None
    edit_date: int | None = None
    has_protected_content: bool | None = None
    media_group_id: str | None = None
    author_signature: str | None = None
    text: str | None = None
    entities: list[MessageEntity] | None = None
    animation: Animation | None = None
    audio: Audio | None = None
    document: Document | None = None
    photo: list[PhotoSize] | None = None
    sticker: Sticker | None = None
    video: Video | None = None
    video_note: VideoNote | None = None
    voice: Voice | None = None
    caption: str | None = None
    caption_entities: list[MessageEntity] | None = None
    has_media_spoiler: bool | None = None
    contact: Contact | None = None
    dice: Dice | None = None
    game: Game | None = None
    poll: Poll | None = None
    venue: Venue | None = None
    location: Location | None = None
    new_chat_members: list[User] | None = None
    left_chat_member: User | None = None
    new_chat_title: str | None = None
    new_chat_photo: list[PhotoSize] | None = None
    delete_chat_photo: bool | None = None
    group_chat_created: bool | None = None
    supergroup_chat_created: bool | None = None
    channel_chat_created: bool | None = None
    message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged | None = None
    migrate_to_chat_id: int | None = None
    migrate_from_chat_id: int | None = None
    pinned_message: Message | None = None
    invoice: Invoice | None = None
    successful_payment: SuccessfulPayment | None = None
    user_shared: UserShared | None = None
    chat_shared: ChatShared | None = None
    connected_website: str | None = None
    write_access_allowed: WriteAccessAllowed | None = None
    passport_data: PassportData | None = None
    proximity_alert_triggered: ProximityAlertTriggered | None = None
    forum_topic_created: ForumTopicCreated | None = None
    forum_topic_edited: ForumTopicEdited | None = None
    forum_topic_closed: ForumTopicClosed | None = None
    forum_topic_reopened: ForumTopicReopened | None = None
    general_forum_topic_hidden: GeneralForumTopicHidden | None = None
    general_forum_topic_unhidden: GeneralForumTopicUnhidden | None = None
    video_chat_scheduled: VideoChatScheduled | None = None
    video_chat_started: VideoChatStarted | None = None
    video_chat_ended: VideoChatEnded | None = None
    video_chat_participants_invited: VideoChatParticipantsInvited | None = None
    web_app_data: WebAppData | None = None
    reply_markup: InlineKeyboardMarkup | None = None


Message.update_forward_refs()
MessageEntity.update_forward_refs()


class DeleteMessage(ExcludeNone):
    chat_id: int | str
    message_id: int


class EditMessageReplyMarkup(ExcludeNone):
    chat_id: int | str | None = None
    message_id: int | None = None
    inline_message_id: str | None = None
    reply_markup: InlineKeyboardMarkup | None = None
