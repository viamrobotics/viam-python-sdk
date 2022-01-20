# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/datacatalog/v1beta1/datacatalog.proto
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
import google.cloud.datacatalog.v1beta1.common_pb2
import google.cloud.datacatalog.v1beta1.gcs_fileset_spec_pb2
import google.cloud.datacatalog.v1beta1.schema_pb2
import google.cloud.datacatalog.v1beta1.search_pb2
import google.cloud.datacatalog.v1beta1.table_spec_pb2
import google.cloud.datacatalog.v1beta1.tags_pb2
import google.cloud.datacatalog.v1beta1.timestamps_pb2
import google.iam.v1.iam_policy_pb2
import google.iam.v1.policy_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.cloud.datacatalog.v1beta1.datacatalog_pb2


class DataCatalogBase(abc.ABC):

    @abc.abstractmethod
    async def SearchCatalog(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.SearchCatalogRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.SearchCatalogResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateEntryGroup(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateEntryGroupRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.EntryGroup]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateEntryGroup(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateEntryGroupRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.EntryGroup]') -> None:
        pass

    @abc.abstractmethod
    async def GetEntryGroup(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.GetEntryGroupRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.EntryGroup]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteEntryGroup(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteEntryGroupRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ListEntryGroups(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntryGroupsRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntryGroupsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateEntry(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateEntryRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateEntry(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateEntryRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteEntry(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteEntryRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GetEntry(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.GetEntryRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry]') -> None:
        pass

    @abc.abstractmethod
    async def LookupEntry(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.LookupEntryRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry]') -> None:
        pass

    @abc.abstractmethod
    async def ListEntries(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntriesRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntriesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateTagTemplate(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateTagTemplateRequest, google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def GetTagTemplate(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.GetTagTemplateRequest, google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateTagTemplate(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateTagTemplateRequest, google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteTagTemplate(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteTagTemplateRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateTagTemplateField(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateTagTemplateFieldRequest, google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplateField]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateTagTemplateField(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateTagTemplateFieldRequest, google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplateField]') -> None:
        pass

    @abc.abstractmethod
    async def RenameTagTemplateField(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.RenameTagTemplateFieldRequest, google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplateField]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteTagTemplateField(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteTagTemplateFieldRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateTag(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateTagRequest, google.cloud.datacatalog.v1beta1.tags_pb2.Tag]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateTag(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateTagRequest, google.cloud.datacatalog.v1beta1.tags_pb2.Tag]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteTag(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteTagRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ListTags(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListTagsRequest, google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListTagsResponse]') -> None:
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
            '/google.cloud.datacatalog.v1beta1.DataCatalog/SearchCatalog': grpclib.const.Handler(
                self.SearchCatalog,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.SearchCatalogRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.SearchCatalogResponse,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateEntryGroup': grpclib.const.Handler(
                self.CreateEntryGroup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateEntryGroupRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.EntryGroup,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateEntryGroup': grpclib.const.Handler(
                self.UpdateEntryGroup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateEntryGroupRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.EntryGroup,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/GetEntryGroup': grpclib.const.Handler(
                self.GetEntryGroup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.GetEntryGroupRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.EntryGroup,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteEntryGroup': grpclib.const.Handler(
                self.DeleteEntryGroup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteEntryGroupRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/ListEntryGroups': grpclib.const.Handler(
                self.ListEntryGroups,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntryGroupsRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntryGroupsResponse,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateEntry': grpclib.const.Handler(
                self.CreateEntry,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateEntryRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateEntry': grpclib.const.Handler(
                self.UpdateEntry,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateEntryRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteEntry': grpclib.const.Handler(
                self.DeleteEntry,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteEntryRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/GetEntry': grpclib.const.Handler(
                self.GetEntry,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.GetEntryRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/LookupEntry': grpclib.const.Handler(
                self.LookupEntry,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.LookupEntryRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/ListEntries': grpclib.const.Handler(
                self.ListEntries,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntriesRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntriesResponse,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateTagTemplate': grpclib.const.Handler(
                self.CreateTagTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateTagTemplateRequest,
                google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplate,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/GetTagTemplate': grpclib.const.Handler(
                self.GetTagTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.GetTagTemplateRequest,
                google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplate,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateTagTemplate': grpclib.const.Handler(
                self.UpdateTagTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateTagTemplateRequest,
                google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplate,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteTagTemplate': grpclib.const.Handler(
                self.DeleteTagTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteTagTemplateRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateTagTemplateField': grpclib.const.Handler(
                self.CreateTagTemplateField,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateTagTemplateFieldRequest,
                google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplateField,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateTagTemplateField': grpclib.const.Handler(
                self.UpdateTagTemplateField,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateTagTemplateFieldRequest,
                google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplateField,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/RenameTagTemplateField': grpclib.const.Handler(
                self.RenameTagTemplateField,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.RenameTagTemplateFieldRequest,
                google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplateField,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteTagTemplateField': grpclib.const.Handler(
                self.DeleteTagTemplateField,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteTagTemplateFieldRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateTag': grpclib.const.Handler(
                self.CreateTag,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateTagRequest,
                google.cloud.datacatalog.v1beta1.tags_pb2.Tag,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateTag': grpclib.const.Handler(
                self.UpdateTag,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateTagRequest,
                google.cloud.datacatalog.v1beta1.tags_pb2.Tag,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteTag': grpclib.const.Handler(
                self.DeleteTag,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteTagRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/ListTags': grpclib.const.Handler(
                self.ListTags,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListTagsRequest,
                google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListTagsResponse,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/SetIamPolicy': grpclib.const.Handler(
                self.SetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/GetIamPolicy': grpclib.const.Handler(
                self.GetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.datacatalog.v1beta1.DataCatalog/TestIamPermissions': grpclib.const.Handler(
                self.TestIamPermissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
            ),
        }


class DataCatalogStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SearchCatalog = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/SearchCatalog',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.SearchCatalogRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.SearchCatalogResponse,
        )
        self.CreateEntryGroup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateEntryGroup',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateEntryGroupRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.EntryGroup,
        )
        self.UpdateEntryGroup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateEntryGroup',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateEntryGroupRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.EntryGroup,
        )
        self.GetEntryGroup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/GetEntryGroup',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.GetEntryGroupRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.EntryGroup,
        )
        self.DeleteEntryGroup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteEntryGroup',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteEntryGroupRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ListEntryGroups = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/ListEntryGroups',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntryGroupsRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntryGroupsResponse,
        )
        self.CreateEntry = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateEntry',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateEntryRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry,
        )
        self.UpdateEntry = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateEntry',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateEntryRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry,
        )
        self.DeleteEntry = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteEntry',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteEntryRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GetEntry = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/GetEntry',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.GetEntryRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry,
        )
        self.LookupEntry = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/LookupEntry',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.LookupEntryRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.Entry,
        )
        self.ListEntries = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/ListEntries',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntriesRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListEntriesResponse,
        )
        self.CreateTagTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateTagTemplate',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateTagTemplateRequest,
            google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplate,
        )
        self.GetTagTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/GetTagTemplate',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.GetTagTemplateRequest,
            google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplate,
        )
        self.UpdateTagTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateTagTemplate',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateTagTemplateRequest,
            google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplate,
        )
        self.DeleteTagTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteTagTemplate',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteTagTemplateRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateTagTemplateField = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateTagTemplateField',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateTagTemplateFieldRequest,
            google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplateField,
        )
        self.UpdateTagTemplateField = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateTagTemplateField',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateTagTemplateFieldRequest,
            google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplateField,
        )
        self.RenameTagTemplateField = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/RenameTagTemplateField',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.RenameTagTemplateFieldRequest,
            google.cloud.datacatalog.v1beta1.tags_pb2.TagTemplateField,
        )
        self.DeleteTagTemplateField = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteTagTemplateField',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteTagTemplateFieldRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateTag = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/CreateTag',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.CreateTagRequest,
            google.cloud.datacatalog.v1beta1.tags_pb2.Tag,
        )
        self.UpdateTag = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/UpdateTag',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.UpdateTagRequest,
            google.cloud.datacatalog.v1beta1.tags_pb2.Tag,
        )
        self.DeleteTag = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/DeleteTag',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.DeleteTagRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ListTags = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/ListTags',
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListTagsRequest,
            google.cloud.datacatalog.v1beta1.datacatalog_pb2.ListTagsResponse,
        )
        self.SetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/SetIamPolicy',
            google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.GetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/GetIamPolicy',
            google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.TestIamPermissions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1beta1.DataCatalog/TestIamPermissions',
            google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
        )
