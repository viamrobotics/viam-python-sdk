from typing import TYPE_CHECKING

from grpclib.server import Stream

from viam.proto.module import (
    AddResourceRequest,
    AddResourceResponse,
    ModuleServiceBase,
    ReadyRequest,
    ReadyResponse,
    ReconfigureResourceRequest,
    ReconfigureResourceResponse,
    RemoveResourceRequest,
    RemoveResourceResponse,
    ValidateConfigRequest,
    ValidateConfigResponse,
)

if TYPE_CHECKING:
    from .module import Module


class ModuleRPCService(ModuleServiceBase):
    _module: "Module"

    def __init__(self, module: "Module") -> None:
        self._module = module

    async def AddResource(self, stream: Stream[AddResourceRequest, AddResourceResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await self._module.add_resource(request)
        await stream.send_message(AddResourceResponse())

    async def ReconfigureResource(self, stream: Stream[ReconfigureResourceRequest, ReconfigureResourceResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await self._module.reconfigure_resource(request)
        await stream.send_message(ReconfigureResourceResponse())

    async def RemoveResource(self, stream: Stream[RemoveResourceRequest, RemoveResourceResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await self._module.remove_resource(request)
        await stream.send_message(RemoveResourceResponse())

    async def Ready(self, stream: Stream[ReadyRequest, ReadyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = await self._module.ready(request)
        await stream.send_message(response)

    async def ValidateConfig(self, stream: Stream[ValidateConfigRequest, ValidateConfigResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = await self._module.validate_config(request)
        if response is not None:
            await stream.send_message(response)
