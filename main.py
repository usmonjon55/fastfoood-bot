import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6025864995:AAHm6vJUnX_KFI17E1LFceI4M1VyZRMGcaY'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

til_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbekcha"),
            KeyboardButton(text="🇷🇺 Русский"),
            KeyboardButton(text="🇺🇸 English"),
        ],
        [
            KeyboardButton(text="↩orqaga"),
        ]
    ],
    resize_keyboard=True
)

uzb_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ichimliklar"),
            KeyboardButton(text="Lavashlar")
        ],
        [
            KeyboardButton(text="Burgerlar"),
            KeyboardButton(text="Pizzalar")
        ],
        [
            KeyboardButton(text="orqaga"),
        ]
    ],
    resize_keyboard=True
)


ichimliklar_menu_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Coca Cola"),
            KeyboardButton(text="Fanta"),
            KeyboardButton(text="Pepsi")
        ],
        [
            KeyboardButton(text="orqaga"),
        ]
    ], 
    resize_keyboard=True
)



cola_menu_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="orqaga"),
        ]
    ], 
    resize_keyboard=True
)

fanta_menu_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="orqaga"),
        ]
    ], 
    resize_keyboard=True
)


pepsi_menu_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="orqaga"),
        ]
    ], 
    resize_keyboard=True
)









@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("""Muloqot tilini tanlang
Выберите язык
Select Language""", reply_markup=til_menu_keyboard)



@dp.message_handler(text="🇺🇿 O'zbekcha")
async def send_welcome(message: types.Message):
    await message.answer("O'zbekcha", reply_markup=uzb_menu_keyboard)



@dp.message_handler(text="Ichimliklar")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://sagaciresearch.com/wp-content/uploads/2019/09/Top-10-Carbonated-Soft-Drinks-Egypt-V3.jpg")
    await message.answer("Ichimlilar", reply_markup=ichimliklar_menu_keyboard)



@dp.message_handler(text="Coca Cola")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://ru.coca-cola.uz/content/dam/one/uz/ru/product-images/coca-cola-classic.jpg")
    await message.answer("Coca Cola  narxi: 7000", reply_markup=cola_menu_keyboard)

@dp.message_handler(text="Fanta")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://web.lebazar.uz/resources/product/2023/3/5/medium_1680695346345101020102-00001.png")
    await message.answer("Fanta narxi: 7000", reply_markup=fanta_menu_keyboard)

@dp.message_handler(text="Pepsi")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://gomart.uz/251-large_default/pepsi-1l.jpg")
    await message.answer("Pepsi narxi: 7000", reply_markup=pepsi_menu_keyboard)






@dp.message_handler(text="orqaga")
async def echo(message: types.Message):
    await message.answer("Menu", reply_markup=til_menu_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)