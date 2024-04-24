"""
@generated by Viam.
Do not edit manually!
"""
from ...gen.module.v1.module_grpc import ModuleServiceBase, ModuleServiceStub
from ...gen.module.v1.module_pb2 import (
    AddResourceRequest,
    AddResourceResponse,
    HandlerDefinition,
    HandlerMap,
    ReadyRequest,
    ReadyResponse,
    ReconfigureResourceRequest,
    ReconfigureResourceResponse,
    RemoveResourceRequest,
    RemoveResourceResponse,
    ValidateConfigRequest,
    ValidateConfigResponse,
)
from ...gen.module.v1.module_unimplemented_grpc import UnimplementedModuleServiceBase

__all__ = [
    "ModuleServiceBase",
    "ModuleServiceStub",
    "AddResourceRequest",
    "AddResourceResponse",
    "HandlerDefinition",
    "HandlerMap",
    "ReadyRequest",
    "ReadyResponse",
    "ReconfigureResourceRequest",
    "ReconfigureResourceResponse",
    "RemoveResourceRequest",
    "RemoveResourceResponse",
    "ValidateConfigRequest",
    "ValidateConfigResponse",
    "UnimplementedModuleServiceBase",
]
