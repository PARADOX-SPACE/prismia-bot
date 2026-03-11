"""
Этот модуль содержит все основные конфигурации prismia-bot.
"""

import os

from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()

def get_env_variable(name: str, default: str = None) -> str:
    """
    Получает переменную окружения. Если не найдена и default=None - вызывает ошибку.
    """
    value = os.getenv(name)
    if value is None:
        if default is None:
            print(f"КРИТИЧЕСКАЯ ОШИБКА: Переменная {name} обязательна!")
            raise ValueError(f"Не найдена обязательная переменная: {name}")
        print(f"Предупреждение: {name} не найден. Используется default: {default}")
        return default
    return value


class ENVIRONMENT_VAR:
    """Класс для доступа к переменным окружения"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def DISCORD_TOKEN(self) -> str:
        """Токен Discord бота (обязательный)"""
        return get_env_variable("DISCORD_TOKEN", "NULL")
    
    @property
    def REPO_NAME(self) -> str:
        """Название репозитория (по умолчанию 'prismia-bot')"""
        return get_env_variable("REPO_NAME", "prismia-bot")
    
    @property
    def AUTHOR_NAME(self) -> str:
        """Имя автора (по умолчанию 'PARADOX-SPACE')"""
        return get_env_variable("AUTHOR_NAME", "PARADOX-SPACE")
    
    @property
    def LOG_TECH_CHANNEL(self) -> int:
        """ID канала для логов (по умолчанию 1374529148474622085)"""
        return int(get_env_variable("LOG_TECH_CHANNEL", "1374529148474622085"))
    
    @property
    def GUILD_DISCORD_SERVER_ID(self) -> int:
        """ID Discord сервера (по умолчанию 1374389368315449477)"""
        return int(get_env_variable("GUILD_DISCORD_SERVER_ID", "1374389368315449477"))
    
    @property
    def COMMANDS_PREFIX(self) -> str:
        """Префикс для команд бота (по умолчанию '$')"""
        return get_env_variable("COMMANDS_PREFIX", "$")
    
    @property
    def HTTP_SERVER_PORT(self) -> int:
        """Порт для HTTP сервера (по умолчанию 9010)"""
        return int(get_env_variable("HTTP_SERVER_PORT", "9010"))
    
    @property
    def HTTP_SERVER_TOKEN(self) -> str:
        """Токен для авторизации на HTTP сервере (по умолчанию 'my_secret_token_123')"""
        return get_env_variable("HTTP_SERVER_TOKEN", "my_secret_token_123")


# # Инициализация класса
# env_cfg = ENVIRONMENT_VAR()
# """Класс для доступа к переменным окружения в стиле ENVIRONMENT_VAR.KEY"""
