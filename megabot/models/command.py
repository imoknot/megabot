from typing import List

from .base import ExcludeNone


class BotCommand(ExcludeNone):
    command: str
    description: str


class SetMyCommands(ExcludeNone):
    commands: List[BotCommand]
    # scope: BotCommandScope | None = None
    language_code: str | None = None

