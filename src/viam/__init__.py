import sys
from importlib.metadata import PackageNotFoundError, version
from uuid import uuid4

from viam.gen.common.v1.common_pb2 import ResourceName as _ResourceName

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
def _rname_str(self: _ResourceName) -> str:
    return f"{self.namespace}:{self.type}:{self.subtype}/{self.name}"


_ResourceName.__str__ = _rname_str


def _rname_repr(self: _ResourceName) -> str:
    return f"<viam.proto.common.ResourceName {str(self)} at {hex(id(self))}>"


_ResourceName.__repr__ = _rname_repr


def _rname_hash(self: _ResourceName) -> int:
    return hash(str(self))


_ResourceName.__hash__ = _rname_hash  # type: ignore


def _rname_eq(self: _ResourceName, other: object) -> bool:
    if isinstance(other, _ResourceName):
        return self.__hash__() == other.__hash__()  # type: ignore
    return False


_ResourceName.__eq__ = _rname_eq  # type: ignore
