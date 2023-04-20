from typing import ForwardRef

from .base import ExcludeNone
from .media import Animation, PhotoSize

MessageEntity = ForwardRef('MessageEntity')



class Game(ExcludeNone):
    title: str
    description: str
    photo: list[PhotoSize]
    text: str | None = None
    text_entities: list[MessageEntity] | None = None
    animation: Animation | None = None
