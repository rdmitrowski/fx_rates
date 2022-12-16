import logging
import time
from logging.handlers import RotatingFileHandler


def log_initialize():

    log_handler = logging.handlers.RotatingFileHandler(
        filename='Fx_rates.log', 
        mode='a', maxBytes=10**4, 
        backupCount=5)
    formatter = logging.Formatter(
        '%(asctime)s fx_rates [%(process)d]: [%(levelname)s] %(message)s',
        '%b %d %H:%M:%S')
    log_handler.setFormatter(formatter)
    logger = logging.getLogger("Process fx_rates rotating log")
    logger.setLevel(logging.INFO)
    logger.addHandler(log_handler)
    # stream handler
    streamHandler = logging.StreamHandler()
    streamFormat = formatter
    streamHandler.setFormatter(streamFormat)
    logger.addHandler(streamHandler)
    return logger
