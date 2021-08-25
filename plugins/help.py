from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f" Just Send Youtube link and i will download it"
    await message.reply_text(helptxt)
