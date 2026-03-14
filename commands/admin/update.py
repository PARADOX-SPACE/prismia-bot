from disnake import AppCommandInteraction
import requests
from requests.auth import HTTPBasicAuth
from bot_init import bot, env_cfg
from modules.check_roles import has_any_role_by_keys


@bot.slash_command(name="update", description="Посылает запрос на обновление сервера.")
@has_any_role_by_keys("head_team")
async def update_command(inter: AppCommandInteraction):

    await inter.response.defer(ephemeral=True)

    url = f"http://{env_cfg.IP_HOST}:5000/instances/{env_cfg.NAME_INST}/update"

    try:
        response = requests.post(
            url,
            auth=HTTPBasicAuth(env_cfg.NAME_INST, env_cfg.POST_REQUEST_WATCHDOG),
            timeout=10  # таймаут в секундах
        )

        if response.status_code == 200:
            await inter.edit_original_response(
                f"✅ Запрос на обновление отправлен.\nОтвет сервера:\n```{response.text}```"
            )
        else:
            await inter.edit_original_response(
                f"⚠️ Сервер вернул ошибку.\n"
                f"Status: **{response.status_code}**\n"
                f"```{response.text}```"
            )

    except requests.Timeout:
        await inter.edit_original_response(
            "⏱ Сервер не ответил (timeout 10s)."
        )

    except requests.RequestException as e:
        await inter.edit_original_response(
            f"❌ Ошибка запроса:\n```{e}```"
        )
