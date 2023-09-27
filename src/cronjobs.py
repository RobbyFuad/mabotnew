import pytz
from datetime import time
from telegram import Update
from telegram.ext import ContextTypes


async def greetings(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=context.job.chat_id, text='''
SEMANGAT PAGII!!!
Selamat pagi semua, semangat menjalani aktivitas.
Jangan lupa senyum \U0001F60A
''')

async def pia(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=context.job.chat_id, text='''
Selamat pagi, jangan lupa isi PIA nyaa \U0001F60C ~ "kak vidya 2k23"
@Mrestuu @rifqimanufi @aditiyanID @riordrmwn @Robbyfuad @Mfikri13 @stoppiegoy @taptanisha @Utarinw

Yang gapunya PIA, isi dompetku juga gapapa
@aimmatulazra @ZAlvian16 @stmrym1
''')

async def notifyus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    name = update.effective_chat.full_name
    await context.bot.send_message(
        chat_id=chat_id,
        text='Schedule notifications activated'
    )
    context.job_queue.run_daily(pia,
                                time=time(hour=9, minute=00,tzinfo=pytz.timezone('Asia/Jakarta')),
                                days=([1,5]),
                                data=name,
                                chat_id=chat_id)
    context.job_queue.run_daily(greetings,
                                time=time(hour=9, minute=0 ,tzinfo=pytz.timezone('Asia/Jakarta')),
                                days=([1, 2, 3, 4, 5]),
                                data=name,
                                chat_id=chat_id)

async def cron_pia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    name = update.effective_chat.full_name
    await context.bot.send_message(
        chat_id=chat_id,
        text='Cronjob for PIA notification has been set'
    )
    context.job_queue.run_daily(pia,
                                time=time(hour=9, minute=00,tzinfo=pytz.timezone('Asia/Jakarta')),
                                days=([1,5]),
                                data=name,
                                chat_id=chat_id)

async def cron_greetings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    name = update.effective_chat.full_name
    await context.bot.send_message(
        chat_id=chat_id,
        text='Cronjob for greetings notification has been set'
    )
    context.job_queue.run_daily(greetings,
                                time=time(hour=9, minute=0 ,tzinfo=pytz.timezone('Asia/Jakarta')),
                                days=([1, 2, 3, 4, 5]),
                                data=name,
                                chat_id=chat_id)
