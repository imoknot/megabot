from .base import ExcludeNone


class PhotoSize(ExcludeNone):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int | None = None



class Audio(ExcludeNone):
    file_id: str
    file_unique_id: str
    duration: int
    performer: str | None = None
    title: str | None = None
    file_name: str | None = None
    mime_type: str | None = None
    file_size: int | None = None
    thumbnail: PhotoSize | None = None


class Animation(ExcludeNone):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: PhotoSize | None = None
    file_name: str | None = None
    mime_type: str | None = None
    file_size: int | None = None


class Document(ExcludeNone):
    file_id: str
    file_unique_id: str
    thumbnail: PhotoSize | None = None
    file_name: str | None = None
    mime_type: str | None = None
    file_size: int | None = None


class Video(ExcludeNone):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: PhotoSize | None = None
    file_name: str | None = None
    mime_type: str | None = None
    file_size: int | None = None


class VideoNote(ExcludeNone):
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumbnail: PhotoSize | None = None
    file_size: int | None = None


class Voice(ExcludeNone):
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: str | None = None
    file_size: int | None = None
