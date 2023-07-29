import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(
    command(["الاوامر","اوامر"])
    & filters.group
    & ~filters.edited
)
async def madison(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c9a64be70b3bbca7b5dda.jpg",
        caption=f"""✅ مرحبا بك عزيزي {message.from_user.mention}\n\n✅ اليك قائمة اوامر سورس لورا .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n\n✅ قائمه الاوامر تحتوي علي 6 اوامر .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n1 ← اوامر التشغيل .\n2 ← اوامر القنوات .\n3 ← اوامر مطور البوت .\n4 ← مميزات السورس .\n5 ← اوامر البوت .\n6 ← اوامر الادمن .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "࿈ اوامر التشغيل .", callback_data=f"madison1"),
                    InlineKeyboardButton(
                        "࿈ اوامر القنوات .", callback_data=f"madison2"),
                ],[
                    InlineKeyboardButton(
                        "࿈ اوامر مطور البوت .", callback_data=f"madison3"),
                    InlineKeyboardButton(
                        "࿈ مميزات السورس .", callback_data=f"madison4"),
                ],[
                    InlineKeyboardButton(
                        "࿈ اوامر البوت .", callback_data=f"madison5"),
                    InlineKeyboardButton(
                        "࿈ اوامر الادمن .", callback_data=f"madison6"),
                ],[
                    InlineKeyboardButton(
                        "࿈ ᥉᥆υɾᥴᥱ ᥣυɾᥲ️ .", url=f"https://t.me/so_alfaa"),
                ],
            ]
        ),
    )

