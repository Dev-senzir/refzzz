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



@app.on_callback_query(filters.regex("madisontg"))
async def madisetting(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""✅ اليك قائمة اوامر سورس لورا .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n\n✅ قائمه الاوامر تحتوي علي 6 اوامر .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n1 ← اوامر التشغيل .\n2 ← اوامر القنوات .\n3 ← اوامر مطور البوت .\n4 ← مميزات السورس .\n5 ← اوامر البوت .\n6 ← اوامر الادمن .""",
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

@app.on_callback_query(filters.regex("madison5"))
async def mad55(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .](https://t.me/so_alfaa)\n\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n✅ اليك قائمة اوامر البوت ,\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لعرض سرعه البوت اكتب : بينج .\n- للتحكم في لغه البوت اكتب : اللغه .\n- للتحكم في ازار التشغيل اكتب : وضع شغل .\n- لعرض اعدادات البوت اكتب : الاعدادات .\n\n- ثانيا اليك اوامر الرتب .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لرفع ادمن في الجروب اكتب : ر ا د .\n- لرفع ادمن في الجروب اكتب : ت ا د .\n- لعرض قائمه الادمنيه اكتب : ق ا د .\n- لرفع مطور ثانوي اكتب : ر م ث .\n- لتنزيل مطور ثانوي اكتب : ت م ث .\n- لعرض قائمه الثانوين اكتب : ق م ث .\n\n- ثالثا اليك اوامر الحظر .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لحظر عضو من الجروب اكتب : ح ر .\n- لالغاء حظر عضو من الجروب اكتب : ا ر .\n- لعرض قائمه المحظورين اكتب : ق ح ر .\n- لحظر عضو عام من الجروب اكتب : ح ع .\n- لالغاء حظر عضو عام من الجروب اكتب : ا ر .\n- لعرض قائمه المحظورين عام اكتب : ق ح ع .""",       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "࿈ اوامر التشغيل .", callback_data=f"madison1"),
                    InlineKeyboardButton(
                        "࿈ اوامر القنوات .", callback_data=f"madison2"),
                ],[
                    InlineKeyboardButton(
                        "࿈ اوامر مطور البوت .", callback_data=f"madison2"),
                    InlineKeyboardButton(
                        "࿈ مميزات السورس .", callback_data=f"madison4"),
                ],[
                    InlineKeyboardButton(
                        "࿈ اوامر الادمن .", callback_data=f"madison6"),
                ],[
                    InlineKeyboardButton(
                        "࿈ Ⴆᥲ️ᥴk .", callback_data="madisontg"),
                ],[
                    InlineKeyboardButton(
                        "࿈ ᥉᥆υɾᥴᥱ ᥣυɾᥲ️ .", url=f"https://t.me/so_alfaa"),

            ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("madison6"))
async def mad66(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .](https://t.me/so_alfaa)\n\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n✅ اليك قائمة اوامر الادمن ,\n\n- جميع الاوامر خاصه ب الادمن فقط .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لعرض سرعه البوت اكتب : بينج .\n- للتحكم في لغه البوت اكتب : اللغه .\n- للتحكم في ازار التشغيل اكتب : وضع شغل .\n- لعرض اعدادات البوت اكتب : الاعدادات .\n\n- ثانيا اليك اوامر الرتب .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لرفع ادمن في الجروب اكتب : ر ا د .\n- لرفع ادمن في الجروب اكتب : ت ا د .\n- لعرض قائمه الادمنيه اكتب : ق ا د .\n\n- ثالثا اليك اوامر الحظر .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لحظر عضو من الجروب اكتب : ح ر .\n- لالغاء حظر عضو من الجروب اكتب : ا ر .\n- لعرض قائمه المحظورين اكتب : ق ح ر .""",       reply_markup=InlineKeyboardMarkup(
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
                ],[
                    InlineKeyboardButton(
                        "࿈ Ⴆᥲ️ᥴk .", callback_data="madisontg"),
                ],[
                    InlineKeyboardButton(
                        "࿈ ᥉᥆υɾᥴᥱ ᥣυɾᥲ️ .", url=f"https://t.me/so_alfaa"),

            ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("madison4"))
