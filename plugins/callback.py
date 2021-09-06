# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from config import *
from pyrogram import Client
from .commands import *
from .modules import modules_help


@Client.on_callback_query(
    filters.user(BOT_OWNER) if PRIVATE else None
)
async def cb_handler(bot, update):
    if update.data == "home":
        await start(bot, update, cb=True)
    elif update.data == "help":
        await help(bot, update, cb=True)
    elif update.data == "about":
        await about(bot, update, cb=True)
    elif update.data == "close":
        await update.message.delete()
    elif update.data.startswith("modules"):
        await modules_help(bot, update, cb=True)
