# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/user_data_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.common.offline_user_data_pb2
import google.api.annotations_pb2
import google.api.field_behavior_pb2
import google.api.client_pb2
import google.ads.googleads.v9.services.user_data_service_pb2


class UserDataServiceBase(abc.ABC):

    @abc.abstractmethod
    async def UploadUserData(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.user_data_service_pb2.UploadUserDataRequest, google.ads.googleads.v9.services.user_data_service_pb2.UploadUserDataResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.UserDataService/UploadUserData': grpclib.const.Handler(
                self.UploadUserData,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.user_data_service_pb2.UploadUserDataRequest,
                google.ads.googleads.v9.services.user_data_service_pb2.UploadUserDataResponse,
            ),
        }


class UserDataServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.UploadUserData = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.UserDataService/UploadUserData',
            google.ads.googleads.v9.services.user_data_service_pb2.UploadUserDataRequest,
            google.ads.googleads.v9.services.user_data_service_pb2.UploadUserDataResponse,
        )
