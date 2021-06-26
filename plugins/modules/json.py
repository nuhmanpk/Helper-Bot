from pyrogram import Client, filters
from io import BytesIO

@Client.on_message(filters.command(["json"]))
async def group(bot, update):
    json = update.reply_to_message
    with BytesIO(str.encode(str(json))) as json_file:
        json_file.name = "json.text"
        await json.reply_document(
            document=json_file,
            reply_markup=JSON_BUTTON
        )