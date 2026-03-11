"""
Глобальное хранилище данных для бота.
"""
from bot_init import log

# Простое хранилище: { userId: {"code": code, "token": token} }
memory_storage = {}

def save_user_data(userId: str, code: str, token: str) -> bool:
    """
    Сохраняет данные пользователя.
    Если userId уже существует — перезаписывает.
    """
    try:
        memory_storage[userId] = {
            "code": code,
            "token": token
        }
        log.info(f"✅ Данные сохранены для userId: {userId}")
        return True
    except Exception as e:
        log.error(f"❌ Ошибка сохранения данных: {e}")
        return False

def get_user_data(userId: str) -> dict | None:
    """Возвращает данные пользователя или None"""
    return memory_storage.get(userId)

def delete_user_data(userId: str) -> bool:
    """Удаляет данные пользователя"""
    if userId in memory_storage:
        del memory_storage[userId]
        log.info(f"🗑️ Данные удалены для userId: {userId}")
        return True
    return False

def get_all_data() -> dict:
    """Возвращает все данные (для отладки)"""
    return memory_storage.copy()
