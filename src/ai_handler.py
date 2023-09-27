from telegram import Update, constants
from telegram.ext import ContextTypes
from functools import wraps
from src.config import SPECIAL_USERS
import openai
import time
import urllib.request


def send_action(action):
    """Sends `action` while processing func command."""
    def decorator(func):
        @wraps(func)
        async def command_func(update, context, *args, **kwargs):
            await context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return await func(update, context,  *args, **kwargs)
        return command_func
    return decorator

@send_action(constants.ChatAction.TYPING)
async def ai_txt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=update.message.text,
            temperature=0,
            max_tokens=1000
            )
        resp = response['choices'][0]['text']
        if '@'+update.effective_user.username in SPECIAL_USERS:
            await update.message.reply_text(text=resp)
        else:
            await update.message.reply_text(text='''
You're not allowed to access this feature \U0000274c\U0000274c\U0000274c.
''')
    
    except openai.error.OpenAIError as e:
        await update.message.reply_text(text=e.error['message'])
        
    
@send_action(constants.ChatAction.UPLOAD_PHOTO)
async def ai_img(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = openai.Image.create(
            prompt= ' '.join(update.message.text.split()[1:]),
            n=1,
            size='1024x1024')
        resp = response['data'][0]['url']
        urllib.request.urlretrieve(resp, 'res.jpg')
        with open('res.jpg', 'rb') as f:
            if '@'+update.effective_user.username in SPECIAL_USERS:
                time.sleep(3)
                await update.message.reply_photo(photo='res.jpg')
            else:
                await update.message.reply_text(text='''
You're not allowed to access this feature \U0000274c\U0000274c\U0000274c.
''')
    except openai.error.OpenAIError as e:
        await update.message.reply_text(text=e.error['message'])