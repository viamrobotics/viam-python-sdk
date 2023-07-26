"""
This file outlines the general structure for the API around a custom, modularized component.

It defines the abstract class definition that all concrete implementations must follow,
the gRPC service that will handle calls to the component,
and the gRPC client that will be able to make calls to this component.

In this example, the ``Gizmo`` abstract class defines what functionality is required for all Gizmos. It extends ``ComponentBase``,
as all component types must. It also defines its specific ``SUBTYPE``, which is used internally to keep track of supported types.

The ``GizmoService`` implements the gRPC service for the Gizmo. This will allow other robots and clients to make requests of the Gizmo.
It extends both from ``GizmoServiceBase`` and ``ResourceRPCServiceBase``. The former is the gRPC service as defined by the proto,
and the latter is the class that all gRPC services for components must inherit from.

Finally, the ``GizmoClient`` is the gRPC client for a Gizmo. It inherits from Gizmo since it implements all the same functions. The
implementations are simply gRPC calls to some remote Gizmo.

To see how this custom modular component is registered, see the __init__.py file.
To see the custom implementation of this component, see the my_gizmo.py file.
"""

import abc
from typing import Final, List, Mapping, Optional, Sequence

from grpclib.client import Channel
from grpclib.server import Stream

from viam.components.component_base import ComponentBase
from viam.components.generic.client import do_command
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.resource.types import RESOURCE_TYPE_COMPONENT, Subtype
from viam.utils import ValueTypes

from ..proto.gizmo_grpc import GizmoServiceBase, GizmoServiceStub
from ..proto.gizmo_pb2 import (
    DoOneBiDiStreamRequest,
    DoOneBiDiStreamResponse,
    DoOneClientStreamRequest,
    DoOneClientStreamResponse,
    DoOneRequest,
    DoOneResponse,
    DoOneServerStreamRequest,
    DoOneServerStreamResponse,
    DoTwoRequest,
    DoTwoResponse,
)


class Gizmo(ComponentBase):
    """Example component to use with the example module."""

    SUBTYPE: Final = Subtype("acme", RESOURCE_TYPE_COMPONENT, "gizmo")

    @abc.abstractmethod
    async def do_one(self, arg1: str, **kwargs) -> bool:
        ...

    @abc.abstractmethod
    async def do_one_client_stream(self, arg1: Sequence[str], **kwargs) -> bool:
        ...

    @abc.abstractmethod
    async def do_one_server_stream(self, arg1: str, **kwargs) -> Sequence[bool]:
        ...

    @abc.abstractmethod
    async def do_one_bidi_stream(self, arg1: Sequence[str], **kwargs) -> Sequence[bool]:
        ...

    @abc.abstractmethod
    async def do_two(self, arg1: bool, **kwargs) -> str:
        ...


class GizmoService(GizmoServiceBase, ResourceRPCServiceBase):
    """Example gRPC service for the Gizmo component"""

    RESOURCE_TYPE = Gizmo

    async def DoOne(self, stream: Stream[DoOneRequest, DoOneResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        gizmo = self.get_resource(name)
        resp = await gizmo.do_one(request.arg1)
        response = DoOneResponse(ret1=resp)
        await stream.send_message(response)

    async def DoOneClientStream(self, stream: Stream[DoOneClientStreamRequest, DoOneClientStreamResponse]) -> None:
        requests = [request async for request in stream]
        args = [request.arg1 for request in requests]
        names = [request.name for request in requests]
        if len(set(names)) != 1:
            raise Exception("Unexpectedly received requests for multiple Gizmos")
        name = names[0]
        gizmo = self.get_resource(name)
        resp = await gizmo.do_one_client_stream(args)
        response = DoOneClientStreamResponse(ret1=resp)
        await stream.send_message(response)

    async def DoOneServerStream(self, stream: Stream[DoOneServerStreamRequest, DoOneServerStreamResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        gizmo = self.get_resource(name)
        resps = await gizmo.do_one_server_stream(request.arg1)
        for resp in resps:
            await stream.send_message(DoOneServerStreamResponse(ret1=resp))

    async def DoOneBiDiStream(self, stream: Stream[DoOneBiDiStreamRequest, DoOneBiDiStreamResponse]) -> None:
        args: List[str] = []
        name: str = ""
        async for request in stream:
            args.append(request.arg1)
            if name == "":
                name = request.name
                continue
            if name != request.name:
                raise Exception("Unexpectedly received requests for multiple Gizmos")
        gizmo = self.get_resource(name)

        resps = await gizmo.do_one_bidi_stream(args)
        for resp in resps:
            await stream.send_message(DoOneBiDiStreamResponse(ret1=resp))

    async def DoTwo(self, stream: Stream[DoTwoRequest, DoTwoResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        gizmo = self.get_resource(name)
        resp = await gizmo.do_two(request.arg1)
        response = DoTwoResponse(ret1=resp)
        await stream.send_message(response)


class GizmoClient(Gizmo):
    """Example gRPC client for the Gizmo component"""

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = GizmoServiceStub(channel)
        super().__init__(name)

    async def do_one(self, arg1: str) -> bool:
        resp: DoOneResponse = await self.client.DoOne(DoOneRequest(name=self.name, arg1=arg1))
        return resp.ret1

    async def do_one_client_stream(self, arg1: Sequence[str]) -> bool:
        async with self.client.DoOneClientStream.open() as stream:
            await stream.send_request()
            for arg in arg1:
                await stream.send_message(DoOneClientStreamRequest(name=self.name, arg1=arg))
            await stream.end()
            response = await stream.recv_message()
            assert response is not None
            return response.ret1

    async def do_one_server_stream(self, arg1: str) -> Sequence[bool]:
        async with self.client.DoOneServerStream.open() as stream:
            await stream.send_message(DoOneServerStreamRequest(name=self.name, arg1=arg1))
            resps = [resp.ret1 async for resp in stream]
            return resps

    async def do_one_bidi_stream(self, arg1: Sequence[str]) -> Sequence[bool]:
        async with self.client.DoOneClientStream.open() as stream:
            await stream.send_request()
            for arg in arg1:
                await stream.send_message(DoOneClientStreamRequest(name=self.name, arg1=arg))
            await stream.end()
            resps = [resp.ret1 async for resp in stream]
            return resps

    async def do_two(self, arg1: bool) -> str:
        resp = await self.client.DoTwo(DoTwoRequest(name=self.name, arg1=arg1))
        return resp.ret1

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
    ) -> Mapping[str, ValueTypes]:
        return await do_command(self.channel, self.name, command, timeout=timeout)
