import inspect

from ..constants import Buttons
from telegram import KeyboardButton, ReplyKeyboardMarkup

from ..logger import Logger
from .message_sender import MessageSender


class MainView:
    greeting_message = "Welcome to my bot"

    def __init__(self, bot):
        self.bot = bot
        self.message_sender = MessageSender(bot=bot)
        self.logger = Logger.get_logger()

    def send_greeting_message(self, chat_id):
        keyboard = [[
            KeyboardButton(text=Buttons.back_to_main_menu),
            KeyboardButton(text=Buttons.sample_button),
        ]]
        markup = ReplyKeyboardMarkup(keyboard=keyboard)
        self.message_sender.send_message(chat_id=chat_id, text=self.greeting_message, reply_markup=markup)
        self.logger.info(inspect.stack()[0][3])
