from telethon import TelegramClient
import logging
import time
openai_key="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"


api_id="1125689"
api_hash="4772d1792ed194020a8fb06a91ffb8fa"
bot_token="5963395579:AAHf6N1WOkXTxRzQGNmX2EEm368J3KHFBxM"

bot=TelegramClient("Gattuu_bot",api_id,api_hash).start(bot_token=bot_token)