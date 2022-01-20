# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/baremetalsolution/v2/baremetalsolution.proto
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
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.baremetalsolution.v2.baremetalsolution_pb2


class BareMetalSolutionBase(abc.ABC):

    @abc.abstractmethod
    async def ListInstances(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListInstancesRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListInstancesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetInstance(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetInstanceRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Instance]') -> None:
        pass

    @abc.abstractmethod
    async def ResetInstance(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ResetInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListVolumes(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumesRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetVolume(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetVolumeRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Volume]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateVolume(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.UpdateVolumeRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListNetworks(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListNetworksRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListNetworksResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetNetwork(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetNetworkRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Network]') -> None:
        pass

    @abc.abstractmethod
    async def ListSnapshotSchedulePolicies(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListSnapshotSchedulePoliciesRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListSnapshotSchedulePoliciesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSnapshotSchedulePolicy(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetSnapshotSchedulePolicyRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.SnapshotSchedulePolicy]') -> None:
        pass

    @abc.abstractmethod
    async def CreateSnapshotSchedulePolicy(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.CreateSnapshotSchedulePolicyRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.SnapshotSchedulePolicy]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateSnapshotSchedulePolicy(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.UpdateSnapshotSchedulePolicyRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.SnapshotSchedulePolicy]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteSnapshotSchedulePolicy(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.DeleteSnapshotSchedulePolicyRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateVolumeSnapshot(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.CreateVolumeSnapshotRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.VolumeSnapshot]') -> None:
        pass

    @abc.abstractmethod
    async def RestoreVolumeSnapshot(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.RestoreVolumeSnapshotRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteVolumeSnapshot(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.DeleteVolumeSnapshotRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GetVolumeSnapshot(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetVolumeSnapshotRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.VolumeSnapshot]') -> None:
        pass

    @abc.abstractmethod
    async def ListVolumeSnapshots(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumeSnapshotsRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumeSnapshotsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLun(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetLunRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Lun]') -> None:
        pass

    @abc.abstractmethod
    async def ListLuns(self, stream: 'grpclib.server.Stream[google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListLunsRequest, google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListLunsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListInstances': grpclib.const.Handler(
                self.ListInstances,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListInstancesRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListInstancesResponse,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetInstance': grpclib.const.Handler(
                self.GetInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetInstanceRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Instance,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ResetInstance': grpclib.const.Handler(
                self.ResetInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ResetInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListVolumes': grpclib.const.Handler(
                self.ListVolumes,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumesRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumesResponse,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetVolume': grpclib.const.Handler(
                self.GetVolume,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetVolumeRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Volume,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/UpdateVolume': grpclib.const.Handler(
                self.UpdateVolume,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.UpdateVolumeRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListNetworks': grpclib.const.Handler(
                self.ListNetworks,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListNetworksRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListNetworksResponse,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetNetwork': grpclib.const.Handler(
                self.GetNetwork,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetNetworkRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Network,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListSnapshotSchedulePolicies': grpclib.const.Handler(
                self.ListSnapshotSchedulePolicies,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListSnapshotSchedulePoliciesRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListSnapshotSchedulePoliciesResponse,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetSnapshotSchedulePolicy': grpclib.const.Handler(
                self.GetSnapshotSchedulePolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetSnapshotSchedulePolicyRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.SnapshotSchedulePolicy,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/CreateSnapshotSchedulePolicy': grpclib.const.Handler(
                self.CreateSnapshotSchedulePolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.CreateSnapshotSchedulePolicyRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.SnapshotSchedulePolicy,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/UpdateSnapshotSchedulePolicy': grpclib.const.Handler(
                self.UpdateSnapshotSchedulePolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.UpdateSnapshotSchedulePolicyRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.SnapshotSchedulePolicy,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/DeleteSnapshotSchedulePolicy': grpclib.const.Handler(
                self.DeleteSnapshotSchedulePolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.DeleteSnapshotSchedulePolicyRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/CreateVolumeSnapshot': grpclib.const.Handler(
                self.CreateVolumeSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.CreateVolumeSnapshotRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.VolumeSnapshot,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/RestoreVolumeSnapshot': grpclib.const.Handler(
                self.RestoreVolumeSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.RestoreVolumeSnapshotRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/DeleteVolumeSnapshot': grpclib.const.Handler(
                self.DeleteVolumeSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.DeleteVolumeSnapshotRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetVolumeSnapshot': grpclib.const.Handler(
                self.GetVolumeSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetVolumeSnapshotRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.VolumeSnapshot,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListVolumeSnapshots': grpclib.const.Handler(
                self.ListVolumeSnapshots,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumeSnapshotsRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumeSnapshotsResponse,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetLun': grpclib.const.Handler(
                self.GetLun,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetLunRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Lun,
            ),
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListLuns': grpclib.const.Handler(
                self.ListLuns,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListLunsRequest,
                google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListLunsResponse,
            ),
        }


class BareMetalSolutionStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListInstances = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListInstances',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListInstancesRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListInstancesResponse,
        )
        self.GetInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetInstance',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetInstanceRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Instance,
        )
        self.ResetInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ResetInstance',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ResetInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListVolumes = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListVolumes',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumesRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumesResponse,
        )
        self.GetVolume = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetVolume',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetVolumeRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Volume,
        )
        self.UpdateVolume = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/UpdateVolume',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.UpdateVolumeRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListNetworks = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListNetworks',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListNetworksRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListNetworksResponse,
        )
        self.GetNetwork = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetNetwork',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetNetworkRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Network,
        )
        self.ListSnapshotSchedulePolicies = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListSnapshotSchedulePolicies',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListSnapshotSchedulePoliciesRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListSnapshotSchedulePoliciesResponse,
        )
        self.GetSnapshotSchedulePolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetSnapshotSchedulePolicy',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetSnapshotSchedulePolicyRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.SnapshotSchedulePolicy,
        )
        self.CreateSnapshotSchedulePolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/CreateSnapshotSchedulePolicy',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.CreateSnapshotSchedulePolicyRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.SnapshotSchedulePolicy,
        )
        self.UpdateSnapshotSchedulePolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/UpdateSnapshotSchedulePolicy',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.UpdateSnapshotSchedulePolicyRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.SnapshotSchedulePolicy,
        )
        self.DeleteSnapshotSchedulePolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/DeleteSnapshotSchedulePolicy',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.DeleteSnapshotSchedulePolicyRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateVolumeSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/CreateVolumeSnapshot',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.CreateVolumeSnapshotRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.VolumeSnapshot,
        )
        self.RestoreVolumeSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/RestoreVolumeSnapshot',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.RestoreVolumeSnapshotRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteVolumeSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/DeleteVolumeSnapshot',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.DeleteVolumeSnapshotRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GetVolumeSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetVolumeSnapshot',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetVolumeSnapshotRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.VolumeSnapshot,
        )
        self.ListVolumeSnapshots = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListVolumeSnapshots',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumeSnapshotsRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListVolumeSnapshotsResponse,
        )
        self.GetLun = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/GetLun',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.GetLunRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.Lun,
        )
        self.ListLuns = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.baremetalsolution.v2.BareMetalSolution/ListLuns',
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListLunsRequest,
            google.cloud.baremetalsolution.v2.baremetalsolution_pb2.ListLunsResponse,
        )
