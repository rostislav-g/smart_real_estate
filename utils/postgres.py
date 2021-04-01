from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from common import get_os_envs


def get_engine() -> Engine:
    """
    Функция иницилизурует DB API Engine
    """
    credentials = get_os_envs(variables=['username', 'password', 'db_name', 'url'])
    engine = create_engine(f"postgresql://{credentials['username']}:{credentials['password']}@{credentials['url']}/{credentials['db_name']}")
    # engine.connect().close()  # Для проверки аутентификации
    return engine