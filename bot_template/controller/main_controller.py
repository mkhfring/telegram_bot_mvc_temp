from telegram.ext import ConversationHandler, CommandHandler, RegexHandler, MessageHandler

from ..constants import Buttons
from ..logger import Logger
from ..view.main_view import MainView


class MainController:

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.main_view = MainView(bot=dispatcher.bot)
        self.default_handlers = [
            CommandHandler(command="start", callback=self.main_menu),
            RegexHandler(pattern=Buttons.back_to_main_menu, callback=self.main_menu),
        ]
        self.logger = Logger.get_logger()
        self.__process_handlers()

    def main_menu(self, bot, update):
        chat_id = update.message.chat_id
        self.main_view.send_greeting_message(chat_id)

    def __process_handlers(self):
        # self.dispatcher.add_handler(CommandHandler(command="start", callback=self.main_menu))
        pass
