from aiogram import types, Bot, executor, Dispatcher
from gtts import gTTS
import random as rand
import os
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5752210475:AAG22iNY1Hs6MFXzN3Zwy4I8fQPEAbpA8DM"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

markup = ReplyKeyboardMarkup(resize_keyboard=True)

button_author = KeyboardButton("🏆Об Авторе🏆")
button_start = KeyboardButton("👋Приветствие👋")
button_help = KeyboardButton("ℹ️Помощьℹ️")

markup.add(button_author)
markup.add(button_start)
markup.add(button_help)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\nЯ бот-озвучиватель, чтобы получить озвучку, введи /sound <текст>\n\n⚠️Бот работает только на русском языке⚠️\n\nОстальное смотри в /help, и подсказках!", reply_markup=markup)

@dp.message_handler(commands='sound')
async def sound(message: types.Message):
    filename = list(str(rand.random()) + ".mp3")
    data_raw = list(message.text)
    
    del filename[1]
    filename = "".join(filename)

    stopper = False

    data_raw.remove('/')
    data_raw.remove('s')
    data_raw.remove('o')
    data_raw.remove('u')
    data_raw.remove('n')
    data_raw.remove('d')

    try:
        del data_raw[0]
    except:
        stopper = True


    data = "".join(data_raw)

    if (data == " "):
        await message.answer('Ошибка, попробуйте ещё раз.\nВведите /help для помощи!')
    elif (stopper == True):
        await message.answer('Ошибка, попробуйте ещё раз.\nВведите /help для помощи!')
    else:
        tts = gTTS(data, lang="ru")

        with open(filename, "wb") as f:
            tts.write_to_fp(f)
            f.close()

        await message.answer(f"Ваш файл с кодом генерации {filename}, и данными \"{data}\" готов!")
        await message.answer("Отправка...")

        with open(filename, 'rb') as f:
            await bot.send_document(message.chat.id, f)

        os.remove(filename)

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer("***⚠️ Помощь ⚠️***\n\n/sound <ваш текст>\n\n*** Примеры ***\n/sound Привет\n/sound Как дела")

@dp.message_handler(commands="author")
async def author(message: types.Message):
	markup_url = InlineKeyboardMarkup()
	button_author_url = InlineKeyboardButton(text="Написать автору", url="t.me/bithoffka")

	markup_url.add(button_author_url)

	await bot.send_message(message.chat.id, "Сделано @bithoffka на Python", reply_markup=markup_url)
	await bot.send_message(message.chat.id, "Спасибо, что пользуетесь ботом", reply_markup=markup)

@dp.message_handler()
async def handler(message: types.Message):
	text = message.text

	if text == "👋Приветствие👋":
		await start(message)
	elif text == "🏆Об Авторе🏆":
		await author(message)
	elif text == "ℹ️Помощьℹ️":
		await help(message)
	else:
		await message.answer("Ваша команда не распознана, введите /help для помощи!")

if __name__ == '__main__':
    executor.start_polling(dp)
