from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
import logging
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://pia.telkomsigma.co.id',
    'Referer': 'https://pia.telkomsigma.co.id/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

LOGIN, GETINFO, FILLPIA = range(3)


async def dev2_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [["login", "not"]]

    await update.message.reply_text(
        "use this format email|password"
        # reply_markup=ReplyKeyboardMarkup(
        #     reply_keyboard,
        #     one_time_keyboard=True,
        #     input_field_placeholder="Boy or Girl?"
        # ),
    )

    return LOGIN

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    if '|' in update.message.text:
    
        text = update.message.text.split('|')
        json_data = {
            'email': text[0],
            'password': text[1],
        }
        response = requests.post('https://apigw.telkomsigma.co.id/pia/apiPrd/auth/', headers=headers, json=json_data)
        result = response.json()
        if result['status'] == 200:
            headers['Authorization'] = f'Bearer {result["token"]}'
            await update.message.reply_text(
                f'login {result["message"]}',
                reply_markup=ReplyKeyboardRemove()
            )
        # await update.message.reply_text(
        #     f'login {result["message"]}',
        #     reply_markup=ReplyKeyboardRemove()
        # )
        response_info = requests.get('https://apigw.telkomsigma.co.id/pia/apiPrd/timesheet/my_task/', headers=headers)
        print(response_info.json())
        result_info = response_info.json()['results']
        answer = ""
        for i in range(len(result_info)):
            if result_info[i]['TASK_STATUS'] == 'ongoing':
                answer = answer+f'''
{result_info[i]['IWO_NO']}
{result_info[i]['PROJECT_NAME']}
{result_info[i]['TASK_ID']}
Task Progress: {result_info[i]['TASK_PROGRESS']}% | {result_info[i]['PLAN_PROGRESS']:.2f}% | {result_info[i]['LAST_PROGRESS']}%
'''
        await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
    # else:
    #     pass
    return GETINFO

async def getInfo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive("user_photo.jpg")
    logger.info("Photo of %s: %s", user.first_name, "user_photo.jpg")
    await update.message.reply_text(
        "Gorgeous! Now, send me your location please, or send /skip if you don't want to."
    )

    return FILLPIA
#     if result['status'] == 200:
#         headers['Authorization'] = f'Bearer {result["token"]}'
#         await update.message.reply_text(
#             f'login {result["message"]}',
#             reply_markup=ReplyKeyboardRemove()
#         )
#         response_info = requests.get('https://apigw.telkomsigma.co.id/pia/apiPrd/timesheet/my_task/', headers=headers)
#         result_info = response_info.json()['results']
#         answer = ""
#         for i in range(len(result_info)):
#             if result_info[i]['TASK_STATUS'] == 'ongoing':
#                 answer = answer+f'''
# {result_info[i]['IWO_NO']}
# {result_info[i]['PROJECT_NAME']}
# {result_info[i]['TASK_ID']}
# Task Progress: {result_info[i]['TASK_PROGRESS']}% | {result_info[i]['PLAN_PROGRESS']:.2f}% | {result_info[i]['LAST_PROGRESS']}%
# '''
#         await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
#     else:
#         await update.message.reply_text(
#             result['message'][0]+result['message'][1],
#             reply_markup=ReplyKeyboardRemove()
#         )
        
#     return PHOTO





async def skip_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the photo and asks for a location."""
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    await update.message.reply_text(
        "I bet you look great! Now, send me your location please, or send /skip."
    )

    return LOCATION


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    await update.message.reply_text(
        "Maybe I can visit you sometime! At last, tell me something about yourself."
    )

    return BIO


async def skip_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the location and asks for info about the user."""
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    await update.message.reply_text(
        "You seem a bit paranoid! At last, tell me something about yourself."
    )

    return BIO


async def bio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text("Thank you! I hope we can talk again some day.")

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


# def main() -> None:
#     """Run the bot."""
#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token("TOKEN").build()

#     # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states={
#             GENDER: [MessageHandler(filters.Regex("^(Boy|Girl|Other)$"), gender)],
#             PHOTO: [MessageHandler(filters.PHOTO, photo), CommandHandler("skip", skip_photo)],
#             LOCATION: [
#                 MessageHandler(filters.LOCATION, location),
#                 CommandHandler("skip", skip_location),
#             ],
#             BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bio)],
#         },
#         fallbacks=[CommandHandler("cancel", cancel)],
#     )

#     application.add_handler(conv_handler)

#     # Run the bot until the user presses Ctrl-C
#     application.run_polling(allowed_updates=Update.ALL_TYPES)


# if __name__ == "__main__":
#     main()