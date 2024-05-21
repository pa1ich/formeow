from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = Bot('6585278213:AAGJpqI-MulfRZB9L4NZM2YVQU3R3RHxIOE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup()
    button = KeyboardButton('Open WEB-site', web_app=WebAppInfo(url='index.html'))
    markup.add(button)
    await message.answer('Привет мой друг!', reply_markup=markup)

executor.start_polling(dp, skip_updates=True)
