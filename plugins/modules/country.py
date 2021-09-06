# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.commands(["country_info", "country_information"]) &
    filters.user(AUTH_USERS) if PRIVATE else None
)
async def countryinfo(bot, update):
    country = update.text.split(" ", -1)
    country = CountryInfo(country)
    info = f"""--**Country Information**--

Name : `{country.name()}`
Native Name : `{country.native_name()}`
Capital : `{country.capital()}`
Population : `{country.population()}`
Region : `{country.region()}`
Sub Region : `{country.subregion()}`
Top Level Domains : `{country.tld()}`
Calling Codes : `{country.calling_codes()}`
Currencies : `{country.currencies()}`
Residence : `{country.demonym()}`
Timezone : `{country.timezones()}`

Made by @FayasNoushad"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Wikipedia', url=f'{country.wiki()}'),
        InlineKeyboardButton('Google', url=f'https://www.google.com/search?q={country_name}')
        ],[
        InlineKeyboardButton('Join Updates Channel', url='https://telegram.me/FayasNoushad')
        ]]
    )
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    except Exception as error:
        print(error)