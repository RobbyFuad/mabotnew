from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext.filters import UpdateFilter
from src.config import SPECIAL_USERS

class Filter_aiimg(UpdateFilter):
    def filter(self, update: Update):
        if 'gbr' == update.message.text.split()[0]:
            return True
        
class Filter_spam(UpdateFilter):
    def filter(self, update: Update):
        if '.xxx' == update.message.text.split()[0]:
            return True
    