from typing import Any, ForwardRef

from pydantic import FilePath

from .base import ExcludeNone
from .media import Animation, PhotoSize



class InputFile(FilePath):
    pass
    # title: str
    # description: str
    # photo: list[PhotoSize]
    # text: str | None = None
    # text_entities: list[MessageEntity] | None = None
    # animation: Animation | None = None
