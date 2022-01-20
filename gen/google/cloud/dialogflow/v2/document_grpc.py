# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/v2/document.proto
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
import google.cloud.dialogflow.v2.gcs_pb2
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.cloud.dialogflow.v2.document_pb2


class DocumentsBase(abc.ABC):

    @abc.abstractmethod
    async def ListDocuments(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.document_pb2.ListDocumentsRequest, google.cloud.dialogflow.v2.document_pb2.ListDocumentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDocument(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.document_pb2.GetDocumentRequest, google.cloud.dialogflow.v2.document_pb2.Document]') -> None:
        pass

    @abc.abstractmethod
    async def CreateDocument(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.document_pb2.CreateDocumentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteDocument(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.document_pb2.DeleteDocumentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateDocument(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.document_pb2.UpdateDocumentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ReloadDocument(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.document_pb2.ReloadDocumentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ExportDocument(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.document_pb2.ExportDocumentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.v2.Documents/ListDocuments': grpclib.const.Handler(
                self.ListDocuments,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.document_pb2.ListDocumentsRequest,
                google.cloud.dialogflow.v2.document_pb2.ListDocumentsResponse,
            ),
            '/google.cloud.dialogflow.v2.Documents/GetDocument': grpclib.const.Handler(
                self.GetDocument,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.document_pb2.GetDocumentRequest,
                google.cloud.dialogflow.v2.document_pb2.Document,
            ),
            '/google.cloud.dialogflow.v2.Documents/CreateDocument': grpclib.const.Handler(
                self.CreateDocument,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.document_pb2.CreateDocumentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.v2.Documents/DeleteDocument': grpclib.const.Handler(
                self.DeleteDocument,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.document_pb2.DeleteDocumentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.v2.Documents/UpdateDocument': grpclib.const.Handler(
                self.UpdateDocument,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.document_pb2.UpdateDocumentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.v2.Documents/ReloadDocument': grpclib.const.Handler(
                self.ReloadDocument,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.document_pb2.ReloadDocumentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.v2.Documents/ExportDocument': grpclib.const.Handler(
                self.ExportDocument,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.document_pb2.ExportDocumentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class DocumentsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListDocuments = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Documents/ListDocuments',
            google.cloud.dialogflow.v2.document_pb2.ListDocumentsRequest,
            google.cloud.dialogflow.v2.document_pb2.ListDocumentsResponse,
        )
        self.GetDocument = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Documents/GetDocument',
            google.cloud.dialogflow.v2.document_pb2.GetDocumentRequest,
            google.cloud.dialogflow.v2.document_pb2.Document,
        )
        self.CreateDocument = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Documents/CreateDocument',
            google.cloud.dialogflow.v2.document_pb2.CreateDocumentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteDocument = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Documents/DeleteDocument',
            google.cloud.dialogflow.v2.document_pb2.DeleteDocumentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateDocument = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Documents/UpdateDocument',
            google.cloud.dialogflow.v2.document_pb2.UpdateDocumentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ReloadDocument = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Documents/ReloadDocument',
            google.cloud.dialogflow.v2.document_pb2.ReloadDocumentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ExportDocument = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Documents/ExportDocument',
            google.cloud.dialogflow.v2.document_pb2.ExportDocumentRequest,
            google.longrunning.operations_pb2.Operation,
        )
