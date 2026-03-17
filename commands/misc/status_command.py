from datetime import datetime, timezone

import aiohttp
from disnake import Embed

from bot_init import bot, env_cfg

timeout = aiohttp.ClientTimeout(total=5)

def get_round_duration(start_time: str) -> str:
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        delta = now - start

        minutes = int(delta.total_seconds() // 60)
        seconds = int(delta.total_seconds() % 60)

        return f"{minutes}м {seconds}с"
    except Exception:
        return "неизвестно"


@bot.command(name="status")
async def status_command(ctx, server: str = "mrp"):
    """Команда для получения информации о сервере"""

    if server.lower() == "mrp":
        address = env_cfg.IP_HOST
        port = "1212"

    url = f"http://{address}:{port}/status"

    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:

                if resp.status != 200:
                    await ctx.send(f"Ошибка: код {resp.status}")
                    return

                data = await resp.json()

                round_time = get_round_duration(data["round_start_time"])

                embed = Embed(
                    title="Статус сервера",
                    color=0x8000ff
                )

                embed.add_field(
                    name="Название",
                    value=data["name"],
                    inline=False
                )

                embed.add_field(
                    name="Игроки",
                    value=f"{data['players']}/{data['soft_max_players']}",
                    inline=False
                )

                embed.add_field(
                    name="Раунд идёт",
                    value=round_time,
                    inline=False
                )

                embed.add_field(
                    name="Раунд ID",
                    value=data["round_id"],
                    inline=False
                )

                await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"Ошибка: {e}")
