from dataclasses import dataclass
from typing import NoReturn

from .models import CallbackQuery, Message


@dataclass
class Handler:
    handler: callable


class Dispatcher:
    handlers_command: dict = {}
    handlers_callback: dict = {}
    tokens: dict = {}

    @classmethod
    def register_handler_command(cls, command: str, handler: callable) -> NoReturn:
        cls.handlers_command[command] = Handler(handler)

    @classmethod
    def register_handler_callback(cls, callback_filter: dict | str, handler: callable) -> NoReturn:
        if isinstance(callback_filter, str):
            if len(callback_filter) < 1:
                raise ValueError(f'length name filter must be > 1 char')
            callback_filter = '#' + callback_filter
            if cls.handlers_callback[callback_filter]:
                raise ValueError(f'Duplicate filter!')
            cls.handlers_callback[callback_filter] = Handler(handler)
            return

        if not isinstance(callback_filter, dict):
            raise ValueError('callback_filter must be dict format: {"prefix:{"hash": object.__dict__}}')

        for key, value in callback_filter.items():
            filter_prefix = cls.handlers_callback.get(key)
            if not filter_prefix:
                cls.handlers_callback[key] = {}

            for _key, _value in value.items():
                cls.handlers_callback[key + '_schema'] = [key, *_value.keys()]
                cls.handlers_callback[key][_key] = Handler(handler)

    @classmethod
    async def message_router(cls, bot_id, data):
        async def parse_callback_query(callback_query: dict) -> NoReturn:
            callback_text = CallbackQuery(**callback_query).data
            if len(callback_text) < 2:
                return

            # text handlers
            callback_list = callback_text[1:].split(callback_text[0])
            main_key = callback_list[0]
            if len(callback_list) == 1:
                current_callback = cls.handlers_callback.get(main_key, None)
                if current_callback:
                    await current_callback.handler(bot_id, CallbackQuery(**callback_query))
                    return

            # dict handlers
            current_schema = cls.handlers_callback.get(main_key)
            if current_schema:
                separator = callback_text[0]
                filter_from_callback = callback_text[1:].split(separator)

                for key, value in current_schema.items():
                    ff_current_schema = key[1:].split(separator)
                    len_ff_current_schema = len(ff_current_schema)
                    if len_ff_current_schema != len(filter_from_callback):
                        continue

                    is_valid = True
                    for _ in range(len_ff_current_schema):
                        if ff_current_schema[_] != '' and ff_current_schema[_] != filter_from_callback[_]:
                            is_valid = False
                            break

                    if is_valid:
                        callback_data = dict(zip(cls.handlers_callback[main_key + '_schema'], filter_from_callback))
                        callback_query['data'] = callback_data
                        await value.handler(bot_id, CallbackQuery(**callback_query))
                        continue

        list_messages = data['result']
        for _ in list_messages:
            callback_query = _.get('callback_query')
            if callback_query:
                await parse_callback_query(callback_query)
                continue

            # all messages
            message = _.get('message')
            if message:
                entities = message.get('entities', None)
                if entities:
                    if entities[0]['type'] == 'bot_command':
                        command = message['text'][1:]
                        msg = command.split(' ')
                        current_handler = cls.handlers_command.get(msg[0], None)
                        if current_handler:
                            message = Message(**message)
                            if len(msg) == 2:
                                await current_handler.handler(bot_id, message, msg[1])
                            else:
                                await current_handler.handler(bot_id, message)
                        continue