async def mad44(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .](https://t.me/so_alfaa)\n\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n✅ اليك قائمة مميزات السورس ,\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n✅ هذه قائمه مميزات سورس لورا الميوزك .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لعرض اوامر البوت اكتب : الاوامر .\n- لعرض كليشه السورس اكتب : سورس لورا .\n- لعرض مطور البوت اكتب : المطور .\n- لعرض اسم البوت اكتب : البوت .\n- لعرض الايدي الخاص بك وصورتك اكتب : ا .\n\n✅ اولا قائمة اوامر البوت ,\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لعمل اذاعه في البوت اعمل ريبلاي علي الاذاعه واكتب : اذاعه .\n- لعرض سرعه البوت اكتب : بينج .\n- للتحكم في لغه البوت اكتب : اللغه .\n- للتحكم في ازار التشغيل اكتب : وضع شغل .\n- لعرض اعدادات البوت اكتب : الاعدادات .\n\n✅ ثانيا اليك اوامر الرتب .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لرفع ادمن في الجروب اكتب : ر ا د .\n- لرفع ادمن في الجروب اكتب : ت ا د .\n- لعرض قائمه الادمنيه اكتب : ق ا د .\n\n✅ ثالثا اليك اوامر الحظر .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لحظر عضو من الجروب اكتب : ح ر .\n- لالغاء حظر عضو من الجروب اكتب : ا ر .\n- لعرض قائمه المحظورين اكتب : ق ح ر .""",       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "࿈ اوامر التشغيل .", callback_data=f"madison1"),
                    InlineKeyboardButton(
                        "࿈ اوامر القنوات .", callback_data=f"madison2"),
                ],[
                    InlineKeyboardButton(
                        "࿈ اوامر مطور البوت .", callback_data=f"madison3"),
                ],[
                    InlineKeyboardButton(
                        "࿈ اوامر البوت .", callback_data=f"madison5"),
                    InlineKeyboardButton(
                        "࿈ اوامر الادمن .", callback_data=f"madison6"),
                ],[
                    InlineKeyboardButton(
                        "࿈ Ⴆᥲ️ᥴk .", callback_data="madisontg"),
                ],[
                    InlineKeyboardButton(
                        "࿈ ᥉᥆υɾᥴᥱ ᥣυɾᥲ️ .", url=f"https://t.me/so_alfaa"),

            ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("madison2"))
async def mad22(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .](https://t.me/so_alfaa)\n\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n✅ اليك قائمة اوامر القنوات ,\n\n- اولا اليك اوامر ربط البوت ب القناة .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n لربط البوت ب القناة مالك القناة فقط يستطيع ربطه .\nلربط القناة اكتب : ربط + معرف القناة\n\n- ثانيا اليك اوامر تشغيل البوت في القناة .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لتشغيل اغنيه اكتب : ق تشغيل او ق شغل او cplay\n- لتشغيل فيديو اكتب : ق فيديو او cvideo\n- لأنهاء الاغنيه اكتب : ق ايقاف او ق انهاء او cstop\n- لايقاف الاغنيه مؤقت اكتب : ق وقف او cpause\n- لتكملة الاغنيه من الايقاف المؤقت اكتب : ق كمل او cresume\n- لتخطي الاغنيه اكتب : تخطي او cskip\n- لكتم البوت في الكول اكتب : ق اسكت او cmute\n- لألغاء كتم البوت في الكول اكتب : ق اتكلم او cunmute\n- لاعادة تشغيل البوت اكتب : /restart""",       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "࿈ اوامر التشغيل .", callback_data=f"madison1"),
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
                        "࿈ Ⴆᥲ️ᥴk .", callback_data="madisontg"),
                ],[
                    InlineKeyboardButton(
                        "࿈ ᥉᥆υɾᥴᥱ ᥣυɾᥲ️ .", url=f"https://t.me/so_alfaa"),

            ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("madison3"))
