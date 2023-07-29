import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["ماديسون"])
    & filters.group
    & ~filters.edited
)
async def madison(client: Client, message: Message):
    usr = await client.get_users(2059448162)
    name = usr.first_name
    async for photo in client.iter_profile_photos(2059448162, limit=1):
                    await message.reply_photo(photo.file_id,
        caption=f"""- مرحبا بك عزيزي {message.from_user.mention}\n\n- للتواصل مع المبرمج ماديسون .\n\n- اتبع الازرار التاليه .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/MaDyY_y"),
                ],
            ]
        ),
    )
