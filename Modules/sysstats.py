# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import platform
import re
import socket
import uuid
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.__version__ import __version__ as pytgver

from FallenMusic import BOT_NAME, SUDOERS, app
from FallenMusic.Modules import ALL_MODULES


@app.on_message(filters.command(["stats", "sysstats"]) | filters.command(["الحاله","الاحصائيات"],prefixes= ["/", "!","","#"]) & SUDOERS)
async def sys_stats(_, message: Message):
    sysrep = await message.reply_text(
        f"ɢᴇᴛᴛɪɴɢ {BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs, ɪᴛ'ʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0  𓆚  𓆚3))) + " ɢʙ"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0  𓆚  𓆚3)
    total = str(total)
    used = hdd.used / (1024.0  𓆚  𓆚3)
    used = str(used)
    free = hdd.free / (1024.0  𓆚  𓆚3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
🎧 <u>  𓆚  𓆚{BOT_NAME} احصائيات النظام   𓆚  𓆚</u>

  𓆚  𓆚بايثون :  𓆚  𓆚 {pyver.split()[0]}
  𓆚  𓆚بايروجرام :  𓆚  𓆚 {pyrover}
  𓆚  𓆚مكالمات بي تي جي :  𓆚  𓆚 {pytgver}
  𓆚  𓆚سودورز :  𓆚  𓆚 `{sudoers}`
  𓆚  𓆚الوحدات :  𓆚  𓆚 `{mod}`

  𓆚  𓆚الايبي :  𓆚  𓆚 {ip_address}
  𓆚  𓆚ماك :  𓆚  𓆚 {mac_address}
  𓆚  𓆚اسم المضيف :  𓆚  𓆚 {hostname}
  𓆚  𓆚منصة :  𓆚  𓆚 {sp}
  𓆚  𓆚المعالج :  𓆚  𓆚 {processor}
  𓆚  𓆚بنيان :  𓆚  𓆚 {architecture}
  𓆚  𓆚إصدار المنصة :  𓆚  𓆚 {platform_release}
  𓆚  𓆚إصدار المنصة :  𓆚  𓆚 {platform_version}

        <b><u>sᴛᴏʀᴀɢᴇ</b><u/>
  𓆚  𓆚متاح :  𓆚  𓆚 {total[:4]} ɢɪʙ
  𓆚  𓆚مستخدم :  𓆚  𓆚 {used[:4]} ɢɪʙ
  𓆚  𓆚حر :  𓆚  𓆚 {free[:4]} ɢɪʙ

  𓆚  𓆚رام :  𓆚  𓆚 {ram}
  𓆚  𓆚النوى المادية :  𓆚  𓆚 {p_core}
  𓆚  𓆚مجموع النوى :  𓆚  𓆚 {t_core}
  𓆚  𓆚تردد وحدة المعالجة المركزية :  𓆚  𓆚 {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="مسح",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )
