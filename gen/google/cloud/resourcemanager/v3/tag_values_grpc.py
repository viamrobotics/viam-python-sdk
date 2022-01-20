# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/resourcemanager/v3/tag_values.proto
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
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.resourcemanager.v3.tag_values_pb2


class TagValuesBase(abc.ABC):

    @abc.abstractmethod
    async def ListTagValues(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v3.tag_values_pb2.ListTagValuesRequest, google.cloud.resourcemanager.v3.tag_values_pb2.ListTagValuesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetTagValue(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v3.tag_values_pb2.GetTagValueRequest, google.cloud.resourcemanager.v3.tag_values_pb2.TagValue]') -> None:
        pass

    @abc.abstractmethod
    async def CreateTagValue(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v3.tag_values_pb2.CreateTagValueRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateTagValue(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v3.tag_values_pb2.UpdateTagValueRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteTagValue(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v3.tag_values_pb2.DeleteTagValueRequest, google.longrunning.operations_pb2.Operation]') -> None:
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
            '/google.cloud.resourcemanager.v3.TagValues/ListTagValues': grpclib.const.Handler(
                self.ListTagValues,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v3.tag_values_pb2.ListTagValuesRequest,
                google.cloud.resourcemanager.v3.tag_values_pb2.ListTagValuesResponse,
            ),
            '/google.cloud.resourcemanager.v3.TagValues/GetTagValue': grpclib.const.Handler(
                self.GetTagValue,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v3.tag_values_pb2.GetTagValueRequest,
                google.cloud.resourcemanager.v3.tag_values_pb2.TagValue,
            ),
            '/google.cloud.resourcemanager.v3.TagValues/CreateTagValue': grpclib.const.Handler(
                self.CreateTagValue,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v3.tag_values_pb2.CreateTagValueRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.resourcemanager.v3.TagValues/UpdateTagValue': grpclib.const.Handler(
                self.UpdateTagValue,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v3.tag_values_pb2.UpdateTagValueRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.resourcemanager.v3.TagValues/DeleteTagValue': grpclib.const.Handler(
                self.DeleteTagValue,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v3.tag_values_pb2.DeleteTagValueRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.resourcemanager.v3.TagValues/GetIamPolicy': grpclib.const.Handler(
                self.GetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.resourcemanager.v3.TagValues/SetIamPolicy': grpclib.const.Handler(
                self.SetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.resourcemanager.v3.TagValues/TestIamPermissions': grpclib.const.Handler(
                self.TestIamPermissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
            ),
        }


class TagValuesStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListTagValues = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v3.TagValues/ListTagValues',
            google.cloud.resourcemanager.v3.tag_values_pb2.ListTagValuesRequest,
            google.cloud.resourcemanager.v3.tag_values_pb2.ListTagValuesResponse,
        )
        self.GetTagValue = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v3.TagValues/GetTagValue',
            google.cloud.resourcemanager.v3.tag_values_pb2.GetTagValueRequest,
            google.cloud.resourcemanager.v3.tag_values_pb2.TagValue,
        )
        self.CreateTagValue = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v3.TagValues/CreateTagValue',
            google.cloud.resourcemanager.v3.tag_values_pb2.CreateTagValueRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateTagValue = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v3.TagValues/UpdateTagValue',
            google.cloud.resourcemanager.v3.tag_values_pb2.UpdateTagValueRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteTagValue = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v3.TagValues/DeleteTagValue',
            google.cloud.resourcemanager.v3.tag_values_pb2.DeleteTagValueRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v3.TagValues/GetIamPolicy',
            google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.SetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v3.TagValues/SetIamPolicy',
            google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.TestIamPermissions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v3.TagValues/TestIamPermissions',
            google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
        )
