from aiogram import Dispatcher, executor, types, Bot # импорт основных элементов библиотеки
# Dispatcher - класс для создания диспетчера, отслеживающего обновления
# executor - объект по исполнению каких-либо задач
# types - модуль всех типов данных библиотеки
# Bot - класс для создания экземпляра (сущности) бота
from tk import API_TOKEN
from kbs import get_kb_course

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message) -> None:
    await msg.answer('Привет!'
                     '\nЭто расписание для студентов ИВМиИТ.'
                     '\nУ меня есть функции:'
                     '\n\start'
                     '\n\help'
                     '\n\cancel'
                     '\n\delete profile'
                     '\nДавай познакомимся.', reply_markup=get_kb_course())


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message_handler(commands=["help"])
async def process_help_command(message: types.Message) -> None:
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


@dp.message_handler(commands=['cancel'])
async def cmd_cancel(msg: types.Message) -> None:
    await msg.answer('Canceled', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['delete profile'])
async def cmd_cancel(msg: types.Message) -> None:
    await msg.answer('Canceled', reply_markup=types.ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message_handler()
async def send_echo(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')


if __name__ == '__main__':
    executor.start_polling(dp)