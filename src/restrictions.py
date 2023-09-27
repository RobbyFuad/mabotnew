from telegram import Update
from telegram.ext import ContextTypes, ApplicationHandlerStop, TypeHandler


async def restrict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='''
You're not allowed to access this bot \U0000274c\U0000274c\U0000274c.
please contact @Robbyfuad first!!.
'''
    )

async def restrict2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='''
You're not allowed to access this command \U0000274c\U0000274c\U0000274c.
'''
    )

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if '@'+update.effective_user.username in SPECIAL_USERS:
        pass
    else:
        await update.effective_message.reply_text('''
You're not allowed to access this bot \U0000274c\U0000274c\U0000274c.
please contact @Robbyfuad first!!.
''')
        raise ApplicationHandlerStop
