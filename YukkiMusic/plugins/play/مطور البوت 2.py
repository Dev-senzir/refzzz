import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from YukkiMusic.misc import SUDOERS

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

IMG_DEV1 = getenv("IMG_DEV1")

OWNER = getenv("OWNER")

BOTID = getenv("BOTID")




def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj



@app.on_message(
    command(["غنغعنغعىال","ئئئئئئئئئئئئئئئءءء","ضضضضضضضضضضضضضضضضضضضثثثثثثثثثثث","دددددددجججججججججججججج","اااااااااااااا","مطور"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(BOTID)
    name = usr.first_name
    async for photo in client.iter_profile_photos(BOTID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""❲ ժᥱ᥎ᥱᥣ᥆ρᥱᖇ᥉ Ⴆ᥆ƚ ❳
— — — — — — — — —
࿈ ժᥱ᥎ ꪀᥲ️ꪔᥱ : [{usr.first_name}](https://t.me/{OWNER})
࿈ ժᥱ᥎ υ᥉ᥱᖇ : @{OWNER}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{OWNER}")
                ],[
                    InlineKeyboardButton(
                        "࿈ ضيف البوت لمجموعتك .", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
    )
