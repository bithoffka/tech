#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import qrcode
import random
import os

token = "5754640726:AAGhih1pWh5iK8-sbKhGcy7nCcR2mniO39Q"

bot = Bot(token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

markup = ReplyKeyboardMarkup(resize_keyboard=True)

button_author = KeyboardButton("🏆Об Авторе🏆")
button_start = KeyboardButton("👋Приветствие👋")
button_help = KeyboardButton("ℹ️Помощьℹ️")

markup.add(button_author)
markup.add(button_start)
markup.add(button_help)

@dp.message_handler(commands="start")
async def start(message: types.Message):
	await bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}\nЭтот бот простой генератор QR кодов!\nДля подсказки пиши /help, или посмотри в меню!", reply_markup=markup)

@dp.message_handler(commands="make")
async def make(message: types.Message):
	filename_raw = str(random.random()) + ".jpg"
	data_raw = list(message.text)

	stopper = False

	data_raw.remove('/')
	data_raw.remove('m')
	data_raw.remove('a')
	data_raw.remove('k')
	data_raw.remove('e')

	try:
		del data_raw[0]
	except Exception as _e:
		e = str(_e)
		stopper = True

	data = "".join(data_raw)

	filename = list(filename_raw)
	del filename[1]
	filename = "".join(filename)

	if (data == " "):
		await message.answer('Ошибка, попробуйте ещё раз.\nВведите /help для помощи!')
		await bot.send_message(message.chat.id, "***Остальные функции***", reply_markup=markup)
	elif (stopper == True):
		await message.answer('Ошибка, попробуйте ещё раз.\nВведите /help для помощи!')
		await bot.send_message(message.chat.id, "***Остальные функции***", reply_markup=markup)
	else:
		img = qrcode.make(data)
		img.save(filename, 'JPEG')

		qr_image = open(filename, 'rb')

		await message.answer(f"Ваш QR код с данными\n\"{data}\"\nи кодом генерации\n{filename}\nуспешно сгенерирован!")
		await message.answer('Отправка...')
		await bot.send_photo(message.chat.id, qr_image)

		await bot.send_message(message.chat.id, "***Остальные функции***", reply_markup=markup)

		os.remove(filename)

@dp.message_handler(commands="help")
async def help(message: types.Message):
	await bot.send_message(message.chat.id, f"***Помощь***\n\nДля генерации QR кода используйте команду /make\n\n***Примеры***\n/make Hello, World! - QR код с данными \"Hello, World!\"\n/make google.com - QR код с данными \"google.com\"", reply_markup=markup)

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