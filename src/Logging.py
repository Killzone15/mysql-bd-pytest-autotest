import inspect
import logging
import os
import datetime


def current_function_name():
    return inspect.stack()[1].function


class Logger:
    def __init__(self, logger_name, log_folder='logs', log_level=logging.INFO):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_folder = os.path.join(os.getcwd(), log_folder, current_datetime)

        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

        log_file_path = os.path.join(self.log_folder, f'{logger_name}_log.txt')
        file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
        file_handler.setLevel(log_level)

        formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_exception(self, message):
        self.logger.exception(message)


logger_test_insert_to_bd = Logger("test_insert_to_bd")
