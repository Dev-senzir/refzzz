import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)


@app.on_callback_query(filters.regex("ssq"))
async def fft(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .](https://t.me/so_alfaa)\n\n[❍ | 𝐋𝐮𝐫𝐚 𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐒𝐨𝐮𝐫𝐜𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞 .](https://t.me/so_alfaa)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/so_alfaa)""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "࿈ ժᥱ᥎ ᥉ᥲ️ɾᥡ᥆ .", url=f"https://t.me/C_V_R"),
                    InlineKeyboardButton(
                        "࿈ ժᥱ᥎ ᥲ️᥎ᥲ️َƚᥲ️𝗋 .", url=f"https://t.me/U_K_D")
                ],[
                    InlineKeyboardButton(
                        "࿈ ժᥱ᥎ ꪔᥲ️ժᎥ᥉᥆ꪀ .", url=f"https://t.me/MaDyY_y"),
                ],[
                    InlineKeyboardButton(
                        "࿈ ᥉᥆υɾᥴᥱ ᥣυɾᥲ️ .", url=f"https://t.me/so_alfaa"),
                    InlineKeyboardButton(
                        "࿈ ᥉υρρ᥆ɾƚ ᥣυɾᥲ️ .", url=f"https://t.me/LURA205")
                ],[
                    InlineKeyboardButton(
                        "࿈ Ⴆᥲ️ᥴk .", callback_data="settingsback_helper"),
               ],
          ]
        ),
    )
