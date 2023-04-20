import requests

from .models import BotCommand, SetMyCommands
from .sender import Base


class Commands(Base):
    async def set_my_commands(self, token: str, commands: list[BotCommand]):
        set_command = SetMyCommands(commands=commands).dict()
        request_url = self.request_url(token, 'setMyCommands')
        response = requests.post(url=request_url, json=set_command)
        return response

