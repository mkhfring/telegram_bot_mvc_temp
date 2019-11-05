def add_handlers(dispatcher, handlers):
    for handler in handlers:
        dispatcher.add_handler(handler)