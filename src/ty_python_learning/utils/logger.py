import os
import logging
from logging.handlers import TimedRotatingFileHandler

from src.ty_python_learning.utils.yaml_reader import CONFIG, LOGS_PATH


class Logger(object):
    def __init__(self):
        os.path.dirname(__file__)
        self.logger = logging.getLogger('autoTest_project')
        logging.root.setLevel(logging.INFO)
        c = CONFIG.get('logs')
        self.log_file_name = c['filename'] if c.get('filename') else 'test_py.log'
        self.backup_count = c['backup_files_count'] if c.get('backup_files_count') else 5
        self.console_output_level = c['console_output_level'] if c.get('console_output_level') else 'DEBUG'
        self.file_output_level = c['file_output_level'] if c.get('file_output_level') else 'WARNING'
        pattern = "%(asctime)s-%(funcName)s-%(levelname)s- %(message)s"
        self.formatter = logging.Formatter(pattern, datefmt='%Y-%m-%d %H:%M:%S')
        self.init_handlers()

    # add handlers in logger, if existed, return directly
    # to avoid record the same log
    def init_handlers(self):
        if self.logger.handlers:
            return

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)
        console_handler.setLevel(self.console_output_level)
        self.logger.addHandler(console_handler)

        # create log file every interval D, and save backupCount day(s)
        file_name_ = os.path.join(LOGS_PATH, self.log_file_name)
        file_handler = TimedRotatingFileHandler(file_name_,
                                                when='D',
                                                interval=1,
                                                backupCount=self.backup_count,
                                                delay=True,
                                                encoding='utf-8')
        file_handler.setFormatter(self.formatter)
        file_handler.setLevel(self.file_output_level)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger


logger = Logger().get_logger()
