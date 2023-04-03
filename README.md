A library for simultaneous operation of a large number of telegram bots 
with a single code base. 

**Python - telegram API adapter**. 
Based in [Pydantic](https://github.com/pydantic/pydantic) model libraries 

You need to implement a web interface for a webhook 
yourself. I recommend [FastAPI](https://github.com/tiangolo/fastapi).

___
1. Fill in the dispatcher tokens in a convenient way for you in the format dict(int(bot_id), str(token)
2. Define callback, message, and command handlers
3. Connect the dispatcher to processing incoming webhooks.
4. Done!
___



The filtering of the callbacks was taken from [aiogram](https://github.com/aiogram/aiogram/), the syntax is identical

example main.py


    from megabot.dispatcher import Dispatcher
    from megabot.poster import MessageService
    from megabot.utils.callback_data import CallbackData

    menu_cat = CallbackData('cat', 'id') # Callback fabric 
    message_service = MessageService()

    async def hello_word(callback: CallbackQuery):
        print(message_service.data)
        await message_service.callback_answer(self.dp.tokens[bot_id], callback.id)
        
    dp = Dispatcher()

    bot_id = 9***9
    token = '9***9:AA*****AA'
    dp.tokens[bot_id] = token
    
    dp.register_handler_callback(hello_word, callback_filter=menu_cat.filter())


webhook router file:

    from main import dp

    async def data_router(self, bot_id: int, data: dict) -> NoReturn:
        token, user_uuid = await self.bot_service.get_token(bot_id)
        if not(dp.tokens.get(bot_id, None)):
            dp.tokens[bot_id] = token

        await dp.message_router(bot_id, data)

for local testing: NOT FOR PROD!!!
    add to main.py
    
    offset = 0
    
    async def check_updates():
        global offset
        while True:
            result, error = await get_updates(token, offset)
            if result:
                result_list = result['result']
                if len(result_list) > 0:
                    print(result)
                    offset = result_list[-1]['update_id']+1
                await dp.message_router(bot_id, result)
            else:
                print(error)
            await asyncio.sleep(1)
    
    
    await def start_bot()
        asyncio.create_task(check_updates())

add start_bot() to main file web_hooks 