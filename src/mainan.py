from telegram import Update, constants
from telegram.ext import ContextTypes
from functools import wraps
from src.config import SPECIAL_USERS
import openai
import time
import urllib.request
print('  ')

async def spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt= ' '.join(update.message.text.split()[1:])
    if '@'+update.effective_user.username == '@Robbyfuad':
        while True:
            await context.bot.send_message(chat_id = update.message.chat_id, text=prompt)
    else:
        await update.message.reply_text(text='''
You're not allowed to access this feature \U0000274c\U0000274c\U0000274c.
''')