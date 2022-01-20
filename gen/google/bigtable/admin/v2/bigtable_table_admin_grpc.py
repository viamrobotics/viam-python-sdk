# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/bigtable/admin/v2/bigtable_table_admin.proto
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
import google.bigtable.admin.v2.common_pb2
import google.bigtable.admin.v2.table_pb2
import google.iam.v1.iam_policy_pb2
import google.iam.v1.policy_pb2
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.bigtable.admin.v2.bigtable_table_admin_pb2


class BigtableTableAdminBase(abc.ABC):

    @abc.abstractmethod
    async def CreateTable(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateTableRequest, google.bigtable.admin.v2.table_pb2.Table]') -> None:
        pass

    @abc.abstractmethod
    async def CreateTableFromSnapshot(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateTableFromSnapshotRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListTables(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesRequest, google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetTable(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.GetTableRequest, google.bigtable.admin.v2.table_pb2.Table]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteTable(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteTableRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ModifyColumnFamilies(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.ModifyColumnFamiliesRequest, google.bigtable.admin.v2.table_pb2.Table]') -> None:
        pass

    @abc.abstractmethod
    async def DropRowRange(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.DropRowRangeRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GenerateConsistencyToken(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.GenerateConsistencyTokenRequest, google.bigtable.admin.v2.bigtable_table_admin_pb2.GenerateConsistencyTokenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CheckConsistency(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.CheckConsistencyRequest, google.bigtable.admin.v2.bigtable_table_admin_pb2.CheckConsistencyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SnapshotTable(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.SnapshotTableRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetSnapshot(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.GetSnapshotRequest, google.bigtable.admin.v2.table_pb2.Snapshot]') -> None:
        pass

    @abc.abstractmethod
    async def ListSnapshots(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.ListSnapshotsRequest, google.bigtable.admin.v2.bigtable_table_admin_pb2.ListSnapshotsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteSnapshot(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteSnapshotRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateBackup(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateBackupRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetBackup(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.GetBackupRequest, google.bigtable.admin.v2.table_pb2.Backup]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateBackup(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.UpdateBackupRequest, google.bigtable.admin.v2.table_pb2.Backup]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteBackup(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteBackupRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ListBackups(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.ListBackupsRequest, google.bigtable.admin.v2.bigtable_table_admin_pb2.ListBackupsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RestoreTable(self, stream: 'grpclib.server.Stream[google.bigtable.admin.v2.bigtable_table_admin_pb2.RestoreTableRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def SetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def TestIamPermissions(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.bigtable.admin.v2.BigtableTableAdmin/CreateTable': grpclib.const.Handler(
                self.CreateTable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateTableRequest,
                google.bigtable.admin.v2.table_pb2.Table,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/CreateTableFromSnapshot': grpclib.const.Handler(
                self.CreateTableFromSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateTableFromSnapshotRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/ListTables': grpclib.const.Handler(
                self.ListTables,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesRequest,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesResponse,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/GetTable': grpclib.const.Handler(
                self.GetTable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.GetTableRequest,
                google.bigtable.admin.v2.table_pb2.Table,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/DeleteTable': grpclib.const.Handler(
                self.DeleteTable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteTableRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/ModifyColumnFamilies': grpclib.const.Handler(
                self.ModifyColumnFamilies,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.ModifyColumnFamiliesRequest,
                google.bigtable.admin.v2.table_pb2.Table,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/DropRowRange': grpclib.const.Handler(
                self.DropRowRange,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.DropRowRangeRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/GenerateConsistencyToken': grpclib.const.Handler(
                self.GenerateConsistencyToken,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.GenerateConsistencyTokenRequest,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.GenerateConsistencyTokenResponse,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/CheckConsistency': grpclib.const.Handler(
                self.CheckConsistency,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.CheckConsistencyRequest,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.CheckConsistencyResponse,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/SnapshotTable': grpclib.const.Handler(
                self.SnapshotTable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.SnapshotTableRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/GetSnapshot': grpclib.const.Handler(
                self.GetSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.GetSnapshotRequest,
                google.bigtable.admin.v2.table_pb2.Snapshot,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/ListSnapshots': grpclib.const.Handler(
                self.ListSnapshots,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.ListSnapshotsRequest,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.ListSnapshotsResponse,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/DeleteSnapshot': grpclib.const.Handler(
                self.DeleteSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteSnapshotRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/CreateBackup': grpclib.const.Handler(
                self.CreateBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateBackupRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/GetBackup': grpclib.const.Handler(
                self.GetBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.GetBackupRequest,
                google.bigtable.admin.v2.table_pb2.Backup,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/UpdateBackup': grpclib.const.Handler(
                self.UpdateBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.UpdateBackupRequest,
                google.bigtable.admin.v2.table_pb2.Backup,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/DeleteBackup': grpclib.const.Handler(
                self.DeleteBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteBackupRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/ListBackups': grpclib.const.Handler(
                self.ListBackups,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.ListBackupsRequest,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.ListBackupsResponse,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/RestoreTable': grpclib.const.Handler(
                self.RestoreTable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.bigtable.admin.v2.bigtable_table_admin_pb2.RestoreTableRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/GetIamPolicy': grpclib.const.Handler(
                self.GetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/SetIamPolicy': grpclib.const.Handler(
                self.SetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.bigtable.admin.v2.BigtableTableAdmin/TestIamPermissions': grpclib.const.Handler(
                self.TestIamPermissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
            ),
        }


class BigtableTableAdminStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateTable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/CreateTable',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateTableRequest,
            google.bigtable.admin.v2.table_pb2.Table,
        )
        self.CreateTableFromSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/CreateTableFromSnapshot',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateTableFromSnapshotRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListTables = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/ListTables',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesRequest,
            google.bigtable.admin.v2.bigtable_table_admin_pb2.ListTablesResponse,
        )
        self.GetTable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/GetTable',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.GetTableRequest,
            google.bigtable.admin.v2.table_pb2.Table,
        )
        self.DeleteTable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/DeleteTable',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteTableRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ModifyColumnFamilies = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/ModifyColumnFamilies',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.ModifyColumnFamiliesRequest,
            google.bigtable.admin.v2.table_pb2.Table,
        )
        self.DropRowRange = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/DropRowRange',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.DropRowRangeRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GenerateConsistencyToken = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/GenerateConsistencyToken',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.GenerateConsistencyTokenRequest,
            google.bigtable.admin.v2.bigtable_table_admin_pb2.GenerateConsistencyTokenResponse,
        )
        self.CheckConsistency = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/CheckConsistency',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.CheckConsistencyRequest,
            google.bigtable.admin.v2.bigtable_table_admin_pb2.CheckConsistencyResponse,
        )
        self.SnapshotTable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/SnapshotTable',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.SnapshotTableRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/GetSnapshot',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.GetSnapshotRequest,
            google.bigtable.admin.v2.table_pb2.Snapshot,
        )
        self.ListSnapshots = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/ListSnapshots',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.ListSnapshotsRequest,
            google.bigtable.admin.v2.bigtable_table_admin_pb2.ListSnapshotsResponse,
        )
        self.DeleteSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/DeleteSnapshot',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteSnapshotRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/CreateBackup',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.CreateBackupRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/GetBackup',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.GetBackupRequest,
            google.bigtable.admin.v2.table_pb2.Backup,
        )
        self.UpdateBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/UpdateBackup',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.UpdateBackupRequest,
            google.bigtable.admin.v2.table_pb2.Backup,
        )
        self.DeleteBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/DeleteBackup',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.DeleteBackupRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ListBackups = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/ListBackups',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.ListBackupsRequest,
            google.bigtable.admin.v2.bigtable_table_admin_pb2.ListBackupsResponse,
        )
        self.RestoreTable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/RestoreTable',
            google.bigtable.admin.v2.bigtable_table_admin_pb2.RestoreTableRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/GetIamPolicy',
            google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.SetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/SetIamPolicy',
            google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.TestIamPermissions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.bigtable.admin.v2.BigtableTableAdmin/TestIamPermissions',
            google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
        )
