from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from telegram.ext.filters import UpdateFilter
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from html import escape
from uuid import uuid4


class Filter_user(UpdateFilter):
    async def filter(self, update: Update):
        if '@'+update.effective_user.username in SPECIAL_USERS:
            pass
        else:
            await update.effective_message.reply_text('''
You're not allowed to access this bot \U0000274c\U0000274c\U0000274c.
please contact @Robbyfuad first!!.
''')
            raise ApplicationHandlerStop
        
async def editor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.edit_message_text(
        chat_id = -1001949245558,
        message_id = 20, text=f'''
sudah diedit
''')
    # idnya : {update.effective_message.id}
    
# async def editor(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=f'''
# id-nya: {update.effective_message.id}
# dan : {update.effective_chat.id}
# ''')

    
async def sstart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    query = update.inline_query.query

    if query == "":
        return

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper()),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Bold",
            input_message_content=InputTextMessageContent(
                f"<b>{escape(query)}</b>", parse_mode=ParseMode.HTML
            ),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Italic",
            input_message_content=InputTextMessageContent(
                f"<i>{escape(query)}</i>", parse_mode=ParseMode.HTML
            ),
        ),
    ]

    await update.inline_query.answer(results)