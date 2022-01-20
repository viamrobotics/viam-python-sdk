"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.firestore.v1.document_pb2
import google.firestore.v1.query_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class BundledQuery(google.protobuf.message.Message):
    """Encodes a query saved in the bundle."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _LimitType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _LimitTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LimitType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        FIRST: BundledQuery.LimitType.ValueType = ...  # 0
        LAST: BundledQuery.LimitType.ValueType = ...  # 1
    class LimitType(_LimitType, metaclass=_LimitTypeEnumTypeWrapper):
        """If the query is a limit query, should the limit be applied to the beginning or
        the end of results.
        """
        pass

    FIRST: BundledQuery.LimitType.ValueType = ...  # 0
    LAST: BundledQuery.LimitType.ValueType = ...  # 1

    PARENT_FIELD_NUMBER: builtins.int
    STRUCTURED_QUERY_FIELD_NUMBER: builtins.int
    LIMIT_TYPE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The parent resource name."""

    @property
    def structured_query(self) -> google.firestore.v1.query_pb2.StructuredQuery:
        """A structured query."""
        pass
    limit_type: global___BundledQuery.LimitType.ValueType = ...
    def __init__(self,
        *,
        parent : typing.Text = ...,
        structured_query : typing.Optional[google.firestore.v1.query_pb2.StructuredQuery] = ...,
        limit_type : global___BundledQuery.LimitType.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["query_type",b"query_type","structured_query",b"structured_query"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["limit_type",b"limit_type","parent",b"parent","query_type",b"query_type","structured_query",b"structured_query"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["query_type",b"query_type"]) -> typing.Optional[typing_extensions.Literal["structured_query"]]: ...
global___BundledQuery = BundledQuery

class NamedQuery(google.protobuf.message.Message):
    """A Query associated with a name, created as part of the bundle file, and can be read
    by client SDKs once the bundle containing them is loaded.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    BUNDLED_QUERY_FIELD_NUMBER: builtins.int
    READ_TIME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the query, such that client can use the name to load this query
    from bundle, and resume from when the query results are materialized
    into this bundle.
    """

    @property
    def bundled_query(self) -> global___BundledQuery:
        """The query saved in the bundle."""
        pass
    @property
    def read_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The read time of the query, when it is used to build the bundle. This is useful to
        resume the query from the bundle, once it is loaded by client SDKs.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        bundled_query : typing.Optional[global___BundledQuery] = ...,
        read_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bundled_query",b"bundled_query","read_time",b"read_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bundled_query",b"bundled_query","name",b"name","read_time",b"read_time"]) -> None: ...
global___NamedQuery = NamedQuery

class BundledDocumentMetadata(google.protobuf.message.Message):
    """Metadata describing a Firestore document saved in the bundle."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    READ_TIME_FIELD_NUMBER: builtins.int
    EXISTS_FIELD_NUMBER: builtins.int
    QUERIES_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The document key of a bundled document."""

    @property
    def read_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The snapshot version of the document data bundled."""
        pass
    exists: builtins.bool = ...
    """Whether the document exists."""

    @property
    def queries(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The names of the queries in this bundle that this document matches to."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        read_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        exists : builtins.bool = ...,
        queries : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_time",b"read_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exists",b"exists","name",b"name","queries",b"queries","read_time",b"read_time"]) -> None: ...
global___BundledDocumentMetadata = BundledDocumentMetadata

class BundleMetadata(google.protobuf.message.Message):
    """Metadata describing the bundle file/stream."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    TOTAL_DOCUMENTS_FIELD_NUMBER: builtins.int
    TOTAL_BYTES_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    """The ID of the bundle."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time at which the documents snapshot is taken for this bundle."""
        pass
    version: builtins.int = ...
    """The schema version of the bundle."""

    total_documents: builtins.int = ...
    """The number of documents in the bundle."""

    total_bytes: builtins.int = ...
    """The size of the bundle in bytes, excluding this `BundleMetadata`."""

    def __init__(self,
        *,
        id : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        version : builtins.int = ...,
        total_documents : builtins.int = ...,
        total_bytes : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","id",b"id","total_bytes",b"total_bytes","total_documents",b"total_documents","version",b"version"]) -> None: ...
global___BundleMetadata = BundleMetadata

class BundleElement(google.protobuf.message.Message):
    """A Firestore bundle is a length-prefixed stream of JSON representations of
    `BundleElement`.
    Only one `BundleMetadata` is expected, and it should be the first element.
    The named queries follow after `metadata`. Every `document_metadata` is
    immediately followed by a `document`.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    METADATA_FIELD_NUMBER: builtins.int
    NAMED_QUERY_FIELD_NUMBER: builtins.int
    DOCUMENT_METADATA_FIELD_NUMBER: builtins.int
    DOCUMENT_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> global___BundleMetadata: ...
    @property
    def named_query(self) -> global___NamedQuery: ...
    @property
    def document_metadata(self) -> global___BundledDocumentMetadata: ...
    @property
    def document(self) -> google.firestore.v1.document_pb2.Document: ...
    def __init__(self,
        *,
        metadata : typing.Optional[global___BundleMetadata] = ...,
        named_query : typing.Optional[global___NamedQuery] = ...,
        document_metadata : typing.Optional[global___BundledDocumentMetadata] = ...,
        document : typing.Optional[google.firestore.v1.document_pb2.Document] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["document",b"document","document_metadata",b"document_metadata","element_type",b"element_type","metadata",b"metadata","named_query",b"named_query"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["document",b"document","document_metadata",b"document_metadata","element_type",b"element_type","metadata",b"metadata","named_query",b"named_query"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["element_type",b"element_type"]) -> typing.Optional[typing_extensions.Literal["metadata","named_query","document_metadata","document"]]: ...
global___BundleElement = BundleElement
