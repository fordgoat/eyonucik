from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app


start_txt = """
hi
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("owner", url="https://t.me/myodiseans"),
          InlineKeyboardButton("repo", url="https://t.me/FordPedia"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/S7U.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
