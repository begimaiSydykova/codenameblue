from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
from decouple import config

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
db = Dispatcher(bot=bot)


@db.message_handler(commands='hello')
async def start_handler(msg: types.Message):
    await bot.send_message(msg.from_user.id, f'Hello {msg.from_user.first_name}!')
    await msg.answer('пока что всё!')


@db.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
