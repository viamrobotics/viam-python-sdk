# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/security/privateca/v1beta1/service.proto
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
import google.cloud.security.privateca.v1beta1.resources_pb2
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.security.privateca.v1beta1.service_pb2


class CertificateAuthorityServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateCertificate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.CreateCertificateRequest, google.cloud.security.privateca.v1beta1.resources_pb2.Certificate]') -> None:
        pass

    @abc.abstractmethod
    async def GetCertificate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.GetCertificateRequest, google.cloud.security.privateca.v1beta1.resources_pb2.Certificate]') -> None:
        pass

    @abc.abstractmethod
    async def ListCertificates(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.ListCertificatesRequest, google.cloud.security.privateca.v1beta1.service_pb2.ListCertificatesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RevokeCertificate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.RevokeCertificateRequest, google.cloud.security.privateca.v1beta1.resources_pb2.Certificate]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateCertificate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.UpdateCertificateRequest, google.cloud.security.privateca.v1beta1.resources_pb2.Certificate]') -> None:
        pass

    @abc.abstractmethod
    async def ActivateCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.ActivateCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def CreateCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.CreateCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DisableCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.DisableCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def EnableCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.EnableCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def FetchCertificateAuthorityCsr(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.FetchCertificateAuthorityCsrRequest, google.cloud.security.privateca.v1beta1.service_pb2.FetchCertificateAuthorityCsrResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.GetCertificateAuthorityRequest, google.cloud.security.privateca.v1beta1.resources_pb2.CertificateAuthority]') -> None:
        pass

    @abc.abstractmethod
    async def ListCertificateAuthorities(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateAuthoritiesRequest, google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateAuthoritiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RestoreCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.RestoreCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ScheduleDeleteCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.ScheduleDeleteCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.UpdateCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetCertificateRevocationList(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.GetCertificateRevocationListRequest, google.cloud.security.privateca.v1beta1.resources_pb2.CertificateRevocationList]') -> None:
        pass

    @abc.abstractmethod
    async def ListCertificateRevocationLists(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateRevocationListsRequest, google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateRevocationListsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateCertificateRevocationList(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.UpdateCertificateRevocationListRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetReusableConfig(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.GetReusableConfigRequest, google.cloud.security.privateca.v1beta1.resources_pb2.ReusableConfig]') -> None:
        pass

    @abc.abstractmethod
    async def ListReusableConfigs(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1beta1.service_pb2.ListReusableConfigsRequest, google.cloud.security.privateca.v1beta1.service_pb2.ListReusableConfigsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/CreateCertificate': grpclib.const.Handler(
                self.CreateCertificate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.CreateCertificateRequest,
                google.cloud.security.privateca.v1beta1.resources_pb2.Certificate,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificate': grpclib.const.Handler(
                self.GetCertificate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.GetCertificateRequest,
                google.cloud.security.privateca.v1beta1.resources_pb2.Certificate,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificates': grpclib.const.Handler(
                self.ListCertificates,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.ListCertificatesRequest,
                google.cloud.security.privateca.v1beta1.service_pb2.ListCertificatesResponse,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/RevokeCertificate': grpclib.const.Handler(
                self.RevokeCertificate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.RevokeCertificateRequest,
                google.cloud.security.privateca.v1beta1.resources_pb2.Certificate,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificate': grpclib.const.Handler(
                self.UpdateCertificate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.UpdateCertificateRequest,
                google.cloud.security.privateca.v1beta1.resources_pb2.Certificate,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ActivateCertificateAuthority': grpclib.const.Handler(
                self.ActivateCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.ActivateCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/CreateCertificateAuthority': grpclib.const.Handler(
                self.CreateCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.CreateCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/DisableCertificateAuthority': grpclib.const.Handler(
                self.DisableCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.DisableCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/EnableCertificateAuthority': grpclib.const.Handler(
                self.EnableCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.EnableCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/FetchCertificateAuthorityCsr': grpclib.const.Handler(
                self.FetchCertificateAuthorityCsr,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.FetchCertificateAuthorityCsrRequest,
                google.cloud.security.privateca.v1beta1.service_pb2.FetchCertificateAuthorityCsrResponse,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificateAuthority': grpclib.const.Handler(
                self.GetCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.GetCertificateAuthorityRequest,
                google.cloud.security.privateca.v1beta1.resources_pb2.CertificateAuthority,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificateAuthorities': grpclib.const.Handler(
                self.ListCertificateAuthorities,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateAuthoritiesRequest,
                google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateAuthoritiesResponse,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/RestoreCertificateAuthority': grpclib.const.Handler(
                self.RestoreCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.RestoreCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ScheduleDeleteCertificateAuthority': grpclib.const.Handler(
                self.ScheduleDeleteCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.ScheduleDeleteCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificateAuthority': grpclib.const.Handler(
                self.UpdateCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.UpdateCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificateRevocationList': grpclib.const.Handler(
                self.GetCertificateRevocationList,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.GetCertificateRevocationListRequest,
                google.cloud.security.privateca.v1beta1.resources_pb2.CertificateRevocationList,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificateRevocationLists': grpclib.const.Handler(
                self.ListCertificateRevocationLists,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateRevocationListsRequest,
                google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateRevocationListsResponse,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificateRevocationList': grpclib.const.Handler(
                self.UpdateCertificateRevocationList,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.UpdateCertificateRevocationListRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetReusableConfig': grpclib.const.Handler(
                self.GetReusableConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.GetReusableConfigRequest,
                google.cloud.security.privateca.v1beta1.resources_pb2.ReusableConfig,
            ),
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListReusableConfigs': grpclib.const.Handler(
                self.ListReusableConfigs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1beta1.service_pb2.ListReusableConfigsRequest,
                google.cloud.security.privateca.v1beta1.service_pb2.ListReusableConfigsResponse,
            ),
        }


class CertificateAuthorityServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateCertificate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/CreateCertificate',
            google.cloud.security.privateca.v1beta1.service_pb2.CreateCertificateRequest,
            google.cloud.security.privateca.v1beta1.resources_pb2.Certificate,
        )
        self.GetCertificate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificate',
            google.cloud.security.privateca.v1beta1.service_pb2.GetCertificateRequest,
            google.cloud.security.privateca.v1beta1.resources_pb2.Certificate,
        )
        self.ListCertificates = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificates',
            google.cloud.security.privateca.v1beta1.service_pb2.ListCertificatesRequest,
            google.cloud.security.privateca.v1beta1.service_pb2.ListCertificatesResponse,
        )
        self.RevokeCertificate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/RevokeCertificate',
            google.cloud.security.privateca.v1beta1.service_pb2.RevokeCertificateRequest,
            google.cloud.security.privateca.v1beta1.resources_pb2.Certificate,
        )
        self.UpdateCertificate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificate',
            google.cloud.security.privateca.v1beta1.service_pb2.UpdateCertificateRequest,
            google.cloud.security.privateca.v1beta1.resources_pb2.Certificate,
        )
        self.ActivateCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ActivateCertificateAuthority',
            google.cloud.security.privateca.v1beta1.service_pb2.ActivateCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.CreateCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/CreateCertificateAuthority',
            google.cloud.security.privateca.v1beta1.service_pb2.CreateCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DisableCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/DisableCertificateAuthority',
            google.cloud.security.privateca.v1beta1.service_pb2.DisableCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.EnableCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/EnableCertificateAuthority',
            google.cloud.security.privateca.v1beta1.service_pb2.EnableCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.FetchCertificateAuthorityCsr = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/FetchCertificateAuthorityCsr',
            google.cloud.security.privateca.v1beta1.service_pb2.FetchCertificateAuthorityCsrRequest,
            google.cloud.security.privateca.v1beta1.service_pb2.FetchCertificateAuthorityCsrResponse,
        )
        self.GetCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificateAuthority',
            google.cloud.security.privateca.v1beta1.service_pb2.GetCertificateAuthorityRequest,
            google.cloud.security.privateca.v1beta1.resources_pb2.CertificateAuthority,
        )
        self.ListCertificateAuthorities = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificateAuthorities',
            google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateAuthoritiesRequest,
            google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateAuthoritiesResponse,
        )
        self.RestoreCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/RestoreCertificateAuthority',
            google.cloud.security.privateca.v1beta1.service_pb2.RestoreCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ScheduleDeleteCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ScheduleDeleteCertificateAuthority',
            google.cloud.security.privateca.v1beta1.service_pb2.ScheduleDeleteCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificateAuthority',
            google.cloud.security.privateca.v1beta1.service_pb2.UpdateCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetCertificateRevocationList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetCertificateRevocationList',
            google.cloud.security.privateca.v1beta1.service_pb2.GetCertificateRevocationListRequest,
            google.cloud.security.privateca.v1beta1.resources_pb2.CertificateRevocationList,
        )
        self.ListCertificateRevocationLists = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListCertificateRevocationLists',
            google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateRevocationListsRequest,
            google.cloud.security.privateca.v1beta1.service_pb2.ListCertificateRevocationListsResponse,
        )
        self.UpdateCertificateRevocationList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/UpdateCertificateRevocationList',
            google.cloud.security.privateca.v1beta1.service_pb2.UpdateCertificateRevocationListRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetReusableConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/GetReusableConfig',
            google.cloud.security.privateca.v1beta1.service_pb2.GetReusableConfigRequest,
            google.cloud.security.privateca.v1beta1.resources_pb2.ReusableConfig,
        )
        self.ListReusableConfigs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1beta1.CertificateAuthorityService/ListReusableConfigs',
            google.cloud.security.privateca.v1beta1.service_pb2.ListReusableConfigsRequest,
            google.cloud.security.privateca.v1beta1.service_pb2.ListReusableConfigsResponse,
        )
