from grpclib.const import Status
from grpclib.exceptions import GRPCError
from grpclib.server import Stream
from viam.proto.rpc.webrtc.signaling import (
    SignalingServiceBase,
    CallRequest,
    CallResponse,
    CallUpdateRequest,
    CallUpdateResponse,
    AnswerRequest,
    AnswerResponse,
    OptionalWebRTCConfigRequest,
    OptionalWebRTCConfigResponse,
)


class SignalingService(SignalingServiceBase):
    async def Call(self, stream: Stream[CallRequest, CallResponse]) -> None:
        raise GRPCError(Status.UNIMPLEMENTED, "SignalingService is unimplemented")

    async def CallUpdate(self, stream: Stream[CallUpdateRequest, CallUpdateResponse]) -> None:
        raise GRPCError(Status.UNIMPLEMENTED, "SignalingService is unimplemented")

    async def Answer(self, stream: Stream[AnswerResponse, AnswerRequest]) -> None:
        raise GRPCError(Status.UNIMPLEMENTED, "SignalingService is unimplemented")

    async def OptionalWebRTCConfig(self, stream: Stream[OptionalWebRTCConfigRequest, OptionalWebRTCConfigResponse]) -> None:
        raise GRPCError(Status.UNIMPLEMENTED, "SignalingService is unimplemented")
