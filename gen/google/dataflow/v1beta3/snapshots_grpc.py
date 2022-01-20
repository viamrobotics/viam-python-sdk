# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/dataflow/v1beta3/snapshots.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.protobuf.duration_pb2
import google.protobuf.timestamp_pb2
import google.api.client_pb2
import google.dataflow.v1beta3.snapshots_pb2


class SnapshotsV1Beta3Base(abc.ABC):

    @abc.abstractmethod
    async def GetSnapshot(self, stream: 'grpclib.server.Stream[google.dataflow.v1beta3.snapshots_pb2.GetSnapshotRequest, google.dataflow.v1beta3.snapshots_pb2.Snapshot]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteSnapshot(self, stream: 'grpclib.server.Stream[google.dataflow.v1beta3.snapshots_pb2.DeleteSnapshotRequest, google.dataflow.v1beta3.snapshots_pb2.DeleteSnapshotResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListSnapshots(self, stream: 'grpclib.server.Stream[google.dataflow.v1beta3.snapshots_pb2.ListSnapshotsRequest, google.dataflow.v1beta3.snapshots_pb2.ListSnapshotsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.dataflow.v1beta3.SnapshotsV1Beta3/GetSnapshot': grpclib.const.Handler(
                self.GetSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.dataflow.v1beta3.snapshots_pb2.GetSnapshotRequest,
                google.dataflow.v1beta3.snapshots_pb2.Snapshot,
            ),
            '/google.dataflow.v1beta3.SnapshotsV1Beta3/DeleteSnapshot': grpclib.const.Handler(
                self.DeleteSnapshot,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.dataflow.v1beta3.snapshots_pb2.DeleteSnapshotRequest,
                google.dataflow.v1beta3.snapshots_pb2.DeleteSnapshotResponse,
            ),
            '/google.dataflow.v1beta3.SnapshotsV1Beta3/ListSnapshots': grpclib.const.Handler(
                self.ListSnapshots,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.dataflow.v1beta3.snapshots_pb2.ListSnapshotsRequest,
                google.dataflow.v1beta3.snapshots_pb2.ListSnapshotsResponse,
            ),
        }


class SnapshotsV1Beta3Stub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.dataflow.v1beta3.SnapshotsV1Beta3/GetSnapshot',
            google.dataflow.v1beta3.snapshots_pb2.GetSnapshotRequest,
            google.dataflow.v1beta3.snapshots_pb2.Snapshot,
        )
        self.DeleteSnapshot = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.dataflow.v1beta3.SnapshotsV1Beta3/DeleteSnapshot',
            google.dataflow.v1beta3.snapshots_pb2.DeleteSnapshotRequest,
            google.dataflow.v1beta3.snapshots_pb2.DeleteSnapshotResponse,
        )
        self.ListSnapshots = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.dataflow.v1beta3.SnapshotsV1Beta3/ListSnapshots',
            google.dataflow.v1beta3.snapshots_pb2.ListSnapshotsRequest,
            google.dataflow.v1beta3.snapshots_pb2.ListSnapshotsResponse,
        )
