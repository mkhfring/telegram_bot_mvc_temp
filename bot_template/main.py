from telegram.ext import Updater

from bot_template.controller import MainController, SampleController
from bot_template.database import Base, engine
from bot_template.main_config import BotConfig
from bot_template.utils import add_handlers

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    updater = Updater(
        token=BotConfig.token,
        base_url='https://tapi.bale.ai/',
        request_kwargs={'read_timeout': 60, 'connect_timeout': 60}
    )

    dispatcher = updater.dispatcher
    main_controller = MainController(dispatcher=dispatcher)
    token_controller = SampleController(dispatcher=dispatcher)
    add_handlers(dispatcher=dispatcher, handlers=main_controller.default_handlers)
    updater.start_polling(poll_interval=1)
    updater.idle()