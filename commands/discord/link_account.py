import time
from collections import defaultdict

import disnake
from disnake.ext import commands

from bot_init import bot, env_cfg, log
from data import delete_user_data, get_user_data

# Словарь для отслеживания времени последнего использования команды
# Структура: { (channel_id, user_id): last_used_timestamp }
user_cooldown = defaultdict(float)

# Настройки
USER_COOLDOWN_SECONDS = env_cfg.DISCORD_AUTH_USER_COOLDOWN_SECONDS  # 60 минут между использованием у одного пользователя
ALLOWED_CHANNEL_ID = env_cfg.DISCORD_AUTH_CHANNEL_ID  # ЗАМЕНИТЬ НА ID СВОЕГО КАНАЛА


@bot.command(
    name="link",
    description="Привязать аккаунт по коду. Доступно только в специальном канале."
)
async def link_account(ctx, code: str):
    """
    Команда доступна всем пользователям в специальном канале.
    Привязывает Discord ID к userId по коду.
    """
    
    # Проверка канала
    if ctx.channel.id != ALLOWED_CHANNEL_ID:
        log.warning(f"❌ {ctx.author} попытался использовать команду не в том канале: {ctx.channel.name}")
        # Можно ничего не отвечать или ответить и удалить
        await ctx.send(f"⛔ Эту команду можно использовать только в канале <#{ALLOWED_CHANNEL_ID}>.", delete_after=10)
        return
    
    # Проверка на спам (cooldown для каждого пользователя)
    current_time = time.time()
    cooldown_key = (ctx.channel.id, ctx.author.id)
    last_used = user_cooldown[cooldown_key]
    
    if current_time - last_used < USER_COOLDOWN_SECONDS:
        remaining = int(USER_COOLDOWN_SECONDS - (current_time - last_used))
        await ctx.send(
            f"⏳ {ctx.author.mention}, подождите {remaining} сек. перед следующим использованием.",
            delete_after=remaining
        )
        return
    
    # Обновляем время последнего использования
    user_cooldown[cooldown_key] = current_time
    
    # Поиск данных по коду в памяти
    log.info(f"🔍 {ctx.author} ввёл код: {code}")
    
    user_data = None
    found_user_id = None
    
    # Проходим по всем данным в памяти
    all_data = get_user_data()  # возвращает весь словарь
    for user_id, data in all_data.items():
        if data.get("code") == code:
            user_data = data
            found_user_id = user_id
            break
    
    if not user_data or not found_user_id:
        log.warning(f"⚠️ Код {code} не найден (пользователь {ctx.author})")
        await ctx.send(
            f"❌ {ctx.author.mention}, код `{code}` не найден. Проверьте правильность ввода.",
            delete_after=15
        )
        return
    
    discord_id = ctx.author.id
    user_id = found_user_id
    
    # TODO: Здесь будет запись в PostgreSQL
    # ----------------------------------------
    # 1. Импортировать модуль для работы с БД (например, db.py)
    # 2. Вызвать функцию сохранения связи:
    #    await save_discord_link(discord_id, user_id, code)
    # 3. Обработать возможные ошибки
    # ----------------------------------------
    log.info(f"✅ [TODO] Привязка: Discord {discord_id} -> userId {user_id} с кодом {code}")
    
    # Удаляем данные из памяти после успешной привязки
    delete_user_data(user_id)
    log.info(f"🗑️ Данные для userId {user_id} удалены из памяти")
    
    # Отправляем подтверждение пользователю
    await ctx.send(
        f"✅ {ctx.author.mention}, ваш аккаунт успешно привязан!"
    )
    
    # Опционально: выдать роль (если нужно)
    # role = ctx.guild.get_role(ROLE_ID)
    # if role:
    #     await ctx.author.add_roles(role, reason="Привязка аккаунта")


@link_account.error
async def link_account_error(ctx, error):
    """Обработчик ошибок"""
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ {ctx.author.mention}, укажите код. Пример: `!link ABC123`", delete_after=15)
    else:
        log.error(f"Ошибка в команде link: {error}")
        await ctx.send("❌ Произошла ошибка при выполнении команды.", delete_after=10)
