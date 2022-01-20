# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/datacatalog/v1/policytagmanagerserialization.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.cloud.datacatalog.v1.policytagmanager_pb2
import google.iam.v1.policy_pb2
import google.api.client_pb2
import google.cloud.datacatalog.v1.policytagmanagerserialization_pb2


class PolicyTagManagerSerializationBase(abc.ABC):

    @abc.abstractmethod
    async def ReplaceTaxonomy(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ReplaceTaxonomyRequest, google.cloud.datacatalog.v1.policytagmanager_pb2.Taxonomy]') -> None:
        pass

    @abc.abstractmethod
    async def ImportTaxonomies(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ImportTaxonomiesRequest, google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ImportTaxonomiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ExportTaxonomies(self, stream: 'grpclib.server.Stream[google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ExportTaxonomiesRequest, google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ExportTaxonomiesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.datacatalog.v1.PolicyTagManagerSerialization/ReplaceTaxonomy': grpclib.const.Handler(
                self.ReplaceTaxonomy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ReplaceTaxonomyRequest,
                google.cloud.datacatalog.v1.policytagmanager_pb2.Taxonomy,
            ),
            '/google.cloud.datacatalog.v1.PolicyTagManagerSerialization/ImportTaxonomies': grpclib.const.Handler(
                self.ImportTaxonomies,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ImportTaxonomiesRequest,
                google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ImportTaxonomiesResponse,
            ),
            '/google.cloud.datacatalog.v1.PolicyTagManagerSerialization/ExportTaxonomies': grpclib.const.Handler(
                self.ExportTaxonomies,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ExportTaxonomiesRequest,
                google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ExportTaxonomiesResponse,
            ),
        }


class PolicyTagManagerSerializationStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ReplaceTaxonomy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1.PolicyTagManagerSerialization/ReplaceTaxonomy',
            google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ReplaceTaxonomyRequest,
            google.cloud.datacatalog.v1.policytagmanager_pb2.Taxonomy,
        )
        self.ImportTaxonomies = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1.PolicyTagManagerSerialization/ImportTaxonomies',
            google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ImportTaxonomiesRequest,
            google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ImportTaxonomiesResponse,
        )
        self.ExportTaxonomies = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.datacatalog.v1.PolicyTagManagerSerialization/ExportTaxonomies',
            google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ExportTaxonomiesRequest,
            google.cloud.datacatalog.v1.policytagmanagerserialization_pb2.ExportTaxonomiesResponse,
        )
