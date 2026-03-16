import aiohttp
from disnake import Game
from disnake.ext import tasks

from bot_init import bot, env_cfg, log


@tasks.loop(seconds=60)
async def monitor_status_ss14():
    """
    Фоновая задача для мониторинга статуса сервера SS14.
    """
    log.info("🔍 Проверка статуса сервера SS14...")

    url = f"http://{env_cfg.IP_HOST}:1212/status"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    log.info(f"✅ Статус сервера: {data['players']}/{data['soft_max_players']} игроков на карте {data['map']}")
                    await bot.change_presence(
                        activity=Game(name=f"{data['players']}/{data['soft_max_players']} на {data['map']}")
                    )
                else:
                    log.warning(f"⚠️ Не удалось получить статус сервера: код {resp.status}")
    except Exception as e:
        log.error(f"❌ Ошибка при мониторинге статуса сервера: {e}")
