import inspect


from retrying import retry

from ..logger import Logger


logger = Logger.get_logger()


class MessageSender:
    def __init__(self, bot):
        self.bot = bot

    @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_delay=30000)
    def send_message(self, chat_id, text, reply_markup=None):
        try:
            self.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)
        except Exception as e:
            logger.error(inspect.stack()[1][3] + "\nmessage is not send.\n" + str(e))
