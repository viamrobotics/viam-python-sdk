from copy import copy
import logging
from logging import DEBUG, INFO, WARN, WARNING, ERROR, FATAL  # noqa: F401
from typing import Dict

LOG_LEVEL = INFO
LOGGERS: Dict[str, logging.Logger] = {}


class ColorFormatter(logging.Formatter):

    MAPPING = {
        "DEBUG": 37,  # white
        "INFO": 36,  # cyan
        "WARNING": 33,  # yellow
        "ERROR": 31,  # red
        "CRITICAL": 41,  # white on red bg
    }

    def __init__(self, patern):
        logging.Formatter.__init__(self, patern)

    def format(self, record):
        colored_record = copy(record)
        levelname = colored_record.levelname
        seq = self.MAPPING.get(levelname, 37)  # default white
        colored_levelname = f"\x1b[33;{seq}m{levelname}\x1b[0m"
        colored_record.levelname = colored_levelname
        return super().format(colored_record)


def getLogger(name: str) -> logging.Logger:
    logger = LOGGERS.get(name)
    if logger:
        return logger
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    handler = logging.StreamHandler()
    format = ColorFormatter("%(asctime)s\t\t" + "%(levelname)s\t" + "%(name)s (%(filename)s:%(lineno)d)\t" + "%(message)s\t")
    handler.setFormatter(format)
    logger.addHandler(handler)
    LOGGERS[name] = logger
    return logger


def setLevel(level: int):
    LOG_LEVEL = level
    for logger in LOGGERS.values():
        logger.setLevel(LOG_LEVEL)
