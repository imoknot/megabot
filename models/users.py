from .base import ExcludeNone


class User(ExcludeNone):
    id: int
    is_bot: bool
    first_name: str
    last_name: str | None = None
    username: str | None = None
    language_code: str | None = None
    is_premium: bool | None = None
    added_to_attachment_menu: bool | None = None
    can_join_groups: bool | None = None
    can_read_all_group_messages: bool | None = None
    supports_inline_queries: bool | None = None


class Contact(ExcludeNone):
    phone_number: str
    first_name: str
    last_name: str | None = None
    user_id: int | None = None
    vcard: str | None = None


class UserShared(ExcludeNone):
    request_id: int
    user_id: int


class PassportFile(ExcludeNone):
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int


class EncryptedCredentials(ExcludeNone):
    data: str
    hash: str
    secret: str


class EncryptedPassportElement(ExcludeNone):
    type: str
    data: str | None = None
    phone_number: str | None = None
    email: str | None = None
    files: list[PassportFile] | None = None
    front_side: PassportFile | None = None
    reverse_side: PassportFile | None = None
    selfie: PassportFile | None = None
    translation: list[PassportFile]
    hash: str


class PassportData(ExcludeNone):
    data: list[EncryptedPassportElement]
    credentials: EncryptedCredentials


class ProximityAlertTriggered(ExcludeNone):
    traveler: User
    watcher: User
    distance: int
