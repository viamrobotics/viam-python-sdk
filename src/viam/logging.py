import asyncio
import logging
import sys
from copy import copy
from datetime import datetime
from logging import DEBUG, ERROR, FATAL, INFO, WARN, WARNING, LogRecord  # noqa: F401
from typing import TYPE_CHECKING, Dict, Optional

import viam

if TYPE_CHECKING:
    from .robot.client import RobotClient


LOG_LEVEL = INFO
LOGGERS: Dict[str, logging.Logger] = {}
_MODULE_PARENT: Optional["RobotClient"] = None


class ModuleHandler(logging.Handler):
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self._parent = _MODULE_PARENT

        logger.handlers.clear()
        super().__init__()

    def emit(self, record: LogRecord):
        assert isinstance(record, logging.LogRecord)
        stack = f"exc_info: {record.exc_info}, exc_text: {record.exc_text}, stack_info: {record.stack_info}"
        message = f"{record.filename}:{record.lineno}\t{record.msg}"
        time = datetime.fromtimestamp(record.created)

        try:
            assert self._parent is not None
            coro = asyncio.wait_for(self._parent.log(record.name, record.levelname, time, message, stack), 10)
            asyncio.create_task(coro, name=f"{viam._TASK_PREFIX}-LOG-{record.created}")
            asyncio.create_task(
                self._parent.log(record.name, record.levelname, time, message, stack), name=f"{viam._TASK_PREFIX}-LOG-{time}"
            )
        except Exception as err:
            # If the module log fails, log using stdout/stderr handlers, and then readd the module handler.
            addHandlers(self.logger, True)
            self.logger.error(f"Module handler failed for {record.name} - {err}")
            self.logger.log(record.levelno, message)
            addHandlers(self.logger)


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


def addHandlers(logger: logging.Logger, default=False):
    logger.handlers.clear()

    format = ColorFormatter("%(asctime)s\t\t" + "%(levelname)s\t" + "%(name)s (%(filename)s:%(lineno)d)\t" + "%(message)s\t")

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(format)
    # filter out logs at error level or above
    handler.setLevel(LOG_LEVEL)
    handler.addFilter(filter=lambda record: (record.levelno < ERROR))

    err_handler = logging.StreamHandler(stream=sys.stderr)
    err_handler.setFormatter(format)
    # filter out logs below error level
    err_handler.setLevel(max(ERROR, LOG_LEVEL))

    if _MODULE_PARENT is not None and not default:
        _startModuleLogging(logger)
    else:
        logger.addHandler(handler)
        logger.addHandler(err_handler)


def _startModuleLogging(logger: logging.Logger):
    handler = ModuleHandler(logger)

    format = ColorFormatter("%(asctime)s\t\t" + "%(levelname)s\t" + "%(name)s (%(filename)s:%(lineno)d)\t" + "%(message)s\t")
    handler.setFormatter(format)
    handler.setLevel(LOG_LEVEL)

    logger.addHandler(handler)


def setParent(parent: "RobotClient"):
    global _MODULE_PARENT
    _MODULE_PARENT = parent
    for logger in list(LOGGERS.values()):
        _startModuleLogging(logger)


def setLevel(level: int):
    global LOG_LEVEL
    LOG_LEVEL = level
    for logger in LOGGERS.values():
        logger.setLevel(LOG_LEVEL)
        addHandlers(logger)


def silence():
    setLevel(FATAL + 1)
