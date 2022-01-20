# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/privacy/dlp/v2/dlp.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.privacy.dlp.v2.storage_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.type.date_pb2
import google.type.dayofweek_pb2
import google.type.timeofday_pb2
import google.api.annotations_pb2
import google.privacy.dlp.v2.dlp_pb2


class DlpServiceBase(abc.ABC):

    @abc.abstractmethod
    async def InspectContent(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.InspectContentRequest, google.privacy.dlp.v2.dlp_pb2.InspectContentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RedactImage(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.RedactImageRequest, google.privacy.dlp.v2.dlp_pb2.RedactImageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeidentifyContent(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.DeidentifyContentRequest, google.privacy.dlp.v2.dlp_pb2.DeidentifyContentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReidentifyContent(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.ReidentifyContentRequest, google.privacy.dlp.v2.dlp_pb2.ReidentifyContentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListInfoTypes(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.ListInfoTypesRequest, google.privacy.dlp.v2.dlp_pb2.ListInfoTypesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateInspectTemplate(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.CreateInspectTemplateRequest, google.privacy.dlp.v2.dlp_pb2.InspectTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateInspectTemplate(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.UpdateInspectTemplateRequest, google.privacy.dlp.v2.dlp_pb2.InspectTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def GetInspectTemplate(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.GetInspectTemplateRequest, google.privacy.dlp.v2.dlp_pb2.InspectTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def ListInspectTemplates(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.ListInspectTemplatesRequest, google.privacy.dlp.v2.dlp_pb2.ListInspectTemplatesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteInspectTemplate(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.DeleteInspectTemplateRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateDeidentifyTemplate(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.CreateDeidentifyTemplateRequest, google.privacy.dlp.v2.dlp_pb2.DeidentifyTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateDeidentifyTemplate(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.UpdateDeidentifyTemplateRequest, google.privacy.dlp.v2.dlp_pb2.DeidentifyTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def GetDeidentifyTemplate(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.GetDeidentifyTemplateRequest, google.privacy.dlp.v2.dlp_pb2.DeidentifyTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def ListDeidentifyTemplates(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.ListDeidentifyTemplatesRequest, google.privacy.dlp.v2.dlp_pb2.ListDeidentifyTemplatesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteDeidentifyTemplate(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.DeleteDeidentifyTemplateRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateJobTrigger(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.CreateJobTriggerRequest, google.privacy.dlp.v2.dlp_pb2.JobTrigger]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateJobTrigger(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.UpdateJobTriggerRequest, google.privacy.dlp.v2.dlp_pb2.JobTrigger]') -> None:
        pass

    @abc.abstractmethod
    async def HybridInspectJobTrigger(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.HybridInspectJobTriggerRequest, google.privacy.dlp.v2.dlp_pb2.HybridInspectResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetJobTrigger(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.GetJobTriggerRequest, google.privacy.dlp.v2.dlp_pb2.JobTrigger]') -> None:
        pass

    @abc.abstractmethod
    async def ListJobTriggers(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.ListJobTriggersRequest, google.privacy.dlp.v2.dlp_pb2.ListJobTriggersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteJobTrigger(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.DeleteJobTriggerRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ActivateJobTrigger(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.ActivateJobTriggerRequest, google.privacy.dlp.v2.dlp_pb2.DlpJob]') -> None:
        pass

    @abc.abstractmethod
    async def CreateDlpJob(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.CreateDlpJobRequest, google.privacy.dlp.v2.dlp_pb2.DlpJob]') -> None:
        pass

    @abc.abstractmethod
    async def ListDlpJobs(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.ListDlpJobsRequest, google.privacy.dlp.v2.dlp_pb2.ListDlpJobsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDlpJob(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.GetDlpJobRequest, google.privacy.dlp.v2.dlp_pb2.DlpJob]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteDlpJob(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.DeleteDlpJobRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CancelDlpJob(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.CancelDlpJobRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateStoredInfoType(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.CreateStoredInfoTypeRequest, google.privacy.dlp.v2.dlp_pb2.StoredInfoType]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateStoredInfoType(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.UpdateStoredInfoTypeRequest, google.privacy.dlp.v2.dlp_pb2.StoredInfoType]') -> None:
        pass

    @abc.abstractmethod
    async def GetStoredInfoType(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.GetStoredInfoTypeRequest, google.privacy.dlp.v2.dlp_pb2.StoredInfoType]') -> None:
        pass

    @abc.abstractmethod
    async def ListStoredInfoTypes(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.ListStoredInfoTypesRequest, google.privacy.dlp.v2.dlp_pb2.ListStoredInfoTypesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteStoredInfoType(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.DeleteStoredInfoTypeRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def HybridInspectDlpJob(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.HybridInspectDlpJobRequest, google.privacy.dlp.v2.dlp_pb2.HybridInspectResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FinishDlpJob(self, stream: 'grpclib.server.Stream[google.privacy.dlp.v2.dlp_pb2.FinishDlpJobRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.privacy.dlp.v2.DlpService/InspectContent': grpclib.const.Handler(
                self.InspectContent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.InspectContentRequest,
                google.privacy.dlp.v2.dlp_pb2.InspectContentResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/RedactImage': grpclib.const.Handler(
                self.RedactImage,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.RedactImageRequest,
                google.privacy.dlp.v2.dlp_pb2.RedactImageResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/DeidentifyContent': grpclib.const.Handler(
                self.DeidentifyContent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.DeidentifyContentRequest,
                google.privacy.dlp.v2.dlp_pb2.DeidentifyContentResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/ReidentifyContent': grpclib.const.Handler(
                self.ReidentifyContent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.ReidentifyContentRequest,
                google.privacy.dlp.v2.dlp_pb2.ReidentifyContentResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/ListInfoTypes': grpclib.const.Handler(
                self.ListInfoTypes,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.ListInfoTypesRequest,
                google.privacy.dlp.v2.dlp_pb2.ListInfoTypesResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/CreateInspectTemplate': grpclib.const.Handler(
                self.CreateInspectTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.CreateInspectTemplateRequest,
                google.privacy.dlp.v2.dlp_pb2.InspectTemplate,
            ),
            '/google.privacy.dlp.v2.DlpService/UpdateInspectTemplate': grpclib.const.Handler(
                self.UpdateInspectTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.UpdateInspectTemplateRequest,
                google.privacy.dlp.v2.dlp_pb2.InspectTemplate,
            ),
            '/google.privacy.dlp.v2.DlpService/GetInspectTemplate': grpclib.const.Handler(
                self.GetInspectTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.GetInspectTemplateRequest,
                google.privacy.dlp.v2.dlp_pb2.InspectTemplate,
            ),
            '/google.privacy.dlp.v2.DlpService/ListInspectTemplates': grpclib.const.Handler(
                self.ListInspectTemplates,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.ListInspectTemplatesRequest,
                google.privacy.dlp.v2.dlp_pb2.ListInspectTemplatesResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/DeleteInspectTemplate': grpclib.const.Handler(
                self.DeleteInspectTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.DeleteInspectTemplateRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.privacy.dlp.v2.DlpService/CreateDeidentifyTemplate': grpclib.const.Handler(
                self.CreateDeidentifyTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.CreateDeidentifyTemplateRequest,
                google.privacy.dlp.v2.dlp_pb2.DeidentifyTemplate,
            ),
            '/google.privacy.dlp.v2.DlpService/UpdateDeidentifyTemplate': grpclib.const.Handler(
                self.UpdateDeidentifyTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.UpdateDeidentifyTemplateRequest,
                google.privacy.dlp.v2.dlp_pb2.DeidentifyTemplate,
            ),
            '/google.privacy.dlp.v2.DlpService/GetDeidentifyTemplate': grpclib.const.Handler(
                self.GetDeidentifyTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.GetDeidentifyTemplateRequest,
                google.privacy.dlp.v2.dlp_pb2.DeidentifyTemplate,
            ),
            '/google.privacy.dlp.v2.DlpService/ListDeidentifyTemplates': grpclib.const.Handler(
                self.ListDeidentifyTemplates,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.ListDeidentifyTemplatesRequest,
                google.privacy.dlp.v2.dlp_pb2.ListDeidentifyTemplatesResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/DeleteDeidentifyTemplate': grpclib.const.Handler(
                self.DeleteDeidentifyTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.DeleteDeidentifyTemplateRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.privacy.dlp.v2.DlpService/CreateJobTrigger': grpclib.const.Handler(
                self.CreateJobTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.CreateJobTriggerRequest,
                google.privacy.dlp.v2.dlp_pb2.JobTrigger,
            ),
            '/google.privacy.dlp.v2.DlpService/UpdateJobTrigger': grpclib.const.Handler(
                self.UpdateJobTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.UpdateJobTriggerRequest,
                google.privacy.dlp.v2.dlp_pb2.JobTrigger,
            ),
            '/google.privacy.dlp.v2.DlpService/HybridInspectJobTrigger': grpclib.const.Handler(
                self.HybridInspectJobTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.HybridInspectJobTriggerRequest,
                google.privacy.dlp.v2.dlp_pb2.HybridInspectResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/GetJobTrigger': grpclib.const.Handler(
                self.GetJobTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.GetJobTriggerRequest,
                google.privacy.dlp.v2.dlp_pb2.JobTrigger,
            ),
            '/google.privacy.dlp.v2.DlpService/ListJobTriggers': grpclib.const.Handler(
                self.ListJobTriggers,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.ListJobTriggersRequest,
                google.privacy.dlp.v2.dlp_pb2.ListJobTriggersResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/DeleteJobTrigger': grpclib.const.Handler(
                self.DeleteJobTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.DeleteJobTriggerRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.privacy.dlp.v2.DlpService/ActivateJobTrigger': grpclib.const.Handler(
                self.ActivateJobTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.ActivateJobTriggerRequest,
                google.privacy.dlp.v2.dlp_pb2.DlpJob,
            ),
            '/google.privacy.dlp.v2.DlpService/CreateDlpJob': grpclib.const.Handler(
                self.CreateDlpJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.CreateDlpJobRequest,
                google.privacy.dlp.v2.dlp_pb2.DlpJob,
            ),
            '/google.privacy.dlp.v2.DlpService/ListDlpJobs': grpclib.const.Handler(
                self.ListDlpJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.ListDlpJobsRequest,
                google.privacy.dlp.v2.dlp_pb2.ListDlpJobsResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/GetDlpJob': grpclib.const.Handler(
                self.GetDlpJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.GetDlpJobRequest,
                google.privacy.dlp.v2.dlp_pb2.DlpJob,
            ),
            '/google.privacy.dlp.v2.DlpService/DeleteDlpJob': grpclib.const.Handler(
                self.DeleteDlpJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.DeleteDlpJobRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.privacy.dlp.v2.DlpService/CancelDlpJob': grpclib.const.Handler(
                self.CancelDlpJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.CancelDlpJobRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.privacy.dlp.v2.DlpService/CreateStoredInfoType': grpclib.const.Handler(
                self.CreateStoredInfoType,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.CreateStoredInfoTypeRequest,
                google.privacy.dlp.v2.dlp_pb2.StoredInfoType,
            ),
            '/google.privacy.dlp.v2.DlpService/UpdateStoredInfoType': grpclib.const.Handler(
                self.UpdateStoredInfoType,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.UpdateStoredInfoTypeRequest,
                google.privacy.dlp.v2.dlp_pb2.StoredInfoType,
            ),
            '/google.privacy.dlp.v2.DlpService/GetStoredInfoType': grpclib.const.Handler(
                self.GetStoredInfoType,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.GetStoredInfoTypeRequest,
                google.privacy.dlp.v2.dlp_pb2.StoredInfoType,
            ),
            '/google.privacy.dlp.v2.DlpService/ListStoredInfoTypes': grpclib.const.Handler(
                self.ListStoredInfoTypes,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.ListStoredInfoTypesRequest,
                google.privacy.dlp.v2.dlp_pb2.ListStoredInfoTypesResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/DeleteStoredInfoType': grpclib.const.Handler(
                self.DeleteStoredInfoType,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.DeleteStoredInfoTypeRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.privacy.dlp.v2.DlpService/HybridInspectDlpJob': grpclib.const.Handler(
                self.HybridInspectDlpJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.HybridInspectDlpJobRequest,
                google.privacy.dlp.v2.dlp_pb2.HybridInspectResponse,
            ),
            '/google.privacy.dlp.v2.DlpService/FinishDlpJob': grpclib.const.Handler(
                self.FinishDlpJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.privacy.dlp.v2.dlp_pb2.FinishDlpJobRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class DlpServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.InspectContent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/InspectContent',
            google.privacy.dlp.v2.dlp_pb2.InspectContentRequest,
            google.privacy.dlp.v2.dlp_pb2.InspectContentResponse,
        )
        self.RedactImage = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/RedactImage',
            google.privacy.dlp.v2.dlp_pb2.RedactImageRequest,
            google.privacy.dlp.v2.dlp_pb2.RedactImageResponse,
        )
        self.DeidentifyContent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/DeidentifyContent',
            google.privacy.dlp.v2.dlp_pb2.DeidentifyContentRequest,
            google.privacy.dlp.v2.dlp_pb2.DeidentifyContentResponse,
        )
        self.ReidentifyContent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/ReidentifyContent',
            google.privacy.dlp.v2.dlp_pb2.ReidentifyContentRequest,
            google.privacy.dlp.v2.dlp_pb2.ReidentifyContentResponse,
        )
        self.ListInfoTypes = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/ListInfoTypes',
            google.privacy.dlp.v2.dlp_pb2.ListInfoTypesRequest,
            google.privacy.dlp.v2.dlp_pb2.ListInfoTypesResponse,
        )
        self.CreateInspectTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/CreateInspectTemplate',
            google.privacy.dlp.v2.dlp_pb2.CreateInspectTemplateRequest,
            google.privacy.dlp.v2.dlp_pb2.InspectTemplate,
        )
        self.UpdateInspectTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/UpdateInspectTemplate',
            google.privacy.dlp.v2.dlp_pb2.UpdateInspectTemplateRequest,
            google.privacy.dlp.v2.dlp_pb2.InspectTemplate,
        )
        self.GetInspectTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/GetInspectTemplate',
            google.privacy.dlp.v2.dlp_pb2.GetInspectTemplateRequest,
            google.privacy.dlp.v2.dlp_pb2.InspectTemplate,
        )
        self.ListInspectTemplates = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/ListInspectTemplates',
            google.privacy.dlp.v2.dlp_pb2.ListInspectTemplatesRequest,
            google.privacy.dlp.v2.dlp_pb2.ListInspectTemplatesResponse,
        )
        self.DeleteInspectTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/DeleteInspectTemplate',
            google.privacy.dlp.v2.dlp_pb2.DeleteInspectTemplateRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateDeidentifyTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/CreateDeidentifyTemplate',
            google.privacy.dlp.v2.dlp_pb2.CreateDeidentifyTemplateRequest,
            google.privacy.dlp.v2.dlp_pb2.DeidentifyTemplate,
        )
        self.UpdateDeidentifyTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/UpdateDeidentifyTemplate',
            google.privacy.dlp.v2.dlp_pb2.UpdateDeidentifyTemplateRequest,
            google.privacy.dlp.v2.dlp_pb2.DeidentifyTemplate,
        )
        self.GetDeidentifyTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/GetDeidentifyTemplate',
            google.privacy.dlp.v2.dlp_pb2.GetDeidentifyTemplateRequest,
            google.privacy.dlp.v2.dlp_pb2.DeidentifyTemplate,
        )
        self.ListDeidentifyTemplates = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/ListDeidentifyTemplates',
            google.privacy.dlp.v2.dlp_pb2.ListDeidentifyTemplatesRequest,
            google.privacy.dlp.v2.dlp_pb2.ListDeidentifyTemplatesResponse,
        )
        self.DeleteDeidentifyTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/DeleteDeidentifyTemplate',
            google.privacy.dlp.v2.dlp_pb2.DeleteDeidentifyTemplateRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateJobTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/CreateJobTrigger',
            google.privacy.dlp.v2.dlp_pb2.CreateJobTriggerRequest,
            google.privacy.dlp.v2.dlp_pb2.JobTrigger,
        )
        self.UpdateJobTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/UpdateJobTrigger',
            google.privacy.dlp.v2.dlp_pb2.UpdateJobTriggerRequest,
            google.privacy.dlp.v2.dlp_pb2.JobTrigger,
        )
        self.HybridInspectJobTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/HybridInspectJobTrigger',
            google.privacy.dlp.v2.dlp_pb2.HybridInspectJobTriggerRequest,
            google.privacy.dlp.v2.dlp_pb2.HybridInspectResponse,
        )
        self.GetJobTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/GetJobTrigger',
            google.privacy.dlp.v2.dlp_pb2.GetJobTriggerRequest,
            google.privacy.dlp.v2.dlp_pb2.JobTrigger,
        )
        self.ListJobTriggers = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/ListJobTriggers',
            google.privacy.dlp.v2.dlp_pb2.ListJobTriggersRequest,
            google.privacy.dlp.v2.dlp_pb2.ListJobTriggersResponse,
        )
        self.DeleteJobTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/DeleteJobTrigger',
            google.privacy.dlp.v2.dlp_pb2.DeleteJobTriggerRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ActivateJobTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/ActivateJobTrigger',
            google.privacy.dlp.v2.dlp_pb2.ActivateJobTriggerRequest,
            google.privacy.dlp.v2.dlp_pb2.DlpJob,
        )
        self.CreateDlpJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/CreateDlpJob',
            google.privacy.dlp.v2.dlp_pb2.CreateDlpJobRequest,
            google.privacy.dlp.v2.dlp_pb2.DlpJob,
        )
        self.ListDlpJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/ListDlpJobs',
            google.privacy.dlp.v2.dlp_pb2.ListDlpJobsRequest,
            google.privacy.dlp.v2.dlp_pb2.ListDlpJobsResponse,
        )
        self.GetDlpJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/GetDlpJob',
            google.privacy.dlp.v2.dlp_pb2.GetDlpJobRequest,
            google.privacy.dlp.v2.dlp_pb2.DlpJob,
        )
        self.DeleteDlpJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/DeleteDlpJob',
            google.privacy.dlp.v2.dlp_pb2.DeleteDlpJobRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CancelDlpJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/CancelDlpJob',
            google.privacy.dlp.v2.dlp_pb2.CancelDlpJobRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateStoredInfoType = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/CreateStoredInfoType',
            google.privacy.dlp.v2.dlp_pb2.CreateStoredInfoTypeRequest,
            google.privacy.dlp.v2.dlp_pb2.StoredInfoType,
        )
        self.UpdateStoredInfoType = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/UpdateStoredInfoType',
            google.privacy.dlp.v2.dlp_pb2.UpdateStoredInfoTypeRequest,
            google.privacy.dlp.v2.dlp_pb2.StoredInfoType,
        )
        self.GetStoredInfoType = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/GetStoredInfoType',
            google.privacy.dlp.v2.dlp_pb2.GetStoredInfoTypeRequest,
            google.privacy.dlp.v2.dlp_pb2.StoredInfoType,
        )
        self.ListStoredInfoTypes = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/ListStoredInfoTypes',
            google.privacy.dlp.v2.dlp_pb2.ListStoredInfoTypesRequest,
            google.privacy.dlp.v2.dlp_pb2.ListStoredInfoTypesResponse,
        )
        self.DeleteStoredInfoType = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/DeleteStoredInfoType',
            google.privacy.dlp.v2.dlp_pb2.DeleteStoredInfoTypeRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.HybridInspectDlpJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/HybridInspectDlpJob',
            google.privacy.dlp.v2.dlp_pb2.HybridInspectDlpJobRequest,
            google.privacy.dlp.v2.dlp_pb2.HybridInspectResponse,
        )
        self.FinishDlpJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.privacy.dlp.v2.DlpService/FinishDlpJob',
            google.privacy.dlp.v2.dlp_pb2.FinishDlpJobRequest,
            google.protobuf.empty_pb2.Empty,
        )
