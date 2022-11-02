#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "YukkiMusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "تم يغالي"
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        try:
            await self.set_bot_commands([
    BotCommand("start", "رسالة البدء"),
    BotCommand("ping", "لقياس سرعة النت"),
    BotCommand("play", "لتشغيل اغنية في المجموعة"),
    BotCommand("skip", "لتخطي الأغنية الحالية"),
    BotCommand("mute", "لكتم الأغنية"),
    BotCommand("unmute", "لألغاء كتم الأغنية"),
    BotCommand("stop", "لأنهاء التشغيل"),
    BotCommand("song", "لتحميل أغنية او فلم"),
    BotCommand("sudolist", "لطلب مساعدة المطور"),
    BotCommand("settings", "لعرض أعدادات البوت")])
        except:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Please promote Bot as Admin in Logger Group"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
