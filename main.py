"""
Модуль для запуска приложения.
"""

import importlib
import pkgutil

from bot_init import bot, env_cfg

def auto_import_modules(package):
    """Автоматический импорт всех модулей из указанного пакета."""
    package = importlib.import_module(package)
    for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package}.{module_name}")

if __name__ == "__main__":
    # Автоматический импорт всех модулей из папки "cogs"
    auto_import_modules("commands")
    auto_import_modules("events")
    auto_import_modules("tasks")
    auto_import_modules("modules")
    # . . .
    
    if env_cfg.DISCORD_TOKEN == "NULL":
        print("КРИТИЧЕСКАЯ ОШИБКА: DISCORD_TOKEN не найден в переменных окружения!")
        exit(1)
    else:
        print("Запуск бота...")     
        bot.run(env_cfg.DISCORD_BOT_TOKEN)
