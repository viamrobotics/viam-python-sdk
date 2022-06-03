import sys
from importlib.metadata import version, PackageNotFoundError
from uuid import uuid4

from .logging import getLogger as _getLogger

try:
    __version__ = version("viam")
except PackageNotFoundError:
    pass

_TASK_PREFIX = uuid4().hex


def _log_exceptions(exctype, value, traceback):
    _LOGGER = _getLogger(__name__)
    _LOGGER.error("[ERROR] Uncaught exception",
                  exc_info=(exctype, value, traceback))
    sys.__excepthook__(exctype, value, traceback)


sys.excepthook = _log_exceptions
