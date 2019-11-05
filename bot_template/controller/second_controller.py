import json

from telegram.ext import ConversationHandler, RegexHandler, run_async, MessageHandler, Filters

from ..constants import Buttons
from ..controller import MainController
from ..view import ScondView


class SampleController(MainController):

    def __init__(self, dispatcher):
        super().__init__(dispatcher)
        self.states = {
            'second': 0,
        }

        self.dispatcher = dispatcher
        self.sample_view = ScondView(bot=dispatcher.bot)
        self.__process_handlers()

    def first(self, bot, update):
        chat_id = update.message.chat_id
        self.sample_view.send_scond_message(chat_id)
        return self.states['first']

    def second(self, bot, update):

        chat_id = update.message.chat_id
        self.sample_view.send_scond_message(chat_id=chat_id)
        ConversationHandler.END

    def __process_handlers(self):
        conversation_handler = ConversationHandler(
            entry_points=[RegexHandler(pattern=Buttons.sample_button, callback=self.first)],
            states={
                self.states['second']: self.default_handlers + [
                    MessageHandler(Filters.text, callback=self.second)
                ],

            },
            fallbacks=[],
            allow_reentry=True
        )
        self.dispatcher.add_handler(conversation_handler)
