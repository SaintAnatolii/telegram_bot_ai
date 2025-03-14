import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from conf import CONF
import datetime
from bot import main_bot


API_TOKET = CONF['telegram']

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKET)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_answer(message: types.Message):
    await message.reply(f"Hello, I'm a bot!\n{datetime.datetime.now()}")

@dp.message(Command("who_im"))
async def get_self_info(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    language_code = message.from_user.language_code
    await message.answer(f"""
        Hi😊 {username}.
        Here is your information: \n
        🆔User  ID: {user_id} \n
        👤Username: {username} \n
        🧑User  firstname: {first_name} \n
        👨‍👩‍👧‍👦User  lastname: {last_name} \n
        🌐Language Code: {language_code} \n
    """)

@dp.message(Command("status"))
async def get_status(message: types.Message):
    chat_member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    status = chat_member.status
    await message.answer(f"Your status is {status}")

@dp.message(Command("my_photo"))
async def get_user_photo(message: types.Message):
    photos = await bot.get_user_profile_photos(message.from_user.id)
    if photos.total_count > 0:
        file_id = photos.photos[0][0].file_id
        # ! скачивания
        # file  = await bot.get_file(file_id)
        # photo_url = f'https://api.telegram.org/file/bot{API_TOKET}/{file.file_path}'
        # await message.answer(photo_url)
        # ! для просмотра
        await message.answer_photo(file_id)
    else:
        await message.answer("No photo found")

@dp.message()
async def echo_handler(message: types.Message):

    try:
        content = message.text
        res = await main_bot(content)
        await message.answer(res)

    except TypeError:

        await message.answer("Nice try!")

async def general():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(general())
