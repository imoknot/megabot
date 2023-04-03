from .base import ExcludeNone, File


class ForumTopicCreated(ExcludeNone):
    name: str
    icon_color: int
    icon_custom_emoji_id: str | None = None


class ForumTopicEdited(ExcludeNone):
    name: str | None = None
    icon_custom_emoji_id: str | None = None


class ForumTopicClosed(ExcludeNone):
    pass


class ForumTopicReopened(ExcludeNone):
    pass


class GeneralForumTopicHidden(ExcludeNone):
    pass


class GeneralForumTopicUnhidden(ExcludeNone):
    pass
