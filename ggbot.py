import logging
import openai
import os
from src import *
import openai
from telegram.ext import CommandHandler, Application, MessageHandler, filters, CallbackQueryHandler, InlineQueryHandler
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')

openai.api_key = OPENAI_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    filter_img = Filter_aiimg()
    filter_user = Filter_user()
    filter_spam = Filter_spam()
    # application = Application.builder().token(BOT_TOKEN).rate_limiter(MyLimiter()).build()
    application = Application.builder().token(BOT_TOKEN).build()
    # application.add_handler(TypeHandler(Update, callback), -1)
    
    ##### Common Feature #####
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('userinfo', userinfo))
    application.add_handler(CommandHandler('linkzoom', linkzoom))
    application.add_handler(CommandHandler('game', game))
    application.add_handler(CommandHandler('notifyus', notifyus))
    application.add_handler(CommandHandler('pasi', pasi))
    application.add_handler(CommandHandler('editor', editor))
    
    #dev
    application.add_handler(CommandHandler("sstart", sstart))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(InlineQueryHandler(inline_query))
    
    ##### Special Feature #####
    application.add_handler(MessageHandler(filters.Regex(r'^!'), ai_txt))
    application.add_handler(MessageHandler(filter_img, ai_img))
    application.add_handler(MessageHandler(filter_spam, spam))
    application.add_handler(MessageHandler(filters.Regex(r'^%'), searcher))

    application.run_polling()

if __name__ == '__main__':
    main()