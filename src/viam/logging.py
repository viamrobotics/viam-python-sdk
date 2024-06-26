import asyncio
import logging
import sys
from copy import copy
from datetime import datetime
from logging import DEBUG, ERROR, FATAL, INFO, WARN, WARNING  # noqa: F401
from typing import TYPE_CHECKING, Dict, Iterable, List, Optional, Union

from grpclib.exceptions import StreamTerminatedError

import viam

if TYPE_CHECKING:
    from .robot.client import RobotClient


LOG_LEVEL = INFO
LOGGERS: Dict[str, logging.Logger] = {}
_MODULE_PARENT: Optional["RobotClient"] = None


class _ModuleHandler(logging.Handler):
    _parent: "RobotClient"
    _logger: logging.Logger

    def __init__(self, parent: "RobotClient"):
        self._parent = parent
        self._logger = logging.getLogger("ModuleLogger")
        addHandlers(self._logger, True)
        super().__init__()
        self._logger.setLevel(self.level)

    def setLevel(self, level: Union[int, str]) -> None:
        self._logger.setLevel(level)
        return super().setLevel(level)

    def handle_task_result(self, task: asyncio.Task):
        try:
            _ = task.result()
        except (asyncio.CancelledError, asyncio.InvalidStateError, StreamTerminatedError):
            pass

    def emit(self, record: logging.LogRecord):
        assert isinstance(record, logging.LogRecord)
        name = record.name.split(".")[-1]
        message = f"{record.filename}:{record.lineno}\t{record.getMessage()}"
        stack = f"exc_info: {record.exc_info}, exc_text: {record.exc_text}, stack_info: {record.stack_info}"
        time = datetime.fromtimestamp(record.created)

        try:
            assert self._parent is not None
            try:
                loop = asyncio.get_event_loop()
                loop.create_task(
                    self._parent.log(name, record.levelname, time, message, stack), name=f"{viam._TASK_PREFIX}-LOG-{record.created}"
                ).add_done_callback(self.handle_task_result)
            except RuntimeError:
                # If the log is coming from a thread that doesn't have an event loop, create and set a new one.
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.create_task(
                    self._parent.log(name, record.levelname, time, message, stack), name=f"{viam._TASK_PREFIX}-LOG-{record.created}"
                ).add_done_callback(self.handle_task_result)
        except Exception as err:
            # If the module log fails, log using stdout/stderr handlers
            self._logger.error(f"ModuleLogger failed for {record.name} - {err}")
            self._logger.log(record.levelno, message)


class _ColorFormatter(logging.Formatter):
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


def addHandlers(logger: logging.Logger, use_default_handlers=False):
    _addHandlers([logger], use_default_handlers)


def _addHandlers(loggers: Iterable[logging.Logger], use_default_handlers=False):
    format = _ColorFormatter("%(asctime)s\t\t" + "%(levelname)s\t" + "%(name)s (%(filename)s:%(lineno)d)\t" + "%(message)s\t")

    handlers: List[logging.Handler] = []

    std_handler = logging.StreamHandler(stream=sys.stdout)
    std_handler.setFormatter(format)
    # filter out logs at error level or above
    std_handler.setLevel(LOG_LEVEL)
    std_handler.addFilter(filter=lambda record: (record.levelno < ERROR))

    err_handler = logging.StreamHandler(stream=sys.stderr)
    err_handler.setFormatter(format)
    # filter out logs below error level
    err_handler.setLevel(max(ERROR, LOG_LEVEL))

    if _MODULE_PARENT is not None and not use_default_handlers:
        mod_handler = _ModuleHandler(_MODULE_PARENT)
        mod_handler.setFormatter(format)
        mod_handler.setLevel(LOG_LEVEL)
        handlers = [mod_handler]
    else:
        handlers = [std_handler, err_handler]

    for logger in loggers:
        logger.handlers.clear()
        if "viam.sessions_client" in LOGGERS and LOGGERS["viam.sessions_client"] == logger:
            logger.addHandler(std_handler)
            logger.addHandler(err_handler)
        else:
            for h in handlers:
                logger.addHandler(h)


def setParent(parent: "RobotClient"):
    global _MODULE_PARENT
    _MODULE_PARENT = parent
    _addHandlers(LOGGERS.values())


def setLevel(level: int):
    global LOG_LEVEL
    LOG_LEVEL = level
    for logger in LOGGERS.values():
        logger.setLevel(LOG_LEVEL)
    _addHandlers(LOGGERS.values())


def silence():
    setLevel(FATAL + 1)
