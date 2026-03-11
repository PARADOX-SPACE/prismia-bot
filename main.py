"""
Модуль для запуска приложения.
"""

import importlib
import pkgutil
from pathlib import Path

from bot_init import bot, env_cfg, log


def load_modules(folder: str):
    package = importlib.import_module(folder)
    if not package.__file__:
        return
    dir_path = Path(package.__file__).parent
    for _, mod_name, _ in pkgutil.iter_modules([str(dir_path)]):
        importlib.import_module(f"{folder}.{mod_name}")

if __name__ == "__main__":
    # Автоматический импорт всех модулей из папки "cogs"
    load_modules('commands.misc')
    # load_modules('commands.discord')
    load_modules("events")
    # load_modules("tasks")
    load_modules("modules")
    # . . .
    
    if env_cfg.DISCORD_TOKEN == "NULL":
        log.error("КРИТИЧЕСКАЯ ОШИБКА: DISCORD_TOKEN не найден в переменных окружения!")
        exit(1)
    else:
        log.info("Запуск бота...")
        bot.run(env_cfg.DISCORD_BOT_TOKEN)
