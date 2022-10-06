import sys
from importlib.metadata import PackageNotFoundError, version
from uuid import uuid4

from viam.proto.common import ResourceName as _ResourceName

from .logging import getLogger as _getLogger

##############
# VERSIONING #
##############
try:
    __version__ = version("viam-sdk")
except PackageNotFoundError:
    pass

##########################################################
# #################### TASK PREFIX ##################### #
# ###### Used to give each task a unique identifier #### #
# so that tasks spawned by Viam can be canceled on close #
##########################################################
_TASK_PREFIX = uuid4().hex


##########################################################
# ################### LOG EXCEPTIONS ################### #
# Change the default exception handler to log exceptions #
# ############### prior to raising them ################ #
##########################################################


def _log_exceptions(exctype, value, traceback):
    _LOGGER = _getLogger(__name__)
    _LOGGER.error("[ERROR] Uncaught exception", exc_info=(exctype, value, traceback))
    sys.__excepthook__(exctype, value, traceback)


sys.excepthook = _log_exceptions


##################
# MONKEY PATCHES #
##################
_ResourceName.__hash__ = lambda self: hash(f"{self.namespace}/{self.type}/{self.subtype}/{self.name}")
