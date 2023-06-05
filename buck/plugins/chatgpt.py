from telethon import events
from .. import bot
import asyncio
import openai
openai_key="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"
@bot.on(events.NewMessage(incoming=True,pattern="(?i)/ask"))
async def _gpt(event):
  if event.sender_id == int(5766936046):
    await event.reply("Buck bot")
  else:
      await event.reply("Buck bot")