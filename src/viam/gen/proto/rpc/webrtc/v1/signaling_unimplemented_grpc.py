import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
from ..... import proto
from .signaling_grpc import SignalingServiceBase as _SignalingServiceBase

class UnimplementedSignalingServiceBase(_SignalingServiceBase):

    async def Call(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.CallRequest, proto.rpc.webrtc.v1.signaling_pb2.CallResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CallUpdate(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.CallUpdateRequest, proto.rpc.webrtc.v1.signaling_pb2.CallUpdateResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Answer(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.AnswerResponse, proto.rpc.webrtc.v1.signaling_pb2.AnswerRequest]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def OptionalWebRTCConfig(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigRequest, proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)