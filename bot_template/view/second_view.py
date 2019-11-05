import inspect

from telegram import KeyboardButton, ReplyKeyboardMarkup

from ..constants import Buttons
from ..logger import Logger
from ..view.message_sender import MessageSender


class ScondView:

    scond_message = "Socond message"

    def __init__(self, bot):
        self.bot = bot
        self.message_sender = MessageSender(bot=bot)
        self.logger = Logger.get_logger()

    def send_scond_message(self, chat_id):
        keyboard = [[
            KeyboardButton(text=Buttons.back_to_main_menu)
        ]]
        markup = ReplyKeyboardMarkup(keyboard=keyboard)
        self.message_sender.send_message(chat_id=chat_id, text=self.scond_message, reply_markup=markup)
        self.logger.info(inspect.stack()[0][3])

