import asyncio
from config import token, user_id
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from parser import parser
import csv
from warnings import filterwarnings

filterwarnings("ignore")
loop = asyncio.get_event_loop()
bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())


class Base(StatesGroup):
    pages_to_parsing = State()
    pages_to_timer = State()


# обработчик команды старт
@dp.message_handler(commands="start", state=None)
async def start(message: types.Message):
    start_buttons = ["🛠 Отопители", "📟 Пульты", "🔧 Блоки", 'Help']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Enter number of pages to automatic parsing or write 'no'", reply_markup=keyboard)
    await Base.pages_to_parsing.set()

    @dp.message_handler(state=Base.pages_to_parsing)
    async def pag_quantity(message: types.Message, state: FSMContext):
        answer = int(message.text)
        await state.update_data(cell_1=answer)
        data = await state.get_data()
        pagenation_quantity = data.get('cell_1')
        # await state.finish()
        await message.answer('Automatic parsing started')
        while True:
            try:
                parser('https://bamper.by/zchbu/zapchast_avtonomnyy-otopitel/', './files/heater_last.csv',
                       './files/heater_old.csv', pagenation_quantity)
                with open('./files/heater_last.csv', 'r', newline='', encoding='utf-8') as file:
                    lenght = sum(1 for line in file)
                with open('./files/heater_last.csv', 'r', newline='', encoding='utf-8') as file:
                    file_reader = csv.reader(file, delimiter=";")
                    # count = 0  # Счетчик для подсчета количества строк и вывода заголовков столбцов
                    if lenght != 0:
                        await bot.send_message(user_id, f'Новинки:')
                        for row in file_reader:
                            # Вывод строк
                            await bot.send_message(user_id, f'{row[0]} : {row[1]} : {row[3]} : {row[4]}')
                await asyncio.sleep(600)
            except Exception as ex:
                await bot.send_message(user_id, f'Нешта не так с сайтом.')
                await bot.send_message(user_id, f'{ex}')
                await asyncio.sleep(60)


@dp.message_handler(Text(equals="🛠 Отопители"))
async def get_heater_list(message: types.Message):
    await message.answer('Please waiting...')
    parser('https://bamper.by/zchbu/zapchast_avtonomnyy-otopitel/', './files/heater_last.csv', './files/heater_old.csv')
    with open('./files/heater_last.csv', 'r', newline='', encoding='utf-8') as file:
        lenght = sum(1 for line in file)
    with open('./files/heater_last.csv', 'r', newline='', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=";")
        count = 0  # Счетчик для подсчета количества строк и вывода заголовков столбцов
        if lenght > 1:
            await message.answer(f'Новинки:')
            for row in file_reader:
                # Вывод строк
                await message.answer(f'{row[0]} : {row[1]} : {row[3]} : {row[4]}')
            count += 1
        else:
            await message.answer(f'няма ничога')


@dp.message_handler(Text(equals="📟 Пульты"))
async def get_timer_list(message: types.Message):
    await message.answer("Enter number of pages to parsing")
    await Base.pages_to_timer.set()

    @dp.message_handler(state=Base.pages_to_timer)
    async def pag_quantity(message: types.Message, state: FSMContext):
        answer = int(message.text)
        await state.update_data(cell_2=answer)
        data = await state.get_data()
        pagenation_quantity = data.get('cell_2')
        await state.finish()
        await message.answer('Please waiting...')
        parser('https://bamper.by/zchbu/zapchast_pult-upravleniya-avtonomnym-otopitelem/', './files/timer_last.csv',
               './files/timer_old.csv', pagenation_quantity)
        with open('./files/timer_last.csv', 'r', newline='', encoding='utf-8') as file:
            lenght = sum(1 for line in file)
        with open('./files/timer_last.csv', 'r', newline='', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=";")
            count = 0  # Счетчик для подсчета количества строк и вывода заголовков столбцов
            if lenght > 1:
                await message.answer(f'Новинки:')
                for row in file_reader:
                    # Вывод строк
                    await message.answer(f'{row[0]} : {row[1]} : {row[3]} : {row[4]}')
                count += 1
            else:
                await message.answer(f'няма ничога')


@dp.message_handler(Text(equals="🔧 Блоки"))
async def get_ecu_list(message: types.Message):
    await message.answer('Please waiting...')
    parser('https://bamper.by/zchbu/zapchast_blok-upravleniya-avtonomnym-otopitelem/', './files/ecu_last.csv',
           './files/ecu_old.csv')
    with open('./files/ecu_last.csv', 'r', newline='', encoding='utf-8') as file:
        lenght = sum(1 for line in file)
    with open('./files/ecu_last.csv', 'r', newline='', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=";")
        count = 0  # Счетчик для подсчета количества строк и вывода заголовков столбцов
        if lenght > 1:
            await message.answer(f'Новинки:')
            for row in file_reader:
                # Вывод строк
                await message.answer(f'{row[0]} : {row[1]} : {row[3]} : {row[4]}')
            count += 1
        else:
            await message.answer(f'няма ничога')


@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='no', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ake')


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
