import logging
import sys
from copy import copy
from datetime import datetime
from logging import DEBUG, ERROR, FATAL, INFO, WARN, WARNING  # noqa: F401
from typing import Dict, List

LOG_LEVEL = INFO
LOGGERS: Dict[str, logging.Logger] = {}


class ModuleLogger:
    def __init__(self, name: str, logger: logging.Logger):
        self.name = name

        self.stdoutLogger = logger

    def start_logging_to_grpc(self, parent):
        self.parent = parent

    async def log(self, level: str, time: datetime, msg: str, caller: Dict[str, int], stack: List[str], retry=False):
        if self.parent and not retry:
            await self.parent.log(self, level, time, msg, caller, stack)
        else:
            if level.capitalize() == "DEBUG":
                self.stdoutLogger.debug(msg)
            elif level.capitalize() == "INFO":
                self.stdoutLogger.info(msg)
            elif level.capitalize() in ["WARN", "WARNING"]:
                self.stdoutLogger.warning(msg)
            elif level.capitalize() == "ERROR":
                self.stdoutLogger.error(msg)
            elif level.capitalize() in ["FATAL", "CRITICAL"]:
                self.stdoutLogger.critical(msg)
            else:
                raise Exception(f"Level {level} is not acceptable. Log level must be DEBUG, INFO, WARN/WARNING, ERROR, or FATAL/CRITICAL.")


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


def setLevel(level: int):
    global LOG_LEVEL
    LOG_LEVEL = level
    for logger in LOGGERS.values():
        logger.setLevel(LOG_LEVEL)
        addHandlers(logger)


def silence():
    setLevel(FATAL + 1)
