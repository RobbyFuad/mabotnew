import requests
import os
from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')

async def searcher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text[1:]
    # using the first page
    page = 1
    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start, (page=2) => (start=11), (page=3) => (start=21)
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    
    # make the API request
    data = requests.get(url).json()
    
    # get the result items
    search_items = data.get("items")
    # iterate over 10 results found
    answer = ""
    for i, search_item in enumerate(search_items, start=1):
        if i!=4:
            try:
                long_description = search_item["pagemap"]["metatags"][0]["og:description"]
            except KeyError:
                long_description = "N/A"
            # get the page title
            title = search_item.get("title")
            # page snippet
            snippet = search_item.get("snippet")
            # alternatively, you can get the HTML snippet (bolded keywords)
            # html_snippet = search_item.get("htmlSnippet")
            # extract the page url
            link = search_item.get("link")
            # print the results
            answer = answer+f'''
{"="*5}Result #{i+start-1}{"="*5}
Title: {title}
Description: {snippet}
URL: {link}
'''
# Long description: {long_description}
        else:
            break
    # resp = get_search(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)