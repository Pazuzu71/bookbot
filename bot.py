import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config_data.config import load_config, Config

from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu


# Инициализируем логгер
logger = logging.getLogger(__name__)

# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логгирование
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s'
    )
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную
    config: Config = load_config()
    TOKEN = config.tgbot.token
    ADMIN_ID = config.tgbot.admin_id

    # Инициализация бота и диспетчера
    bot: Bot = Bot(token=TOKEN, parse_mode='HTML')
    dispatcher: Dispatcher = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dispatcher.include_router(user_handlers.router)
    dispatcher.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

    # @dispatcher.message(Command(commands=['start']))
    # async def start(msg: Message):
    #     await msg.reply(f'{msg.from_user.id}')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')
