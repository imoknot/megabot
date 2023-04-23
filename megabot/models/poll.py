from typing import ForwardRef

from .base import ExcludeNone

MessageEntity = ForwardRef('MessageEntity')


class PollOption(ExcludeNone):
    text: str
    voter_count: int


class Poll(ExcludeNone):
    id: int
    question: str
    options: list[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str  # “regular” or “quiz”
    allows_multiple_answers: bool
    correct_option_id: int | None = None
    explanation: str | None = None
    explanation_entities: list[MessageEntity] | None = None
    open_period: int | None = None
    close_date: int | None = None
