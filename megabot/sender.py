import requests

from .models import (AnswerCallbackQuery, ForceReply, InlineKeyboardMarkup, InputFile, ReplyKeyboardMarkup,
                     ReplyKeyboardRemove, SendMessage, SendPhoto)


class Base:
    def request_url(self, token, command):
        return f'https://api.telegram.org/bot{token}/{command}'


class MessageService(Base):
    async def callback_answer(
        self,
        token: str,
        callback_query_id: str,
        text: str | None = None,
        show_alert: bool | None = None,
        url: str | None = None,
        cache_time: str | None = None,
    ):
        message = AnswerCallbackQuery(
            callback_query_id=callback_query_id, text=text, show_alert=show_alert, url=url, cache_time=cache_time
        ).dict()
        request_url = self.request_url(token, 'answerCallbackQuery')
        response = requests.post(url=request_url, json=message)
        return response

    async def send_message(
        self,
        token: str,
        chat_id: int,
        message_thread_id: int | None = None,
        text: str | None = None,
        parse_mode: str | None = None,
        entities: list | None = None,
        disable_web_page_preview: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None,
    ):
        message = SendMessage(
            chat_id=chat_id,
            message_thread_id=message_thread_id,
            text=text,
            parse_mode=parse_mode,
            entities=entities,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        ).dict()
        request_url = self.request_url(token, 'sendMessage')
        response = requests.post(url=request_url, json=message)
        return response

    async def send_photo(
        self,
        token: str,
        chat_id: int,
        photo: str | InputFile,
        message_thread_id: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None,
    ):
        message = SendPhoto(
            chat_id=chat_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
        ).dict()
        if reply_markup:
            message['reply_markup'] = reply_markup.json()

        request_url = self.request_url(token, 'sendPhoto')
        if isinstance(photo, str):
            message['photo'] = photo
            response = requests.post(url=request_url, data=message)
        else:
            response = requests.post(url=request_url, data=message, files={'photo': photo})
        return response.json()


async def get_updates(token: str, offset=0):
    request_url = f'https://api.telegram.org/bot{token}/getUpdates'
    data = {'offset': offset}
    response = requests.post(url=request_url, data=data)
    if response.status_code == 200:
        result = response.json()
        return result, None
    return None, response
