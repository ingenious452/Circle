import logging
from logging.handlers import RotatingFileHandler

LOG_FORMAT = "{asctime} | {name} | {levelname} | {message}"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_logger(name: str, log_path, level=logging.INFO):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    file_handler = RotatingFileHandler(log_path, maxBytes=2_000_000, backupCount=5)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT, style="{"))

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT, style="{"))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(level)
    return logger
