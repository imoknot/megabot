from typing import ForwardRef, Any
from pydantic import FilePath
from .base import ExcludeNone
from .media import PhotoSize, Animation


class InputFile(FilePath):
    pass
    # title: str
    # description: str
    # photo: list[PhotoSize]
    # text: str | None = None
    # text_entities: list[MessageEntity] | None = None
    # animation: Animation | None = None
