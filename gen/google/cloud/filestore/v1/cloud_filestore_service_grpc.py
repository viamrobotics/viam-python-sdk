# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/filestore/v1/cloud_filestore_service.proto
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
import google.cloud.common.operation_metadata_pb2
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import google.cloud.filestore.v1.cloud_filestore_service_pb2


class CloudFilestoreManagerBase(abc.ABC):

    @abc.abstractmethod
    async def ListInstances(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.ListInstancesRequest, google.cloud.filestore.v1.cloud_filestore_service_pb2.ListInstancesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetInstance(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.GetInstanceRequest, google.cloud.filestore.v1.cloud_filestore_service_pb2.Instance]') -> None:
        pass

    @abc.abstractmethod
    async def CreateInstance(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.CreateInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateInstance(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.UpdateInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def RestoreInstance(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.RestoreInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteInstance(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.DeleteInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListBackups(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.ListBackupsRequest, google.cloud.filestore.v1.cloud_filestore_service_pb2.ListBackupsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetBackup(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.GetBackupRequest, google.cloud.filestore.v1.cloud_filestore_service_pb2.Backup]') -> None:
        pass

    @abc.abstractmethod
    async def CreateBackup(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.CreateBackupRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteBackup(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.DeleteBackupRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateBackup(self, stream: 'grpclib.server.Stream[google.cloud.filestore.v1.cloud_filestore_service_pb2.UpdateBackupRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.filestore.v1.CloudFilestoreManager/ListInstances': grpclib.const.Handler(
                self.ListInstances,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.ListInstancesRequest,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.ListInstancesResponse,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/GetInstance': grpclib.const.Handler(
                self.GetInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.GetInstanceRequest,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.Instance,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/CreateInstance': grpclib.const.Handler(
                self.CreateInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.CreateInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/UpdateInstance': grpclib.const.Handler(
                self.UpdateInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.UpdateInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/RestoreInstance': grpclib.const.Handler(
                self.RestoreInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.RestoreInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/DeleteInstance': grpclib.const.Handler(
                self.DeleteInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.DeleteInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/ListBackups': grpclib.const.Handler(
                self.ListBackups,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.ListBackupsRequest,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.ListBackupsResponse,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/GetBackup': grpclib.const.Handler(
                self.GetBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.GetBackupRequest,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.Backup,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/CreateBackup': grpclib.const.Handler(
                self.CreateBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.CreateBackupRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/DeleteBackup': grpclib.const.Handler(
                self.DeleteBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.DeleteBackupRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.filestore.v1.CloudFilestoreManager/UpdateBackup': grpclib.const.Handler(
                self.UpdateBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.filestore.v1.cloud_filestore_service_pb2.UpdateBackupRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class CloudFilestoreManagerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListInstances = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/ListInstances',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.ListInstancesRequest,
            google.cloud.filestore.v1.cloud_filestore_service_pb2.ListInstancesResponse,
        )
        self.GetInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/GetInstance',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.GetInstanceRequest,
            google.cloud.filestore.v1.cloud_filestore_service_pb2.Instance,
        )
        self.CreateInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/CreateInstance',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.CreateInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/UpdateInstance',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.UpdateInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.RestoreInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/RestoreInstance',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.RestoreInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/DeleteInstance',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.DeleteInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListBackups = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/ListBackups',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.ListBackupsRequest,
            google.cloud.filestore.v1.cloud_filestore_service_pb2.ListBackupsResponse,
        )
        self.GetBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/GetBackup',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.GetBackupRequest,
            google.cloud.filestore.v1.cloud_filestore_service_pb2.Backup,
        )
        self.CreateBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/CreateBackup',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.CreateBackupRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/DeleteBackup',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.DeleteBackupRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.filestore.v1.CloudFilestoreManager/UpdateBackup',
            google.cloud.filestore.v1.cloud_filestore_service_pb2.UpdateBackupRequest,
            google.longrunning.operations_pb2.Operation,
        )
