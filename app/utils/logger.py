import logging

from app.config import Config


def encode_msg(msg: str) -> str:
    return msg.encode('utf-8', 'replace').decode('utf-8')


class ColoredFormatter(logging.Formatter):
    COLOR_CODES = {
        logging.DEBUG: '\033[36m',
        logging.INFO: '\033[32m',
        logging.WARNING: '\033[33m',
        logging.ERROR: '\033[31m',
        logging.CRITICAL: '\033[41m',
    }
    RESET_CODE = '\033[0m'

    def format(self, record: logging.LogRecord) -> str:
        color_code = self.COLOR_CODES.get(record.levelno, self.RESET_CODE)
        message = super().format(record)
        return f"{color_code}{message}{self.RESET_CODE}"


class Logger:
    _instances = {}

    def __new__(cls, name: str):
        if name not in cls._instances:
            instance = super(Logger, cls).__new__(cls)
            cls._instances[name] = instance
            instance._initialized = False
        return cls._instances[name]

    def __init__(self, name: str):
        if self._initialized:
            return

        self.logger = logging.getLogger(name)
        
        if not Config.LOGGING_ENABLED:
            self.logger.setLevel(logging.CRITICAL + 1)
            return
            
        console_level = self._get_level_code(Config.LOG_LEVEL)
        self.logger.setLevel(console_level)
        
        self._setup_console_handler(console_level)
        self._initialized = True

    @staticmethod
    def _get_level_code(level: str) -> int:
        level_dict = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL,
        }
        return level_dict.get(level.lower(), logging.INFO)

    def _setup_console_handler(self, level: int) -> None:
        formatter = ColoredFormatter('%(levelname)s: %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def set_level(self, level: str) -> None:
        level_code = self._get_level_code(level)
        self.logger.setLevel(level_code)
        for handler in self.logger.handlers:
            handler.setLevel(level_code)

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

    def error(self, msg: str, exc_info: bool = False) -> None:
        self.logger.error(msg, exc_info=exc_info)

    def critical(self, msg: str) -> None:
        self.logger.critical(msg) 