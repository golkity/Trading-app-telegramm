from aiogram import Bot,Dispatcher,exceptions,types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('TOKEN')
dp = Dispatcher(bot)

#treking command start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open web app',web_app=WebAppInfo(url='url your web site')))
    await message.answer('Hellow my dear friend!',reply_markup=markup)

executor.start_polling(dp)
