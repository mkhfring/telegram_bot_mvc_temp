import logging
import os

HERE = os.path.dirname(os.path.realpath(__file__))


class BotConfig:
    project_root = os.path.dirname(os.path.realpath(__file__))
    prometheus_port = int(os.environ.get('PROMETHEUS_PORT', '8000'))
    token = os.environ.get(
        'BOT_TOKEN',
        '560354132:4810fa6592d53b23d61e761da6d0531ed9b5faab'
    )
    # 0:print to output        1:use graylog       2:both 0 and 1
    use_graylog = os.environ.get('SDK_USE_GRAYLOG', "1")
    source = os.environ.get('SOURCE', "vip_bot_source")
    graylog_host = os.environ.get('GRAYLOG_HOST', "127.0.0.1")
    graylog_port = int(os.environ.get('GRAYLOG_PORT', "12201"))
    log_level = int(os.environ.get('LOG_LEVEL', logging.INFO))
    log_facility_name = os.environ.get('LOG_FACILITY_NAME', "python_bale_bot")


class DbConfig:
    db_user = os.environ.get('POSTGRES_USER', 'test')
    db_password = os.environ.get('POSTGRES_PASSWORD', 'test')
    db_host = os.environ.get('POSTGRES_HOST', '192.168.32.52')
    db_name = os.environ.get('POSTGRES_DB', 'test_db')
    db_port = os.environ.get('POSTGRES_PORT', 5499)
    main_database_url = "postgresql://{}:{}@{}:{}/{}".format(
        db_user,
        db_password,
        db_host,
        db_port,
        db_name
    ) if db_name else None
    test_database_ur = 'sqlite:///{}/vip_practice_database.db'.format(HERE)
    database_url = main_database_url or test_database_ur


class LogConfig:
    receive_timeout = int(os.environ.get("SESSION_TIMEOUT", 60))
    base_url = os.environ.get('BASE_URL', "wss://api.bale.ai/v1/bots/")
    request_timeout = int(os.environ.get('REQUEST_TIMEOUT', 5))
    # 0:print to output        1:use graylog       2:both 0 and 1
    use_graylog = os.environ.get('SDK_USE_GRAYLOG', "2")
    source = os.environ.get('LOG_SOURCE', "bot_source")
    graylog_host = os.environ.get('SDK_GRAYLOG_HOST', "172.30.41.67")
    graylog_port = int(os.environ.get('SDK_GRAYLOG_PORT', 12201))
    log_level = int(os.environ.get('SDK_LOG_LEVEL', logging.DEBUG))
    log_facility_name = os.environ.get('SDK_LOG_FACILITY_NAME', "python_bale_bot")
