import logging
import sys
from copy import copy
from logging import DEBUG, ERROR, FATAL, INFO, WARN, WARNING, LogRecord  # noqa: F401
from typing import Dict

LOG_LEVEL = INFO
LOGGERS: Dict[str, logging.Logger] = {}


class ModuleHandler(logging.Handler):
    def __init__(self, logger: logging.Logger, parent):
        self.parent = parent
        LOGGERS[f"BACKUP_{logger.name}"] = logger
        self.backup_logger = logger

        logger.handlers.clear()
        super().__init__()

    def emit(self, record: LogRecord):
        try:
            self.parent.log(
                record.name,
                record.levelname,
                record.asctime,
                record.msg,
                {record.filename: record.lineno},
                record.stack_info,
                record.__dict__,
            )
        except Exception:
            self.backup_logger.log(record.levelno, record.msg, exc_info=record.exc_info)
        return None


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

    addHandlers(logger)

    LOGGERS[name] = logger
    return logger


def addHandlers(logger: logging.Logger):
    logger.handlers.clear()

    format = ColorFormatter("%(asctime)s\t\t" + "%(levelname)s\t" + "%(name)s (%(filename)s:%(lineno)d)\t" + "%(message)s\t")

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(format)
    # filter out logs at error level or above
    handler.setLevel(LOG_LEVEL)
    handler.addFilter(filter=lambda record: (record.levelno < ERROR))
    logger.addHandler(handler)

    err_handler = logging.StreamHandler(stream=sys.stderr)
    err_handler.setFormatter(format)
    # filter out logs below error level
    err_handler.setLevel(max(ERROR, LOG_LEVEL))
    logger.addHandler(err_handler)


def addModuleHandler(logger: logging.Logger, parent):
    handler = ModuleHandler(logger, parent)
    logger.addHandler(handler)


def setLevel(level: int):
    global LOG_LEVEL
    LOG_LEVEL = level
    for logger in LOGGERS.values():
        logger.setLevel(LOG_LEVEL)
        addHandlers(logger)


def silence():
    setLevel(FATAL + 1)
