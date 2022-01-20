# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/networkmanagement/v1/reachability.proto
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
import google.cloud.networkmanagement.v1.connectivity_test_pb2
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.networkmanagement.v1.reachability_pb2


class ReachabilityServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListConnectivityTests(self, stream: 'grpclib.server.Stream[google.cloud.networkmanagement.v1.reachability_pb2.ListConnectivityTestsRequest, google.cloud.networkmanagement.v1.reachability_pb2.ListConnectivityTestsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetConnectivityTest(self, stream: 'grpclib.server.Stream[google.cloud.networkmanagement.v1.reachability_pb2.GetConnectivityTestRequest, google.cloud.networkmanagement.v1.connectivity_test_pb2.ConnectivityTest]') -> None:
        pass

    @abc.abstractmethod
    async def CreateConnectivityTest(self, stream: 'grpclib.server.Stream[google.cloud.networkmanagement.v1.reachability_pb2.CreateConnectivityTestRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateConnectivityTest(self, stream: 'grpclib.server.Stream[google.cloud.networkmanagement.v1.reachability_pb2.UpdateConnectivityTestRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def RerunConnectivityTest(self, stream: 'grpclib.server.Stream[google.cloud.networkmanagement.v1.reachability_pb2.RerunConnectivityTestRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteConnectivityTest(self, stream: 'grpclib.server.Stream[google.cloud.networkmanagement.v1.reachability_pb2.DeleteConnectivityTestRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.networkmanagement.v1.ReachabilityService/ListConnectivityTests': grpclib.const.Handler(
                self.ListConnectivityTests,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.networkmanagement.v1.reachability_pb2.ListConnectivityTestsRequest,
                google.cloud.networkmanagement.v1.reachability_pb2.ListConnectivityTestsResponse,
            ),
            '/google.cloud.networkmanagement.v1.ReachabilityService/GetConnectivityTest': grpclib.const.Handler(
                self.GetConnectivityTest,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.networkmanagement.v1.reachability_pb2.GetConnectivityTestRequest,
                google.cloud.networkmanagement.v1.connectivity_test_pb2.ConnectivityTest,
            ),
            '/google.cloud.networkmanagement.v1.ReachabilityService/CreateConnectivityTest': grpclib.const.Handler(
                self.CreateConnectivityTest,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.networkmanagement.v1.reachability_pb2.CreateConnectivityTestRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.networkmanagement.v1.ReachabilityService/UpdateConnectivityTest': grpclib.const.Handler(
                self.UpdateConnectivityTest,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.networkmanagement.v1.reachability_pb2.UpdateConnectivityTestRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.networkmanagement.v1.ReachabilityService/RerunConnectivityTest': grpclib.const.Handler(
                self.RerunConnectivityTest,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.networkmanagement.v1.reachability_pb2.RerunConnectivityTestRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.networkmanagement.v1.ReachabilityService/DeleteConnectivityTest': grpclib.const.Handler(
                self.DeleteConnectivityTest,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.networkmanagement.v1.reachability_pb2.DeleteConnectivityTestRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class ReachabilityServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListConnectivityTests = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.networkmanagement.v1.ReachabilityService/ListConnectivityTests',
            google.cloud.networkmanagement.v1.reachability_pb2.ListConnectivityTestsRequest,
            google.cloud.networkmanagement.v1.reachability_pb2.ListConnectivityTestsResponse,
        )
        self.GetConnectivityTest = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.networkmanagement.v1.ReachabilityService/GetConnectivityTest',
            google.cloud.networkmanagement.v1.reachability_pb2.GetConnectivityTestRequest,
            google.cloud.networkmanagement.v1.connectivity_test_pb2.ConnectivityTest,
        )
        self.CreateConnectivityTest = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.networkmanagement.v1.ReachabilityService/CreateConnectivityTest',
            google.cloud.networkmanagement.v1.reachability_pb2.CreateConnectivityTestRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateConnectivityTest = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.networkmanagement.v1.ReachabilityService/UpdateConnectivityTest',
            google.cloud.networkmanagement.v1.reachability_pb2.UpdateConnectivityTestRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.RerunConnectivityTest = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.networkmanagement.v1.ReachabilityService/RerunConnectivityTest',
            google.cloud.networkmanagement.v1.reachability_pb2.RerunConnectivityTestRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteConnectivityTest = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.networkmanagement.v1.ReachabilityService/DeleteConnectivityTest',
            google.cloud.networkmanagement.v1.reachability_pb2.DeleteConnectivityTestRequest,
            google.longrunning.operations_pb2.Operation,
        )
