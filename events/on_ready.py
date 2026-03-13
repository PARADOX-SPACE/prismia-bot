from bot_init import bot, env_cfg, log


async def start_task_if_not_running(task, task_name: str):
    """
    Запускает задачу, если она еще не запущена.
    """
    if not task.is_running():
        task.start()
        print(f"✅ Задача {task_name} запущена.")
    else:
        print(f"⚙️ Задача {task_name} уже работает.")


@bot.event
async def on_ready():
    """
    Событие, которое выполняется при запуске бота.
    """
    await bot.sync_commands() # Синхронизация команд при запуске

    guild_names = [guild.name for guild in bot.guilds]
    log.info("✅ Connected to Discord successfully.")
    log.info(f"✅ Guilds: {guild_names}")
    log.info(f"✅ Bot {bot.user.name} (ID: {bot.user.id}) is ready to work!")

    # Логирование запуска бота в канал
    log_channel = bot.get_channel(env_cfg.LOG_TECH_CHANNEL)
    if not log_channel:
        log.warning("Channel LOG_TECH_CHANNEL not found!!")
        return
    try:
        await log_channel.send(f"✅ **{bot.user.name}** запущен и готов к работе!")
        log.info("✅ Startup log sent to Discord channel")
    except Exception as e:
        log.error(f"❌ Failed to send log: {e}")

    # Запуск всех фоновых задач
    # tasks_to_start = [
    #     (monitor_commits, "Monitor Commits"),
    #     (update_member_count, "Update Member Count"),
    # ]
    # Для дебага
    # tasks_to_start = []
    # for task, name in tasks_to_start:
    #     await start_task_if_not_running(task, name)
