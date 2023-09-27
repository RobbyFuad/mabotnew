from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

async def linkzoom(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('''
Zoom Banyak Breakout :
https://us02web.zoom.us/j/88611861878?pwd=Q08xblpTdlJCR0c2Tm5YWjFjWDBhdz09\n
Zoom Telkomsel :
https://telkomsel.zoom.us/j/96851614403?pwd=OXhqWHZhejFzN3Z6T1FOT0lQb2dIQT09
''')

async def pasi(update: Update, context: CallbackContext) -> None:
    await update.message.reply_voice(voice='src/kauni.opus', duration=15)
