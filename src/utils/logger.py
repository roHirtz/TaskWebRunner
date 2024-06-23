import sys
import traceback
from datetime import datetime
from loguru import logger as log
from src.utils.environment import Environment


class Logger:
    __instance = None
    __time = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.logger = log
        self.__time = Environment.get_environment('start_time')
        self.logger.add(f'log/{self.__time}.log', encoding='utf-8')

    def info(self, message, *args, **kwargs):
        self.logger.info(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self.logger.warning(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self.logger.error(message, *args, **kwargs)

    def success(self, message, *args, **kwargs):
        self.logger.success(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self.logger.critical(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        self.logger.debug(message, *args, **kwargs)


logger = Logger()


def log(func):
    def log_request(*args, **kwargs):
        logger.info(f'执行函数：{func.__name__}')
        if args:
            logger.info(f'执行参数：{args[1::]}')
        if kwargs:
            logger.info(f'关键字参数：{kwargs}')
        resp = func(*args, **kwargs)
        logger.info(f'执行结果为：{resp}')
        return resp

    return log_request
