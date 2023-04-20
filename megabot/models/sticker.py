from .base import ExcludeNone, File
from .media import PhotoSize



class MaskPosition(ExcludeNone):
    point: str
    x_shift: float
    y_shift: float
    scale: float


class Sticker(ExcludeNone):
    file_id: str
    file_unique_id: str
    type: str
    width: int
    height: int
    is_animated: bool
    is_video: bool
    thumbnail: PhotoSize | None = None
    emoji: str | None = None
    set_name: str | None = None
    premium_animation: File | None = None
    mask_position: MaskPosition | None = None
    custom_emoji_id: str | None = None
    needs_repainting: bool | None = None
    file_size: int | None = None
