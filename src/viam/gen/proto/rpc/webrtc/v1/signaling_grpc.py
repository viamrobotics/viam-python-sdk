import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
from ..... import proto

class SignalingServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Call(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.CallRequest, proto.rpc.webrtc.v1.signaling_pb2.CallResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CallUpdate(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.CallUpdateRequest, proto.rpc.webrtc.v1.signaling_pb2.CallUpdateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Answer(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.AnswerResponse, proto.rpc.webrtc.v1.signaling_pb2.AnswerRequest]') -> None:
        pass

    @abc.abstractmethod
    async def OptionalWebRTCConfig(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigRequest, proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.rpc.webrtc.v1.SignalingService/Call': grpclib.const.Handler(self.Call, grpclib.const.Cardinality.UNARY_STREAM, proto.rpc.webrtc.v1.signaling_pb2.CallRequest, proto.rpc.webrtc.v1.signaling_pb2.CallResponse), '/proto.rpc.webrtc.v1.SignalingService/CallUpdate': grpclib.const.Handler(self.CallUpdate, grpclib.const.Cardinality.UNARY_UNARY, proto.rpc.webrtc.v1.signaling_pb2.CallUpdateRequest, proto.rpc.webrtc.v1.signaling_pb2.CallUpdateResponse), '/proto.rpc.webrtc.v1.SignalingService/Answer': grpclib.const.Handler(self.Answer, grpclib.const.Cardinality.STREAM_STREAM, proto.rpc.webrtc.v1.signaling_pb2.AnswerResponse, proto.rpc.webrtc.v1.signaling_pb2.AnswerRequest), '/proto.rpc.webrtc.v1.SignalingService/OptionalWebRTCConfig': grpclib.const.Handler(self.OptionalWebRTCConfig, grpclib.const.Cardinality.UNARY_UNARY, proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigRequest, proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigResponse)}

class UnimplementedSignalingServiceBase(SignalingServiceBase):

    async def Call(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.CallRequest, proto.rpc.webrtc.v1.signaling_pb2.CallResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CallUpdate(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.CallUpdateRequest, proto.rpc.webrtc.v1.signaling_pb2.CallUpdateResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Answer(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.AnswerResponse, proto.rpc.webrtc.v1.signaling_pb2.AnswerRequest]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def OptionalWebRTCConfig(self, stream: 'grpclib.server.Stream[proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigRequest, proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class SignalingServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Call = grpclib.client.UnaryStreamMethod(channel, '/proto.rpc.webrtc.v1.SignalingService/Call', proto.rpc.webrtc.v1.signaling_pb2.CallRequest, proto.rpc.webrtc.v1.signaling_pb2.CallResponse)
        self.CallUpdate = grpclib.client.UnaryUnaryMethod(channel, '/proto.rpc.webrtc.v1.SignalingService/CallUpdate', proto.rpc.webrtc.v1.signaling_pb2.CallUpdateRequest, proto.rpc.webrtc.v1.signaling_pb2.CallUpdateResponse)
        self.Answer = grpclib.client.StreamStreamMethod(channel, '/proto.rpc.webrtc.v1.SignalingService/Answer', proto.rpc.webrtc.v1.signaling_pb2.AnswerResponse, proto.rpc.webrtc.v1.signaling_pb2.AnswerRequest)
        self.OptionalWebRTCConfig = grpclib.client.UnaryUnaryMethod(channel, '/proto.rpc.webrtc.v1.SignalingService/OptionalWebRTCConfig', proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigRequest, proto.rpc.webrtc.v1.signaling_pb2.OptionalWebRTCConfigResponse)