# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/devtools/containeranalysis/v1beta1/containeranalysis.proto
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
import google.iam.v1.iam_policy_pb2
import google.iam.v1.policy_pb2
import google.protobuf.timestamp_pb2
import google.devtools.containeranalysis.v1beta1.containeranalysis_pb2


class ContainerAnalysisV1Beta1Base(abc.ABC):

    @abc.abstractmethod
    async def SetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def GetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def TestIamPermissions(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetScanConfig(self, stream: 'grpclib.server.Stream[google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.GetScanConfigRequest, google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ScanConfig]') -> None:
        pass

    @abc.abstractmethod
    async def ListScanConfigs(self, stream: 'grpclib.server.Stream[google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ListScanConfigsRequest, google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ListScanConfigsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateScanConfig(self, stream: 'grpclib.server.Stream[google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.UpdateScanConfigRequest, google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ScanConfig]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/SetIamPolicy': grpclib.const.Handler(
                self.SetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/GetIamPolicy': grpclib.const.Handler(
                self.GetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/TestIamPermissions': grpclib.const.Handler(
                self.TestIamPermissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
            ),
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/GetScanConfig': grpclib.const.Handler(
                self.GetScanConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.GetScanConfigRequest,
                google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ScanConfig,
            ),
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/ListScanConfigs': grpclib.const.Handler(
                self.ListScanConfigs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ListScanConfigsRequest,
                google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ListScanConfigsResponse,
            ),
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/UpdateScanConfig': grpclib.const.Handler(
                self.UpdateScanConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.UpdateScanConfigRequest,
                google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ScanConfig,
            ),
        }


class ContainerAnalysisV1Beta1Stub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/SetIamPolicy',
            google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.GetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/GetIamPolicy',
            google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.TestIamPermissions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/TestIamPermissions',
            google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
        )
        self.GetScanConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/GetScanConfig',
            google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.GetScanConfigRequest,
            google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ScanConfig,
        )
        self.ListScanConfigs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/ListScanConfigs',
            google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ListScanConfigsRequest,
            google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ListScanConfigsResponse,
        )
        self.UpdateScanConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1/UpdateScanConfig',
            google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.UpdateScanConfigRequest,
            google.devtools.containeranalysis.v1beta1.containeranalysis_pb2.ScanConfig,
        )
