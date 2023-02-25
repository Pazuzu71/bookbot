from aiogram import Bot, Dispatcher
from typing import Text
from config_data.config import load_config, Config


config: Config = load_config()
TOKEN = config.tgbot.token
print(TOKEN)

