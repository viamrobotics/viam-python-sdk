# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/oslogin/v1beta/oslogin.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.cloud.oslogin.common.common_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.cloud.oslogin.v1beta.oslogin_pb2


class OsLoginServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DeletePosixAccount(self, stream: 'grpclib.server.Stream[google.cloud.oslogin.v1beta.oslogin_pb2.DeletePosixAccountRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteSshPublicKey(self, stream: 'grpclib.server.Stream[google.cloud.oslogin.v1beta.oslogin_pb2.DeleteSshPublicKeyRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GetLoginProfile(self, stream: 'grpclib.server.Stream[google.cloud.oslogin.v1beta.oslogin_pb2.GetLoginProfileRequest, google.cloud.oslogin.v1beta.oslogin_pb2.LoginProfile]') -> None:
        pass

    @abc.abstractmethod
    async def GetSshPublicKey(self, stream: 'grpclib.server.Stream[google.cloud.oslogin.v1beta.oslogin_pb2.GetSshPublicKeyRequest, google.cloud.oslogin.common.common_pb2.SshPublicKey]') -> None:
        pass

    @abc.abstractmethod
    async def ImportSshPublicKey(self, stream: 'grpclib.server.Stream[google.cloud.oslogin.v1beta.oslogin_pb2.ImportSshPublicKeyRequest, google.cloud.oslogin.v1beta.oslogin_pb2.ImportSshPublicKeyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateSshPublicKey(self, stream: 'grpclib.server.Stream[google.cloud.oslogin.v1beta.oslogin_pb2.UpdateSshPublicKeyRequest, google.cloud.oslogin.common.common_pb2.SshPublicKey]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.oslogin.v1beta.OsLoginService/DeletePosixAccount': grpclib.const.Handler(
                self.DeletePosixAccount,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.oslogin.v1beta.oslogin_pb2.DeletePosixAccountRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.oslogin.v1beta.OsLoginService/DeleteSshPublicKey': grpclib.const.Handler(
                self.DeleteSshPublicKey,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.oslogin.v1beta.oslogin_pb2.DeleteSshPublicKeyRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.oslogin.v1beta.OsLoginService/GetLoginProfile': grpclib.const.Handler(
                self.GetLoginProfile,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.oslogin.v1beta.oslogin_pb2.GetLoginProfileRequest,
                google.cloud.oslogin.v1beta.oslogin_pb2.LoginProfile,
            ),
            '/google.cloud.oslogin.v1beta.OsLoginService/GetSshPublicKey': grpclib.const.Handler(
                self.GetSshPublicKey,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.oslogin.v1beta.oslogin_pb2.GetSshPublicKeyRequest,
                google.cloud.oslogin.common.common_pb2.SshPublicKey,
            ),
            '/google.cloud.oslogin.v1beta.OsLoginService/ImportSshPublicKey': grpclib.const.Handler(
                self.ImportSshPublicKey,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.oslogin.v1beta.oslogin_pb2.ImportSshPublicKeyRequest,
                google.cloud.oslogin.v1beta.oslogin_pb2.ImportSshPublicKeyResponse,
            ),
            '/google.cloud.oslogin.v1beta.OsLoginService/UpdateSshPublicKey': grpclib.const.Handler(
                self.UpdateSshPublicKey,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.oslogin.v1beta.oslogin_pb2.UpdateSshPublicKeyRequest,
                google.cloud.oslogin.common.common_pb2.SshPublicKey,
            ),
        }


class OsLoginServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DeletePosixAccount = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.oslogin.v1beta.OsLoginService/DeletePosixAccount',
            google.cloud.oslogin.v1beta.oslogin_pb2.DeletePosixAccountRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.DeleteSshPublicKey = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.oslogin.v1beta.OsLoginService/DeleteSshPublicKey',
            google.cloud.oslogin.v1beta.oslogin_pb2.DeleteSshPublicKeyRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GetLoginProfile = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.oslogin.v1beta.OsLoginService/GetLoginProfile',
            google.cloud.oslogin.v1beta.oslogin_pb2.GetLoginProfileRequest,
            google.cloud.oslogin.v1beta.oslogin_pb2.LoginProfile,
        )
        self.GetSshPublicKey = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.oslogin.v1beta.OsLoginService/GetSshPublicKey',
            google.cloud.oslogin.v1beta.oslogin_pb2.GetSshPublicKeyRequest,
            google.cloud.oslogin.common.common_pb2.SshPublicKey,
        )
        self.ImportSshPublicKey = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.oslogin.v1beta.OsLoginService/ImportSshPublicKey',
            google.cloud.oslogin.v1beta.oslogin_pb2.ImportSshPublicKeyRequest,
            google.cloud.oslogin.v1beta.oslogin_pb2.ImportSshPublicKeyResponse,
        )
        self.UpdateSshPublicKey = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.oslogin.v1beta.OsLoginService/UpdateSshPublicKey',
            google.cloud.oslogin.v1beta.oslogin_pb2.UpdateSshPublicKeyRequest,
            google.cloud.oslogin.common.common_pb2.SshPublicKey,
        )
