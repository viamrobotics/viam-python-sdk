import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import component
from .input_controller_grpc import InputControllerServiceBase as _InputControllerServiceBase

class UnimplementedInputControllerServiceBase(_InputControllerServiceBase):

    async def GetControls(self, stream: 'grpclib.server.Stream[component.inputcontroller.v1.input_controller_pb2.GetControlsRequest, component.inputcontroller.v1.input_controller_pb2.GetControlsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetEvents(self, stream: 'grpclib.server.Stream[component.inputcontroller.v1.input_controller_pb2.GetEventsRequest, component.inputcontroller.v1.input_controller_pb2.GetEventsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StreamEvents(self, stream: 'grpclib.server.Stream[component.inputcontroller.v1.input_controller_pb2.StreamEventsRequest, component.inputcontroller.v1.input_controller_pb2.StreamEventsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def TriggerEvent(self, stream: 'grpclib.server.Stream[component.inputcontroller.v1.input_controller_pb2.TriggerEventRequest, component.inputcontroller.v1.input_controller_pb2.TriggerEventResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)