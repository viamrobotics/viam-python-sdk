# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/speech/v1p1beta1/cloud_speech_adaptation.proto
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
import google.cloud.speech.v1p1beta1.resource_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2


class AdaptationBase(abc.ABC):

    @abc.abstractmethod
    async def CreatePhraseSet(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.CreatePhraseSetRequest, google.cloud.speech.v1p1beta1.resource_pb2.PhraseSet]') -> None:
        pass

    @abc.abstractmethod
    async def GetPhraseSet(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.GetPhraseSetRequest, google.cloud.speech.v1p1beta1.resource_pb2.PhraseSet]') -> None:
        pass

    @abc.abstractmethod
    async def ListPhraseSet(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListPhraseSetRequest, google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListPhraseSetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdatePhraseSet(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.UpdatePhraseSetRequest, google.cloud.speech.v1p1beta1.resource_pb2.PhraseSet]') -> None:
        pass

    @abc.abstractmethod
    async def DeletePhraseSet(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.DeletePhraseSetRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateCustomClass(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.CreateCustomClassRequest, google.cloud.speech.v1p1beta1.resource_pb2.CustomClass]') -> None:
        pass

    @abc.abstractmethod
    async def GetCustomClass(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.GetCustomClassRequest, google.cloud.speech.v1p1beta1.resource_pb2.CustomClass]') -> None:
        pass

    @abc.abstractmethod
    async def ListCustomClasses(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListCustomClassesRequest, google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListCustomClassesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateCustomClass(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.UpdateCustomClassRequest, google.cloud.speech.v1p1beta1.resource_pb2.CustomClass]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteCustomClass(self, stream: 'grpclib.server.Stream[google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.DeleteCustomClassRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.speech.v1p1beta1.Adaptation/CreatePhraseSet': grpclib.const.Handler(
                self.CreatePhraseSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.CreatePhraseSetRequest,
                google.cloud.speech.v1p1beta1.resource_pb2.PhraseSet,
            ),
            '/google.cloud.speech.v1p1beta1.Adaptation/GetPhraseSet': grpclib.const.Handler(
                self.GetPhraseSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.GetPhraseSetRequest,
                google.cloud.speech.v1p1beta1.resource_pb2.PhraseSet,
            ),
            '/google.cloud.speech.v1p1beta1.Adaptation/ListPhraseSet': grpclib.const.Handler(
                self.ListPhraseSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListPhraseSetRequest,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListPhraseSetResponse,
            ),
            '/google.cloud.speech.v1p1beta1.Adaptation/UpdatePhraseSet': grpclib.const.Handler(
                self.UpdatePhraseSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.UpdatePhraseSetRequest,
                google.cloud.speech.v1p1beta1.resource_pb2.PhraseSet,
            ),
            '/google.cloud.speech.v1p1beta1.Adaptation/DeletePhraseSet': grpclib.const.Handler(
                self.DeletePhraseSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.DeletePhraseSetRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.speech.v1p1beta1.Adaptation/CreateCustomClass': grpclib.const.Handler(
                self.CreateCustomClass,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.CreateCustomClassRequest,
                google.cloud.speech.v1p1beta1.resource_pb2.CustomClass,
            ),
            '/google.cloud.speech.v1p1beta1.Adaptation/GetCustomClass': grpclib.const.Handler(
                self.GetCustomClass,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.GetCustomClassRequest,
                google.cloud.speech.v1p1beta1.resource_pb2.CustomClass,
            ),
            '/google.cloud.speech.v1p1beta1.Adaptation/ListCustomClasses': grpclib.const.Handler(
                self.ListCustomClasses,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListCustomClassesRequest,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListCustomClassesResponse,
            ),
            '/google.cloud.speech.v1p1beta1.Adaptation/UpdateCustomClass': grpclib.const.Handler(
                self.UpdateCustomClass,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.UpdateCustomClassRequest,
                google.cloud.speech.v1p1beta1.resource_pb2.CustomClass,
            ),
            '/google.cloud.speech.v1p1beta1.Adaptation/DeleteCustomClass': grpclib.const.Handler(
                self.DeleteCustomClass,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.DeleteCustomClassRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class AdaptationStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreatePhraseSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/CreatePhraseSet',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.CreatePhraseSetRequest,
            google.cloud.speech.v1p1beta1.resource_pb2.PhraseSet,
        )
        self.GetPhraseSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/GetPhraseSet',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.GetPhraseSetRequest,
            google.cloud.speech.v1p1beta1.resource_pb2.PhraseSet,
        )
        self.ListPhraseSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/ListPhraseSet',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListPhraseSetRequest,
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListPhraseSetResponse,
        )
        self.UpdatePhraseSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/UpdatePhraseSet',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.UpdatePhraseSetRequest,
            google.cloud.speech.v1p1beta1.resource_pb2.PhraseSet,
        )
        self.DeletePhraseSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/DeletePhraseSet',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.DeletePhraseSetRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateCustomClass = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/CreateCustomClass',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.CreateCustomClassRequest,
            google.cloud.speech.v1p1beta1.resource_pb2.CustomClass,
        )
        self.GetCustomClass = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/GetCustomClass',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.GetCustomClassRequest,
            google.cloud.speech.v1p1beta1.resource_pb2.CustomClass,
        )
        self.ListCustomClasses = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/ListCustomClasses',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListCustomClassesRequest,
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.ListCustomClassesResponse,
        )
        self.UpdateCustomClass = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/UpdateCustomClass',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.UpdateCustomClassRequest,
            google.cloud.speech.v1p1beta1.resource_pb2.CustomClass,
        )
        self.DeleteCustomClass = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.speech.v1p1beta1.Adaptation/DeleteCustomClass',
            google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2.DeleteCustomClassRequest,
            google.protobuf.empty_pb2.Empty,
        )
