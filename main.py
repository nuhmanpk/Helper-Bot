import os
import pyrogram
from pyrogram import Client, filters
from config import *

plugins = dict(root="plugins")

bot = Client(
    "Telegram-Helper-Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH,
    plugins = plugins
)

bot.run()