async def mad33(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .](https://t.me/so_alfaa)\n\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n✅ اليك قائمة اوامر مطور البوت ,\n\n- جميع الاوامر خاصه بمطور البوت فقط .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لعمل اذاعه في البوت اعمل ريبلاي علي الاذاعه واكتب : اذاعه .\n - لعرض احصائيات البوت اكتب : الاحصائيات .\n- لعرض سرعه البوت اكتب : بينج .\n- للتحكم في لغه البوت اكتب : اللغه .\n- للتحكم في ازار التشغيل اكتب : وضع شغل .\n- لعرض اعدادات البوت اكتب : الاعدادات .\n\n- ثانيا اليك اوامر الرتب .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لرفع ادمن في الجروب اكتب : ر ا د .\n- لرفع ادمن في الجروب اكتب : ت ا د .\n- لعرض قائمه الادمنيه اكتب : ق ا د .\n- لرفع مطور ثانوي اكتب : ر م ث .\n- لتنزيل مطور ثانوي اكتب : ت م ث .\n- لعرض قائمه الثانوين اكتب : ق م ث .\n\n- ثالثا اليك اوامر الحظر .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لحظر عضو من الجروب اكتب : ح ر .\n- لالغاء حظر عضو من الجروب اكتب : ا ر .\n- لعرض قائمه المحظورين اكتب : ق ح ر .\n- لحظر عضو عام من الجروب اكتب : ح ع .\n- لالغاء حظر عضو عام من الجروب اكتب : ا ر .\n- لعرض قائمه المحظورين عام اكتب : ق ح ع .""",       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "࿈ اوامر التشغيل .", callback_data=f"madison1"),
                    InlineKeyboardButton(
                        "࿈ اوامر القنوات .", callback_data=f"madison2"),
                ],[
                    InlineKeyboardButton(
                        "࿈ مميزات السورس .", callback_data=f"madison4"),
                ],[
                    InlineKeyboardButton(
                        "࿈ اوامر البوت .", callback_data=f"madison5"),
                    InlineKeyboardButton(
                        "࿈ اوامر الادمن .", callback_data=f"madison6"),
                ],[
                    InlineKeyboardButton(
                        "࿈ Ⴆᥲ️ᥴk .", callback_data="madisontg"),
                ],[
                    InlineKeyboardButton(
                        "࿈ ᥉᥆υɾᥴᥱ ᥣυɾᥲ️ .", url=f"https://t.me/so_alfaa"),

            ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("madison1"))
async def mad11(_, query: CallbackQuery):
   await query.edit_message_text(
          f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐮𝐫𝐚 .](https://t.me/so_alfaa)\n\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n✅ اليك قائمة اوامر التشغيل ,\n\n- اولا اليك اوامر التشغيل ف الجروب .\n•═════•| 𝙻𝚞𝚛𝚊 |•═════•\n- لتشغيل اغنيه اكتب : تشغيل او شغل او /play\n- لتشغيل فيديو اكتب : فيديو او /video\n- لأنهاء الاغنيه اكتب : ايقاف او انهاء او /stop\n- لايقاف الاغنيه مؤقت اكتب : وقف او /pause\n- لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او /resume\n- لتخطي الاغنيه اكتب : تخطي او /skip\n- لكتم البوت في الكول اكتب : اسكت او /mute\n- لألغاء كتم البوت في الكول اكتب : اتكلم او /unmute\n- لاعادة تشغيل البوت اكتب : /restart""",       reply_markup=InlineKeyboardMarkup(
          [
               [
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
                        "࿈ Ⴆᥲ️ᥴk .", callback_data="madisontg"),
                ],[
                    InlineKeyboardButton(
                        "࿈ ᥉᥆υɾᥴᥱ ᥣυɾᥲ️ .", url=f"https://t.me/so_alfaa"),

            ],
            ]
        ),
    )
