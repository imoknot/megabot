import requests

from .models import BotCommand
from .sender import Base


class CommandsService(Base):
    async def set_my_commands(self, token: str, commands: list[BotCommand]):
        message = AnswerCallbackQuery(
            callback_query_id=callback_query_id, text=text, show_alert=show_alert, url=url, cache_time=cache_time
        ).dict()
        request_url = self.request_url(token, 'answerCallbackQuery')
        response = requests.post(url=request_url, json=message)
        return response
