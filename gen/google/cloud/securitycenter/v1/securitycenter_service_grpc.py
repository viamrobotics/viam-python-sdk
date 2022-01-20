# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/securitycenter/v1/securitycenter_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.cloud.securitycenter.v1.run_asset_discovery_response_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.cloud.securitycenter.v1.asset_pb2
import google.cloud.securitycenter.v1.external_system_pb2
import google.cloud.securitycenter.v1.finding_pb2
import google.cloud.securitycenter.v1.folder_pb2
import google.cloud.securitycenter.v1.mute_config_pb2
import google.cloud.securitycenter.v1.notification_config_pb2
import google.cloud.securitycenter.v1.organization_settings_pb2
import google.cloud.securitycenter.v1.security_marks_pb2
import google.cloud.securitycenter.v1.source_pb2
import google.iam.v1.iam_policy_pb2
import google.iam.v1.policy_pb2
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.cloud.securitycenter.v1.securitycenter_service_pb2


class SecurityCenterBase(abc.ABC):

    @abc.abstractmethod
    async def BulkMuteFindings(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.BulkMuteFindingsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def CreateSource(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateSourceRequest, google.cloud.securitycenter.v1.source_pb2.Source]') -> None:
        pass

    @abc.abstractmethod
    async def CreateFinding(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateFindingRequest, google.cloud.securitycenter.v1.finding_pb2.Finding]') -> None:
        pass

    @abc.abstractmethod
    async def CreateMuteConfig(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateMuteConfigRequest, google.cloud.securitycenter.v1.mute_config_pb2.MuteConfig]') -> None:
        pass

    @abc.abstractmethod
    async def CreateNotificationConfig(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateNotificationConfigRequest, google.cloud.securitycenter.v1.notification_config_pb2.NotificationConfig]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteMuteConfig(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.DeleteMuteConfigRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteNotificationConfig(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.DeleteNotificationConfigRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def GetMuteConfig(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.GetMuteConfigRequest, google.cloud.securitycenter.v1.mute_config_pb2.MuteConfig]') -> None:
        pass

    @abc.abstractmethod
    async def GetNotificationConfig(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.GetNotificationConfigRequest, google.cloud.securitycenter.v1.notification_config_pb2.NotificationConfig]') -> None:
        pass

    @abc.abstractmethod
    async def GetOrganizationSettings(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.GetOrganizationSettingsRequest, google.cloud.securitycenter.v1.organization_settings_pb2.OrganizationSettings]') -> None:
        pass

    @abc.abstractmethod
    async def GetSource(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.GetSourceRequest, google.cloud.securitycenter.v1.source_pb2.Source]') -> None:
        pass

    @abc.abstractmethod
    async def GroupAssets(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupAssetsRequest, google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupAssetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GroupFindings(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupFindingsRequest, google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupFindingsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListAssets(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.ListAssetsRequest, google.cloud.securitycenter.v1.securitycenter_service_pb2.ListAssetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListFindings(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.ListFindingsRequest, google.cloud.securitycenter.v1.securitycenter_service_pb2.ListFindingsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListMuteConfigs(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.ListMuteConfigsRequest, google.cloud.securitycenter.v1.securitycenter_service_pb2.ListMuteConfigsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListNotificationConfigs(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.ListNotificationConfigsRequest, google.cloud.securitycenter.v1.securitycenter_service_pb2.ListNotificationConfigsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListSources(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.ListSourcesRequest, google.cloud.securitycenter.v1.securitycenter_service_pb2.ListSourcesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RunAssetDiscovery(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.RunAssetDiscoveryRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def SetFindingState(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.SetFindingStateRequest, google.cloud.securitycenter.v1.finding_pb2.Finding]') -> None:
        pass

    @abc.abstractmethod
    async def SetMute(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.SetMuteRequest, google.cloud.securitycenter.v1.finding_pb2.Finding]') -> None:
        pass

    @abc.abstractmethod
    async def SetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def TestIamPermissions(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateExternalSystem(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateExternalSystemRequest, google.cloud.securitycenter.v1.external_system_pb2.ExternalSystem]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateFinding(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateFindingRequest, google.cloud.securitycenter.v1.finding_pb2.Finding]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateMuteConfig(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateMuteConfigRequest, google.cloud.securitycenter.v1.mute_config_pb2.MuteConfig]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateNotificationConfig(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateNotificationConfigRequest, google.cloud.securitycenter.v1.notification_config_pb2.NotificationConfig]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateOrganizationSettings(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateOrganizationSettingsRequest, google.cloud.securitycenter.v1.organization_settings_pb2.OrganizationSettings]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateSource(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateSourceRequest, google.cloud.securitycenter.v1.source_pb2.Source]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateSecurityMarks(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateSecurityMarksRequest, google.cloud.securitycenter.v1.security_marks_pb2.SecurityMarks]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.securitycenter.v1.SecurityCenter/BulkMuteFindings': grpclib.const.Handler(
                self.BulkMuteFindings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.BulkMuteFindingsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/CreateSource': grpclib.const.Handler(
                self.CreateSource,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateSourceRequest,
                google.cloud.securitycenter.v1.source_pb2.Source,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/CreateFinding': grpclib.const.Handler(
                self.CreateFinding,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateFindingRequest,
                google.cloud.securitycenter.v1.finding_pb2.Finding,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/CreateMuteConfig': grpclib.const.Handler(
                self.CreateMuteConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateMuteConfigRequest,
                google.cloud.securitycenter.v1.mute_config_pb2.MuteConfig,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/CreateNotificationConfig': grpclib.const.Handler(
                self.CreateNotificationConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateNotificationConfigRequest,
                google.cloud.securitycenter.v1.notification_config_pb2.NotificationConfig,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/DeleteMuteConfig': grpclib.const.Handler(
                self.DeleteMuteConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.DeleteMuteConfigRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/DeleteNotificationConfig': grpclib.const.Handler(
                self.DeleteNotificationConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.DeleteNotificationConfigRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/GetIamPolicy': grpclib.const.Handler(
                self.GetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/GetMuteConfig': grpclib.const.Handler(
                self.GetMuteConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.GetMuteConfigRequest,
                google.cloud.securitycenter.v1.mute_config_pb2.MuteConfig,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/GetNotificationConfig': grpclib.const.Handler(
                self.GetNotificationConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.GetNotificationConfigRequest,
                google.cloud.securitycenter.v1.notification_config_pb2.NotificationConfig,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/GetOrganizationSettings': grpclib.const.Handler(
                self.GetOrganizationSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.GetOrganizationSettingsRequest,
                google.cloud.securitycenter.v1.organization_settings_pb2.OrganizationSettings,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/GetSource': grpclib.const.Handler(
                self.GetSource,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.GetSourceRequest,
                google.cloud.securitycenter.v1.source_pb2.Source,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/GroupAssets': grpclib.const.Handler(
                self.GroupAssets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupAssetsRequest,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupAssetsResponse,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/GroupFindings': grpclib.const.Handler(
                self.GroupFindings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupFindingsRequest,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupFindingsResponse,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/ListAssets': grpclib.const.Handler(
                self.ListAssets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListAssetsRequest,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListAssetsResponse,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/ListFindings': grpclib.const.Handler(
                self.ListFindings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListFindingsRequest,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListFindingsResponse,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/ListMuteConfigs': grpclib.const.Handler(
                self.ListMuteConfigs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListMuteConfigsRequest,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListMuteConfigsResponse,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/ListNotificationConfigs': grpclib.const.Handler(
                self.ListNotificationConfigs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListNotificationConfigsRequest,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListNotificationConfigsResponse,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/ListSources': grpclib.const.Handler(
                self.ListSources,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListSourcesRequest,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.ListSourcesResponse,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/RunAssetDiscovery': grpclib.const.Handler(
                self.RunAssetDiscovery,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.RunAssetDiscoveryRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/SetFindingState': grpclib.const.Handler(
                self.SetFindingState,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.SetFindingStateRequest,
                google.cloud.securitycenter.v1.finding_pb2.Finding,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/SetMute': grpclib.const.Handler(
                self.SetMute,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.SetMuteRequest,
                google.cloud.securitycenter.v1.finding_pb2.Finding,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/SetIamPolicy': grpclib.const.Handler(
                self.SetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/TestIamPermissions': grpclib.const.Handler(
                self.TestIamPermissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateExternalSystem': grpclib.const.Handler(
                self.UpdateExternalSystem,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateExternalSystemRequest,
                google.cloud.securitycenter.v1.external_system_pb2.ExternalSystem,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateFinding': grpclib.const.Handler(
                self.UpdateFinding,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateFindingRequest,
                google.cloud.securitycenter.v1.finding_pb2.Finding,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateMuteConfig': grpclib.const.Handler(
                self.UpdateMuteConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateMuteConfigRequest,
                google.cloud.securitycenter.v1.mute_config_pb2.MuteConfig,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateNotificationConfig': grpclib.const.Handler(
                self.UpdateNotificationConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateNotificationConfigRequest,
                google.cloud.securitycenter.v1.notification_config_pb2.NotificationConfig,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateOrganizationSettings': grpclib.const.Handler(
                self.UpdateOrganizationSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateOrganizationSettingsRequest,
                google.cloud.securitycenter.v1.organization_settings_pb2.OrganizationSettings,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateSource': grpclib.const.Handler(
                self.UpdateSource,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateSourceRequest,
                google.cloud.securitycenter.v1.source_pb2.Source,
            ),
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateSecurityMarks': grpclib.const.Handler(
                self.UpdateSecurityMarks,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateSecurityMarksRequest,
                google.cloud.securitycenter.v1.security_marks_pb2.SecurityMarks,
            ),
        }


class SecurityCenterStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.BulkMuteFindings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/BulkMuteFindings',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.BulkMuteFindingsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.CreateSource = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/CreateSource',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateSourceRequest,
            google.cloud.securitycenter.v1.source_pb2.Source,
        )
        self.CreateFinding = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/CreateFinding',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateFindingRequest,
            google.cloud.securitycenter.v1.finding_pb2.Finding,
        )
        self.CreateMuteConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/CreateMuteConfig',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateMuteConfigRequest,
            google.cloud.securitycenter.v1.mute_config_pb2.MuteConfig,
        )
        self.CreateNotificationConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/CreateNotificationConfig',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.CreateNotificationConfigRequest,
            google.cloud.securitycenter.v1.notification_config_pb2.NotificationConfig,
        )
        self.DeleteMuteConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/DeleteMuteConfig',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.DeleteMuteConfigRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.DeleteNotificationConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/DeleteNotificationConfig',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.DeleteNotificationConfigRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/GetIamPolicy',
            google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.GetMuteConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/GetMuteConfig',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.GetMuteConfigRequest,
            google.cloud.securitycenter.v1.mute_config_pb2.MuteConfig,
        )
        self.GetNotificationConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/GetNotificationConfig',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.GetNotificationConfigRequest,
            google.cloud.securitycenter.v1.notification_config_pb2.NotificationConfig,
        )
        self.GetOrganizationSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/GetOrganizationSettings',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.GetOrganizationSettingsRequest,
            google.cloud.securitycenter.v1.organization_settings_pb2.OrganizationSettings,
        )
        self.GetSource = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/GetSource',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.GetSourceRequest,
            google.cloud.securitycenter.v1.source_pb2.Source,
        )
        self.GroupAssets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/GroupAssets',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupAssetsRequest,
            google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupAssetsResponse,
        )
        self.GroupFindings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/GroupFindings',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupFindingsRequest,
            google.cloud.securitycenter.v1.securitycenter_service_pb2.GroupFindingsResponse,
        )
        self.ListAssets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/ListAssets',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListAssetsRequest,
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListAssetsResponse,
        )
        self.ListFindings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/ListFindings',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListFindingsRequest,
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListFindingsResponse,
        )
        self.ListMuteConfigs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/ListMuteConfigs',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListMuteConfigsRequest,
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListMuteConfigsResponse,
        )
        self.ListNotificationConfigs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/ListNotificationConfigs',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListNotificationConfigsRequest,
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListNotificationConfigsResponse,
        )
        self.ListSources = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/ListSources',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListSourcesRequest,
            google.cloud.securitycenter.v1.securitycenter_service_pb2.ListSourcesResponse,
        )
        self.RunAssetDiscovery = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/RunAssetDiscovery',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.RunAssetDiscoveryRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.SetFindingState = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/SetFindingState',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.SetFindingStateRequest,
            google.cloud.securitycenter.v1.finding_pb2.Finding,
        )
        self.SetMute = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/SetMute',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.SetMuteRequest,
            google.cloud.securitycenter.v1.finding_pb2.Finding,
        )
        self.SetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/SetIamPolicy',
            google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.TestIamPermissions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/TestIamPermissions',
            google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
        )
        self.UpdateExternalSystem = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateExternalSystem',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateExternalSystemRequest,
            google.cloud.securitycenter.v1.external_system_pb2.ExternalSystem,
        )
        self.UpdateFinding = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateFinding',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateFindingRequest,
            google.cloud.securitycenter.v1.finding_pb2.Finding,
        )
        self.UpdateMuteConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateMuteConfig',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateMuteConfigRequest,
            google.cloud.securitycenter.v1.mute_config_pb2.MuteConfig,
        )
        self.UpdateNotificationConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateNotificationConfig',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateNotificationConfigRequest,
            google.cloud.securitycenter.v1.notification_config_pb2.NotificationConfig,
        )
        self.UpdateOrganizationSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateOrganizationSettings',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateOrganizationSettingsRequest,
            google.cloud.securitycenter.v1.organization_settings_pb2.OrganizationSettings,
        )
        self.UpdateSource = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateSource',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateSourceRequest,
            google.cloud.securitycenter.v1.source_pb2.Source,
        )
        self.UpdateSecurityMarks = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1.SecurityCenter/UpdateSecurityMarks',
            google.cloud.securitycenter.v1.securitycenter_service_pb2.UpdateSecurityMarksRequest,
            google.cloud.securitycenter.v1.security_marks_pb2.SecurityMarks,
        )
