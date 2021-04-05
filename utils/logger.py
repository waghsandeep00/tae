import logging
import sys
from logging import Logger

execution_logging_format = "%(asctime)s - %(name)s- %(levelname)s - %(message)s"

class LOGGER(Logger):

    log_instance = None
    def __init__(
            self, log_file=None, logger_name="execution", *args, **kwargs):
        Logger.__init__(self, logger_name, *args, **kwargs)
        log_format = execution_logging_format
        self.log_file = log_file
        self.formatter = logging.Formatter(log_format)
        self.addHandler(self.get_console_handler())
        if log_file:
            self.addHandler(self.get_file_handler())
        self.propagate = False

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def get_file_handler(self):
        file_hanlder = logging.FileHandler(filename=self.log_file)
        file_hanlder.setFormatter(self.formatter)
        return file_hanlder

    @staticmethod
    def set_logger(log_file='', logger_name='execution'):
        logging.setLoggerClass(LOGGER)
        LOGGER.log_instance = LOGGER(log_file=log_file, logger_name=logger_name)

    @staticmethod
    def get_logger():
        return LOGGER.log_instance