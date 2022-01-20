"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.automl.v1.geometry_pb2
import google.cloud.automl.v1.io_pb2
import google.cloud.automl.v1.text_segment_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Image(google.protobuf.message.Message):
    """A representation of an image.
    Only images up to 30MB in size are supported.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IMAGE_BYTES_FIELD_NUMBER: builtins.int
    THUMBNAIL_URI_FIELD_NUMBER: builtins.int
    image_bytes: builtins.bytes = ...
    """Image content represented as a stream of bytes.
    Note: As with all `bytes` fields, protobuffers use a pure binary
    representation, whereas JSON representations use base64.
    """

    thumbnail_uri: typing.Text = ...
    """Output only. HTTP URI to the thumbnail image."""

    def __init__(self,
        *,
        image_bytes : builtins.bytes = ...,
        thumbnail_uri : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data",b"data","image_bytes",b"image_bytes"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data",b"data","image_bytes",b"image_bytes","thumbnail_uri",b"thumbnail_uri"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["data",b"data"]) -> typing.Optional[typing_extensions.Literal["image_bytes"]]: ...
global___Image = Image

class TextSnippet(google.protobuf.message.Message):
    """A representation of a text snippet."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONTENT_FIELD_NUMBER: builtins.int
    MIME_TYPE_FIELD_NUMBER: builtins.int
    CONTENT_URI_FIELD_NUMBER: builtins.int
    content: typing.Text = ...
    """Required. The content of the text snippet as a string. Up to 250000
    characters long.
    """

    mime_type: typing.Text = ...
    """Optional. The format of [content][google.cloud.automl.v1.TextSnippet.content]. Currently the only two allowed
    values are "text/html" and "text/plain". If left blank, the format is
    automatically determined from the type of the uploaded [content][google.cloud.automl.v1.TextSnippet.content].
    """

    content_uri: typing.Text = ...
    """Output only. HTTP URI where you can download the content."""

    def __init__(self,
        *,
        content : typing.Text = ...,
        mime_type : typing.Text = ...,
        content_uri : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content","content_uri",b"content_uri","mime_type",b"mime_type"]) -> None: ...
global___TextSnippet = TextSnippet

class DocumentDimensions(google.protobuf.message.Message):
    """Message that describes dimension of a document."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _DocumentDimensionUnit:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _DocumentDimensionUnitEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DocumentDimensionUnit.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        DOCUMENT_DIMENSION_UNIT_UNSPECIFIED: DocumentDimensions.DocumentDimensionUnit.ValueType = ...  # 0
        """Should not be used."""

        INCH: DocumentDimensions.DocumentDimensionUnit.ValueType = ...  # 1
        """Document dimension is measured in inches."""

        CENTIMETER: DocumentDimensions.DocumentDimensionUnit.ValueType = ...  # 2
        """Document dimension is measured in centimeters."""

        POINT: DocumentDimensions.DocumentDimensionUnit.ValueType = ...  # 3
        """Document dimension is measured in points. 72 points = 1 inch."""

    class DocumentDimensionUnit(_DocumentDimensionUnit, metaclass=_DocumentDimensionUnitEnumTypeWrapper):
        """Unit of the document dimension."""
        pass

    DOCUMENT_DIMENSION_UNIT_UNSPECIFIED: DocumentDimensions.DocumentDimensionUnit.ValueType = ...  # 0
    """Should not be used."""

    INCH: DocumentDimensions.DocumentDimensionUnit.ValueType = ...  # 1
    """Document dimension is measured in inches."""

    CENTIMETER: DocumentDimensions.DocumentDimensionUnit.ValueType = ...  # 2
    """Document dimension is measured in centimeters."""

    POINT: DocumentDimensions.DocumentDimensionUnit.ValueType = ...  # 3
    """Document dimension is measured in points. 72 points = 1 inch."""


    UNIT_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    unit: global___DocumentDimensions.DocumentDimensionUnit.ValueType = ...
    """Unit of the dimension."""

    width: builtins.float = ...
    """Width value of the document, works together with the unit."""

    height: builtins.float = ...
    """Height value of the document, works together with the unit."""

    def __init__(self,
        *,
        unit : global___DocumentDimensions.DocumentDimensionUnit.ValueType = ...,
        width : builtins.float = ...,
        height : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height",b"height","unit",b"unit","width",b"width"]) -> None: ...
global___DocumentDimensions = DocumentDimensions

class Document(google.protobuf.message.Message):
    """A structured text document e.g. a PDF."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Layout(google.protobuf.message.Message):
        """Describes the layout information of a [text_segment][google.cloud.automl.v1.Document.Layout.text_segment] in the document."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class _TextSegmentType:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _TextSegmentTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TextSegmentType.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
            TEXT_SEGMENT_TYPE_UNSPECIFIED: Document.Layout.TextSegmentType.ValueType = ...  # 0
            """Should not be used."""

            TOKEN: Document.Layout.TextSegmentType.ValueType = ...  # 1
            """The text segment is a token. e.g. word."""

            PARAGRAPH: Document.Layout.TextSegmentType.ValueType = ...  # 2
            """The text segment is a paragraph."""

            FORM_FIELD: Document.Layout.TextSegmentType.ValueType = ...  # 3
            """The text segment is a form field."""

            FORM_FIELD_NAME: Document.Layout.TextSegmentType.ValueType = ...  # 4
            """The text segment is the name part of a form field. It will be treated
            as child of another FORM_FIELD TextSegment if its span is subspan of
            another TextSegment with type FORM_FIELD.
            """

            FORM_FIELD_CONTENTS: Document.Layout.TextSegmentType.ValueType = ...  # 5
            """The text segment is the text content part of a form field. It will be
            treated as child of another FORM_FIELD TextSegment if its span is
            subspan of another TextSegment with type FORM_FIELD.
            """

            TABLE: Document.Layout.TextSegmentType.ValueType = ...  # 6
            """The text segment is a whole table, including headers, and all rows."""

            TABLE_HEADER: Document.Layout.TextSegmentType.ValueType = ...  # 7
            """The text segment is a table's headers. It will be treated as child of
            another TABLE TextSegment if its span is subspan of another TextSegment
            with type TABLE.
            """

            TABLE_ROW: Document.Layout.TextSegmentType.ValueType = ...  # 8
            """The text segment is a row in table. It will be treated as child of
            another TABLE TextSegment if its span is subspan of another TextSegment
            with type TABLE.
            """

            TABLE_CELL: Document.Layout.TextSegmentType.ValueType = ...  # 9
            """The text segment is a cell in table. It will be treated as child of
            another TABLE_ROW TextSegment if its span is subspan of another
            TextSegment with type TABLE_ROW.
            """

        class TextSegmentType(_TextSegmentType, metaclass=_TextSegmentTypeEnumTypeWrapper):
            """The type of TextSegment in the context of the original document."""
            pass

        TEXT_SEGMENT_TYPE_UNSPECIFIED: Document.Layout.TextSegmentType.ValueType = ...  # 0
        """Should not be used."""

        TOKEN: Document.Layout.TextSegmentType.ValueType = ...  # 1
        """The text segment is a token. e.g. word."""

        PARAGRAPH: Document.Layout.TextSegmentType.ValueType = ...  # 2
        """The text segment is a paragraph."""

        FORM_FIELD: Document.Layout.TextSegmentType.ValueType = ...  # 3
        """The text segment is a form field."""

        FORM_FIELD_NAME: Document.Layout.TextSegmentType.ValueType = ...  # 4
        """The text segment is the name part of a form field. It will be treated
        as child of another FORM_FIELD TextSegment if its span is subspan of
        another TextSegment with type FORM_FIELD.
        """

        FORM_FIELD_CONTENTS: Document.Layout.TextSegmentType.ValueType = ...  # 5
        """The text segment is the text content part of a form field. It will be
        treated as child of another FORM_FIELD TextSegment if its span is
        subspan of another TextSegment with type FORM_FIELD.
        """

        TABLE: Document.Layout.TextSegmentType.ValueType = ...  # 6
        """The text segment is a whole table, including headers, and all rows."""

        TABLE_HEADER: Document.Layout.TextSegmentType.ValueType = ...  # 7
        """The text segment is a table's headers. It will be treated as child of
        another TABLE TextSegment if its span is subspan of another TextSegment
        with type TABLE.
        """

        TABLE_ROW: Document.Layout.TextSegmentType.ValueType = ...  # 8
        """The text segment is a row in table. It will be treated as child of
        another TABLE TextSegment if its span is subspan of another TextSegment
        with type TABLE.
        """

        TABLE_CELL: Document.Layout.TextSegmentType.ValueType = ...  # 9
        """The text segment is a cell in table. It will be treated as child of
        another TABLE_ROW TextSegment if its span is subspan of another
        TextSegment with type TABLE_ROW.
        """


        TEXT_SEGMENT_FIELD_NUMBER: builtins.int
        PAGE_NUMBER_FIELD_NUMBER: builtins.int
        BOUNDING_POLY_FIELD_NUMBER: builtins.int
        TEXT_SEGMENT_TYPE_FIELD_NUMBER: builtins.int
        @property
        def text_segment(self) -> google.cloud.automl.v1.text_segment_pb2.TextSegment:
            """Text Segment that represents a segment in
            [document_text][google.cloud.automl.v1p1beta.Document.document_text].
            """
            pass
        page_number: builtins.int = ...
        """Page number of the [text_segment][google.cloud.automl.v1.Document.Layout.text_segment] in the original document, starts
        from 1.
        """

        @property
        def bounding_poly(self) -> google.cloud.automl.v1.geometry_pb2.BoundingPoly:
            """The position of the [text_segment][google.cloud.automl.v1.Document.Layout.text_segment] in the page.
            Contains exactly 4
            [normalized_vertices][google.cloud.automl.v1p1beta.BoundingPoly.normalized_vertices]
            and they are connected by edges in the order provided, which will
            represent a rectangle parallel to the frame. The
            [NormalizedVertex-s][google.cloud.automl.v1p1beta.NormalizedVertex] are
            relative to the page.
            Coordinates are based on top-left as point (0,0).
            """
            pass
        text_segment_type: global___Document.Layout.TextSegmentType.ValueType = ...
        """The type of the [text_segment][google.cloud.automl.v1.Document.Layout.text_segment] in document."""

        def __init__(self,
            *,
            text_segment : typing.Optional[google.cloud.automl.v1.text_segment_pb2.TextSegment] = ...,
            page_number : builtins.int = ...,
            bounding_poly : typing.Optional[google.cloud.automl.v1.geometry_pb2.BoundingPoly] = ...,
            text_segment_type : global___Document.Layout.TextSegmentType.ValueType = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["bounding_poly",b"bounding_poly","text_segment",b"text_segment"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["bounding_poly",b"bounding_poly","page_number",b"page_number","text_segment",b"text_segment","text_segment_type",b"text_segment_type"]) -> None: ...

    INPUT_CONFIG_FIELD_NUMBER: builtins.int
    DOCUMENT_TEXT_FIELD_NUMBER: builtins.int
    LAYOUT_FIELD_NUMBER: builtins.int
    DOCUMENT_DIMENSIONS_FIELD_NUMBER: builtins.int
    PAGE_COUNT_FIELD_NUMBER: builtins.int
    @property
    def input_config(self) -> google.cloud.automl.v1.io_pb2.DocumentInputConfig:
        """An input config specifying the content of the document."""
        pass
    @property
    def document_text(self) -> global___TextSnippet:
        """The plain text version of this document."""
        pass
    @property
    def layout(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Document.Layout]:
        """Describes the layout of the document.
        Sorted by [page_number][].
        """
        pass
    @property
    def document_dimensions(self) -> global___DocumentDimensions:
        """The dimensions of the page in the document."""
        pass
    page_count: builtins.int = ...
    """Number of pages in the document."""

    def __init__(self,
        *,
        input_config : typing.Optional[google.cloud.automl.v1.io_pb2.DocumentInputConfig] = ...,
        document_text : typing.Optional[global___TextSnippet] = ...,
        layout : typing.Optional[typing.Iterable[global___Document.Layout]] = ...,
        document_dimensions : typing.Optional[global___DocumentDimensions] = ...,
        page_count : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["document_dimensions",b"document_dimensions","document_text",b"document_text","input_config",b"input_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["document_dimensions",b"document_dimensions","document_text",b"document_text","input_config",b"input_config","layout",b"layout","page_count",b"page_count"]) -> None: ...
global___Document = Document

class ExamplePayload(google.protobuf.message.Message):
    """Example data used for training or prediction."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IMAGE_FIELD_NUMBER: builtins.int
    TEXT_SNIPPET_FIELD_NUMBER: builtins.int
    DOCUMENT_FIELD_NUMBER: builtins.int
    @property
    def image(self) -> global___Image:
        """Example image."""
        pass
    @property
    def text_snippet(self) -> global___TextSnippet:
        """Example text."""
        pass
    @property
    def document(self) -> global___Document:
        """Example document."""
        pass
    def __init__(self,
        *,
        image : typing.Optional[global___Image] = ...,
        text_snippet : typing.Optional[global___TextSnippet] = ...,
        document : typing.Optional[global___Document] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["document",b"document","image",b"image","payload",b"payload","text_snippet",b"text_snippet"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["document",b"document","image",b"image","payload",b"payload","text_snippet",b"text_snippet"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["payload",b"payload"]) -> typing.Optional[typing_extensions.Literal["image","text_snippet","document"]]: ...
global___ExamplePayload = ExamplePayload
