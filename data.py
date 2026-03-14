"""
Глобальное хранилище данных для бота.
"""
from bot_init import log

# Простое хранилище: { userId: {"code": code, "token": token} }
memory_storage = {}
code_index = {}

def save_user_data(userId: str, code: str, token: str) -> bool:
    try:
        code = str(code)

        # Проверка: уже есть userId
        if userId in memory_storage:
            old_code = memory_storage[userId]["code"]
            log.warning(f"⚠️ Перезапись данных для userId {userId} (старый код: {old_code}, новый код: {code})")

            # удаляем старый индекс
            if str(old_code) in code_index:
                del code_index[str(old_code)]

        # Проверка: код уже существует
        if code in code_index:
            old_user = code_index[code]
            log.warning(f"⚠️ Код {code} уже был выдан userId {old_user}. Перезаписываем на {userId}")

        # Сохраняем данные
        memory_storage[userId] = {
            "code": code,
            "token": token
        }

        code_index[code] = userId

        log.info(f"✅ Данные сохранены для userId: {userId} (код: {code})")
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
