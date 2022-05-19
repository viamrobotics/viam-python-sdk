"""
.. include:: ../README.md
"""
import sys
from uuid import uuid4

from ._version import __version__  # noqa: F401
from .logging import getLogger

__docformat__ = "restructuredtext"

_TASK_PREFIX = uuid4().hex


def _log_exceptions(exctype, value, traceback):
    _LOGGER = getLogger(__name__)
    _LOGGER.error('[ERROR] Uncaught exception', exc_info=(exctype, value, traceback))
    sys.__excepthook__(exctype, value, traceback)


sys.excepthook = _log_exceptions
