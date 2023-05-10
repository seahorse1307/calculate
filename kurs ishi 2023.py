import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6068837998:AAFsfMc233HQtn393X3XUkIl0_2Pq_WULiI'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())

mainKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='To\'g\'ri foizlash')
        ],
        [
            KeyboardButton(text='Teskari foizlash')
        ]
    ],
    resize_keyboard=True
)


class mainState(StatesGroup):
    mainState = State()


class TrueState(StatesGroup):
    mainState = State()


class FalseState(StatesGroup):
    mainState = State()


class trueState(StatesGroup):
    mainState = State()


class falseState(StatesGroup):
    mainState = State()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!\nBotga xush kelibsiz.", reply_markup=mainKey)
    await mainState.mainState.set()


@dp.message_handler(text='To\'g\'ri foizlash', state=mainState)
async def trueF(m: types.Message, state: FSMContext):
    await m.reply('sum: ')
    await state.finish()
    await TrueState.mainState.set()


@dp.message_handler(state=TrueState)
async def foizlash1(m: types.Message, state: FSMContext):
    await state.finish()
    global summa
    summa = m.text
    await m.reply('foiz')
    await trueState.mainState.set()


@dp.message_handler(state=trueState)
async def foizlash2(m: types.Message, state: FSMContext):
    await state.finish()
    txt = float(summa) * float(m.text) / 100
    await m.reply(str(txt), reply_markup=mainKey)
    await mainState.mainState.set()


@dp.message_handler(text='Teskari foizlash', state=mainState)
async def trueF(m: types.Message, state: FSMContext):
    await m.reply('sum: ')
    await state.finish()
    await FalseState.mainState.set()


@dp.message_handler(state=FalseState)
async def foizlash3(m: types.Message, state: FSMContext):
    await state.finish()
    global summa
    summa = m.text
    await m.reply('foiz')
    await falseState.mainState.set()


@dp.message_handler(state=falseState)
async def foizlash2(m: types.Message, state: FSMContext):
    await state.finish()
    txt = float(summa) / float(m.text) * 100
    await m.reply(str(txt), reply_markup=mainKey)
    await mainState.mainState.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    