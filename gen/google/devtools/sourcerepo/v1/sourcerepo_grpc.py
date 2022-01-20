# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/devtools/sourcerepo/v1/sourcerepo.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.iam.v1.iam_policy_pb2
import google.iam.v1.policy_pb2
import google.protobuf.empty_pb2
import google.devtools.sourcerepo.v1.sourcerepo_pb2


class SourceRepoBase(abc.ABC):

    @abc.abstractmethod
    async def ListRepos(self, stream: 'grpclib.server.Stream[google.devtools.sourcerepo.v1.sourcerepo_pb2.ListReposRequest, google.devtools.sourcerepo.v1.sourcerepo_pb2.ListReposResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRepo(self, stream: 'grpclib.server.Stream[google.devtools.sourcerepo.v1.sourcerepo_pb2.GetRepoRequest, google.devtools.sourcerepo.v1.sourcerepo_pb2.Repo]') -> None:
        pass

    @abc.abstractmethod
    async def CreateRepo(self, stream: 'grpclib.server.Stream[google.devtools.sourcerepo.v1.sourcerepo_pb2.CreateRepoRequest, google.devtools.sourcerepo.v1.sourcerepo_pb2.Repo]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteRepo(self, stream: 'grpclib.server.Stream[google.devtools.sourcerepo.v1.sourcerepo_pb2.DeleteRepoRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def SetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def GetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def TestIamPermissions(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.devtools.sourcerepo.v1.SourceRepo/ListRepos': grpclib.const.Handler(
                self.ListRepos,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.sourcerepo.v1.sourcerepo_pb2.ListReposRequest,
                google.devtools.sourcerepo.v1.sourcerepo_pb2.ListReposResponse,
            ),
            '/google.devtools.sourcerepo.v1.SourceRepo/GetRepo': grpclib.const.Handler(
                self.GetRepo,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.sourcerepo.v1.sourcerepo_pb2.GetRepoRequest,
                google.devtools.sourcerepo.v1.sourcerepo_pb2.Repo,
            ),
            '/google.devtools.sourcerepo.v1.SourceRepo/CreateRepo': grpclib.const.Handler(
                self.CreateRepo,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.sourcerepo.v1.sourcerepo_pb2.CreateRepoRequest,
                google.devtools.sourcerepo.v1.sourcerepo_pb2.Repo,
            ),
            '/google.devtools.sourcerepo.v1.SourceRepo/DeleteRepo': grpclib.const.Handler(
                self.DeleteRepo,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.sourcerepo.v1.sourcerepo_pb2.DeleteRepoRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.devtools.sourcerepo.v1.SourceRepo/SetIamPolicy': grpclib.const.Handler(
                self.SetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.devtools.sourcerepo.v1.SourceRepo/GetIamPolicy': grpclib.const.Handler(
                self.GetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.devtools.sourcerepo.v1.SourceRepo/TestIamPermissions': grpclib.const.Handler(
                self.TestIamPermissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
            ),
        }


class SourceRepoStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListRepos = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.sourcerepo.v1.SourceRepo/ListRepos',
            google.devtools.sourcerepo.v1.sourcerepo_pb2.ListReposRequest,
            google.devtools.sourcerepo.v1.sourcerepo_pb2.ListReposResponse,
        )
        self.GetRepo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.sourcerepo.v1.SourceRepo/GetRepo',
            google.devtools.sourcerepo.v1.sourcerepo_pb2.GetRepoRequest,
            google.devtools.sourcerepo.v1.sourcerepo_pb2.Repo,
        )
        self.CreateRepo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.sourcerepo.v1.SourceRepo/CreateRepo',
            google.devtools.sourcerepo.v1.sourcerepo_pb2.CreateRepoRequest,
            google.devtools.sourcerepo.v1.sourcerepo_pb2.Repo,
        )
        self.DeleteRepo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.sourcerepo.v1.SourceRepo/DeleteRepo',
            google.devtools.sourcerepo.v1.sourcerepo_pb2.DeleteRepoRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.SetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.sourcerepo.v1.SourceRepo/SetIamPolicy',
            google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.GetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.sourcerepo.v1.SourceRepo/GetIamPolicy',
            google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.TestIamPermissions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.sourcerepo.v1.SourceRepo/TestIamPermissions',
            google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
        )
