"""
Глобальное хранилище данных для бота.
"""
from bot_init import log

# Простое хранилище: { userId: {"code": code, "token": token} }
memory_storage = {}
code_index = {}

def save_user_data(userId: str, code: str, token: str) -> bool:
    try:
        memory_storage[userId] = {
            "code": code,
            "token": token
        }

        # индекс по коду
        code_index[str(code)] = userId

        log.info(f"✅ Данные сохранены для userId: {userId}")
        return True

    except Exception as e:
        log.error(f"❌ Ошибка сохранения данных: {e}")
        return False

def get_user_by_code(code: str) -> str | None:
    return code_index.get(str(code))

def get_user_data(userId: str) -> dict | None:
    """Возвращает данные пользователя или None"""
    return memory_storage.get(userId)

def delete_user_data(userId: str) -> bool:
    if userId in memory_storage:
        code = memory_storage[userId]["code"]

        del memory_storage[userId]

        if str(code) in code_index:
            del code_index[str(code)]

        log.info(f"🗑️ Данные удалены для userId: {userId}")
        return True
    return False

def get_all_data() -> dict:
    """Возвращает все данные (для отладки)"""
    return memory_storage.copy()
