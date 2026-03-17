from datetime import datetime, timezone

import aiohttp
from disnake import Game
from disnake.ext import tasks

from bot_init import bot, env_cfg, log

timeout = aiohttp.ClientTimeout(total=5)

def get_round_duration(start_time: str) -> str:
    """Возвращает длительность раунда."""
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        delta = now - start

        minutes = int(delta.total_seconds() // 60)
        seconds = int(delta.total_seconds() % 60)

        return f"{minutes}м {seconds}с"
    except Exception:
        return "неизвестно"


@tasks.loop(seconds=60)
async def monitor_status_ss14():
    log.info("🔍 Проверка статуса сервера SS14...")

    url = f"http://{env_cfg.IP_HOST}:1212/status"

    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()

                    round_time = get_round_duration(data["round_start_time"])

                    log.info(
                        f"✅ Статус сервера: "
                        f"{data['players']}/{data['soft_max_players']} игроков | "
                        f"раунд {round_time}"
                    )

                    await bot.change_presence(
                        activity=Game(
                            name=f"{data['players']}/{data['soft_max_players']} | раунд {round_time}"
                        )
                    )

                else:
                    log.warning(
                        f"⚠️ Не удалось получить статус сервера: код {resp.status}"
                    )

    except Exception as e:
        log.error(f"❌ Ошибка при мониторинге статуса сервера: {e}")
