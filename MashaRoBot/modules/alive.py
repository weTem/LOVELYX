# COPYRIGHT (C) 2021 BY LEGENDX2222 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
                 MADE BY LEGENDX22 AND PROBOYX
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
PHOTO = "https://telegra.ph/file/bf5222d53da56fe688603.jpg"
@register(pattern=("/alive"))
async def awake(event):
  lovely = event.sender.first_name
  LOVELY = "HELLO THIS IS LOVELY \n\n"
  LOVELY += "ALL SYSTEM WORKING PROPERLY\n\n"
  LOVELY += "GRAND OS : 3.8 LATEST\n\n"
  LOVELY += f"MY MASTER {V3DMATOWNER} ☺️\n\n"
  LOVELY += "FULLY UPDATED\n\n"
  LOVELY += "TELETHON : 1.19.5 LATEST\n\n"
  LOVELY += "THANKS FOR ADD ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/V3DMATOWNER"), Button.url("DEVLOPER", "https://t.me/ABOUTVEDMAT")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX22")))
async def callback_query_handler(event):
# inline by LEGENDX2222 and PROBOYX🔥
  LOVELY = [[Button.url("REPO-LOVELY", "https://github.com/attitudeking1/EMCEE"), Button.url("REPO-LOVELY", "https://github.com/attitudeking1/EMCEE")]]
  LOVELY +=[[Button.url("SUPPORT CHANNEL", "https://t.me/SHAYRI_OF_LOVES"), Button.url("SUPPORT GROUP", "https://t.me/LOVELYSUPPORTS")]]
  LOVELY +=[[custom.Button.inline("ALIVE", data="LOVELY")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=LOVELY)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  lovely = event.sender.first_name
  LOVELY = "HELLO THIS IS LOVELY \n\n"
  LOVELY += "ALL SYSTEM WORKING PROPERLY\n\n"
  LOVELY += "GRAND OS : 3.8 LATEST\n\n"
  LOVELY += f"MY MASTER {V3DMATOWNER} ☺️\n\n"
  LOVELY += "FULLY UPDATED\n\n"
  LOVELY += "TELETHON : 1.19.5 LATEST\n\n"
  LOVELY += "THANKS FOR ADD ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/V3DMATOWNER"), Button.url("DEVLOPER", "https://t.me/ABOUTVEDMAT")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF LOVELY", buttons=[[Button.url("REPO", "https://t.me/ABOUTVEDMAT")]])
# PROBOYX 🔥 LEGENDX2222

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "ALIVE"
