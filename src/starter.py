from telegram import Update, Dice, constants
from telegram.ext import CallbackContext, ContextTypes
L = '\033[0;0m'
WW = '\33[5;31;42m'
GRY = '\033[90m'
RED = '\033[31m'
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("{WW} How May I Help You? {L}  \U0001F60A \U00002B1B \U0001F7E5 \U0001F7E6 \U0001F7E9 \U0001F7E8 \U0001F7EB \U0001F7E7")
    # \U00002B1D \U00002B1B \U00001F7E5 \U00001F7E6 \U00001F7E9 \U00001F7E8 \U00001F7EB \U00001F7E7


async def evilbot(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Give bot for admin, and miracle will come \U0001F608 \U0001F608 \U0001F608")

async def userinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'''
id: {update.effective_user.id}
first name: {update.effective_user.first_name}
username: @{update.effective_user.username}
''')

async def game(update: Update, context: CallbackContext) -> None:
    games = Dice(64, constants.DiceEmoji.SLOT_MACHINE)
    await update.message.reply_text(reply_markup=games)
