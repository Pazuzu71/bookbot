from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class Config:
    tgbot: TgBot


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(
        tgbot=TgBot(
            token=env('TOKEN'),
            admin_id=env('ADMIN_ID')
        )
    )
