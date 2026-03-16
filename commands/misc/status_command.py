import aiohttp
from bot_init import bot, env_cfg
from disnake import Embed


embed_status = {
    "title": "Статус сервера",
    "color": 0x8000ff,
    "fields": [
        {"name": "Название", "value": "data['name']", "inline": False},
        {"name": "Игроки", "value": "f\"{data['players']}/{data['soft_max_players']}\"", "inline": False},
        {"name": "Карта", "value": "data['map']", "inline": False},
        {"name": "Статус", "value": "'Раунд идёт' if data['run_level'] == 1 else 'Неизвестно'", "inline": False},
        {"name": "Раунд ID", "value": "data['round_id']", "inline": False},
    ]
}


@bot.command(name="status")
async def status_command(ctx, server: str = "mrp"):
    '''Команда для получения информации о сервере'''
    if server.lower() == "mrp":
        address = env_cfg.IP_HOST
        port = "1212"

    url = f"http://{address}:{port}/status"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()

                    embed = Embed(title=embed_status["title"], color=embed_status["color"])
                    for field in embed_status["fields"]:
                        embed.add_field(name=field["name"], value=eval(field["value"]), inline=field["inline"])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Ошибка: код {resp.status}")
    except Exception as e:
        await ctx.send(f"Ошибка: {e}")
