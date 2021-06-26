# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from config import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        quote=True,
	reply_markup=START_BUTTONS
    )

async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
      	disable_web_page_preview=True,
        quote=True,
	reply_markup=HELP_BUTTONS
    )

async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        quote=True,
	reply_markup=ABOUT_BUTTONS
    )