from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from crud_functions import *

api = '7632417742:AAGsGxZ67hoES9bqmPNeaLqxSfhOKaMmtbk'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

products = get_all_products()

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.add(button)
kb.insert(button2)
kb.add(button3)
kb.add(button4)
kb.resize_keyboard = True

kbin = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')

kbin.add(button)
kbin.insert(button2)

kbin_product = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Product 1', callback_data="product_buying")
button2 = InlineKeyboardButton(text='Product 2', callback_data="product_buying")
button3 = InlineKeyboardButton(text='Product 3', callback_data="product_buying")
buttron4 = InlineKeyboardButton(text='Product 4', callback_data="product_buying")

kbin_product.add(button, button2, button3, buttron4)

"""@dp.callback_query_handler(text = 'info')
async def infor(call):
    await call.message.answer('Информация о боте')
    await call.answer()"""


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя:')
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_email(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data["username"], data["email"], data["age"])
    await message.answer('Регистрация завершена')
    await state.finish()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберете опцию', reply_markup=kbin)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('(10 * ваш вес) + ( 6.25 * ваш рост ) - (5 * ваш возраст) - 161')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет!', reply_markup=kb)


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    form = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) - 161
    await message.answer(f'Ваша дневная норма каллорий: {form}')
    await state.finish()


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    list_jpg = ['ghoul.jpg | Спать', 'beliy.jpg | Быть на веселе', 'kushat.jpg | Кушать', 'nagei.jpg | Быть Кирилом']

    k = 0
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        with open(f'{list_jpg[k].split(" | ")[0]}', 'rb') as jpg:
            await message.answer_photo(jpg)
        k = k + 1
    await message.answer('Выберите продукт для покупки:', reply_markup=kbin_product)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
