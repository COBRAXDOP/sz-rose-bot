import os
from pyrogram import Client, filters
from pyrogram.types import *

from DewmiBot.config import get_str_key
from DewmiBot import pbot

REPO_TEXT = "**A Powerful BOT to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 @XD_LIF 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Resently\n╰──────────────\n\n»»» @AlizaProBot «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("Repository", url=f"https://t.me/Xd_lif"),
        InlineKeyboardButton("Video info ", url=f"https://t.me/L0VEXWORLD"),
      ],[
        InlineKeyboardButton("Support ", url="https://t.me/MISTY_SUPORTER"),
        InlineKeyboardButton("Update", url="https://t.me/MISTY_SUPORT"),
      ],[
        InlineKeyboardButton("Aliza update info", url="https://t.me/MISTY_SUPORT"),
        InlineKeyboardButton("Developer", url="https://t.me/XD_LIF"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
