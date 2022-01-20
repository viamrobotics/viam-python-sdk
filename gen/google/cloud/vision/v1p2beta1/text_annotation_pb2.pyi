"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.vision.v1p2beta1.geometry_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TextAnnotation(google.protobuf.message.Message):
    """TextAnnotation contains a structured representation of OCR extracted text.
    The hierarchy of an OCR extracted text structure is like this:
        TextAnnotation -> Page -> Block -> Paragraph -> Word -> Symbol
    Each structural component, starting from Page, may further have their own
    properties. Properties describe detected languages, breaks etc.. Please refer
    to the
    [TextAnnotation.TextProperty][google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty]
    message definition below for more detail.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class DetectedLanguage(google.protobuf.message.Message):
        """Detected language for a structural component."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        LANGUAGE_CODE_FIELD_NUMBER: builtins.int
        CONFIDENCE_FIELD_NUMBER: builtins.int
        language_code: typing.Text = ...
        """The BCP-47 language code, such as "en-US" or "sr-Latn". For more
        information, see
        http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
        """

        confidence: builtins.float = ...
        """Confidence of detected language. Range [0, 1]."""

        def __init__(self,
            *,
            language_code : typing.Text = ...,
            confidence : builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["confidence",b"confidence","language_code",b"language_code"]) -> None: ...

    class DetectedBreak(google.protobuf.message.Message):
        """Detected start or end of a structural component."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class _BreakType:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType
        class _BreakTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BreakType.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
            UNKNOWN: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 0
            """Unknown break label type."""

            SPACE: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 1
            """Regular space."""

            SURE_SPACE: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 2
            """Sure space (very wide)."""

            EOL_SURE_SPACE: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 3
            """Line-wrapping break."""

            HYPHEN: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 4
            """End-line hyphen that is not present in text; does not co-occur with
            `SPACE`, `LEADER_SPACE`, or `LINE_BREAK`.
            """

            LINE_BREAK: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 5
            """Line break that ends a paragraph."""

        class BreakType(_BreakType, metaclass=_BreakTypeEnumTypeWrapper):
            """Enum to denote the type of break found. New line, space etc."""
            pass

        UNKNOWN: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 0
        """Unknown break label type."""

        SPACE: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 1
        """Regular space."""

        SURE_SPACE: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 2
        """Sure space (very wide)."""

        EOL_SURE_SPACE: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 3
        """Line-wrapping break."""

        HYPHEN: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 4
        """End-line hyphen that is not present in text; does not co-occur with
        `SPACE`, `LEADER_SPACE`, or `LINE_BREAK`.
        """

        LINE_BREAK: TextAnnotation.DetectedBreak.BreakType.ValueType = ...  # 5
        """Line break that ends a paragraph."""


        TYPE_FIELD_NUMBER: builtins.int
        IS_PREFIX_FIELD_NUMBER: builtins.int
        type: global___TextAnnotation.DetectedBreak.BreakType.ValueType = ...
        """Detected break type."""

        is_prefix: builtins.bool = ...
        """True if break prepends the element."""

        def __init__(self,
            *,
            type : global___TextAnnotation.DetectedBreak.BreakType.ValueType = ...,
            is_prefix : builtins.bool = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["is_prefix",b"is_prefix","type",b"type"]) -> None: ...

    class TextProperty(google.protobuf.message.Message):
        """Additional information detected on the structural component."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        DETECTED_LANGUAGES_FIELD_NUMBER: builtins.int
        DETECTED_BREAK_FIELD_NUMBER: builtins.int
        @property
        def detected_languages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TextAnnotation.DetectedLanguage]:
            """A list of detected languages together with confidence."""
            pass
        @property
        def detected_break(self) -> global___TextAnnotation.DetectedBreak:
            """Detected start or end of a text segment."""
            pass
        def __init__(self,
            *,
            detected_languages : typing.Optional[typing.Iterable[global___TextAnnotation.DetectedLanguage]] = ...,
            detected_break : typing.Optional[global___TextAnnotation.DetectedBreak] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["detected_break",b"detected_break"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["detected_break",b"detected_break","detected_languages",b"detected_languages"]) -> None: ...

    PAGES_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    @property
    def pages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Page]:
        """List of pages detected by OCR."""
        pass
    text: typing.Text = ...
    """UTF-8 text detected on the pages."""

    def __init__(self,
        *,
        pages : typing.Optional[typing.Iterable[global___Page]] = ...,
        text : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pages",b"pages","text",b"text"]) -> None: ...
global___TextAnnotation = TextAnnotation

class Page(google.protobuf.message.Message):
    """Detected page from OCR."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROPERTY_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    BLOCKS_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    @property
    def property(self) -> global___TextAnnotation.TextProperty:
        """Additional information detected on the page."""
        pass
    width: builtins.int = ...
    """Page width. For PDFs the unit is points. For images (including
    TIFFs) the unit is pixels.
    """

    height: builtins.int = ...
    """Page height. For PDFs the unit is points. For images (including
    TIFFs) the unit is pixels.
    """

    @property
    def blocks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Block]:
        """List of blocks of text, images etc on this page."""
        pass
    confidence: builtins.float = ...
    """Confidence of the OCR results on the page. Range [0, 1]."""

    def __init__(self,
        *,
        property : typing.Optional[global___TextAnnotation.TextProperty] = ...,
        width : builtins.int = ...,
        height : builtins.int = ...,
        blocks : typing.Optional[typing.Iterable[global___Block]] = ...,
        confidence : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["property",b"property"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["blocks",b"blocks","confidence",b"confidence","height",b"height","property",b"property","width",b"width"]) -> None: ...
global___Page = Page

class Block(google.protobuf.message.Message):
    """Logical element on the page."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _BlockType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _BlockTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BlockType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNKNOWN: Block.BlockType.ValueType = ...  # 0
        """Unknown block type."""

        TEXT: Block.BlockType.ValueType = ...  # 1
        """Regular text block."""

        TABLE: Block.BlockType.ValueType = ...  # 2
        """Table block."""

        PICTURE: Block.BlockType.ValueType = ...  # 3
        """Image block."""

        RULER: Block.BlockType.ValueType = ...  # 4
        """Horizontal/vertical line box."""

        BARCODE: Block.BlockType.ValueType = ...  # 5
        """Barcode block."""

    class BlockType(_BlockType, metaclass=_BlockTypeEnumTypeWrapper):
        """Type of a block (text, image etc) as identified by OCR."""
        pass

    UNKNOWN: Block.BlockType.ValueType = ...  # 0
    """Unknown block type."""

    TEXT: Block.BlockType.ValueType = ...  # 1
    """Regular text block."""

    TABLE: Block.BlockType.ValueType = ...  # 2
    """Table block."""

    PICTURE: Block.BlockType.ValueType = ...  # 3
    """Image block."""

    RULER: Block.BlockType.ValueType = ...  # 4
    """Horizontal/vertical line box."""

    BARCODE: Block.BlockType.ValueType = ...  # 5
    """Barcode block."""


    PROPERTY_FIELD_NUMBER: builtins.int
    BOUNDING_BOX_FIELD_NUMBER: builtins.int
    PARAGRAPHS_FIELD_NUMBER: builtins.int
    BLOCK_TYPE_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    @property
    def property(self) -> global___TextAnnotation.TextProperty:
        """Additional information detected for the block."""
        pass
    @property
    def bounding_box(self) -> google.cloud.vision.v1p2beta1.geometry_pb2.BoundingPoly:
        """The bounding box for the block.
        The vertices are in the order of top-left, top-right, bottom-right,
        bottom-left. When a rotation of the bounding box is detected the rotation
        is represented as around the top-left corner as defined when the text is
        read in the 'natural' orientation.
        For example:

        * when the text is horizontal it might look like:

                0----1
                |    |
                3----2

        * when it's rotated 180 degrees around the top-left corner it becomes:

                2----3
                |    |
                1----0

          and the vertice order will still be (0, 1, 2, 3).
        """
        pass
    @property
    def paragraphs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Paragraph]:
        """List of paragraphs in this block (if this blocks is of type text)."""
        pass
    block_type: global___Block.BlockType.ValueType = ...
    """Detected block type (text, image etc) for this block."""

    confidence: builtins.float = ...
    """Confidence of the OCR results on the block. Range [0, 1]."""

    def __init__(self,
        *,
        property : typing.Optional[global___TextAnnotation.TextProperty] = ...,
        bounding_box : typing.Optional[google.cloud.vision.v1p2beta1.geometry_pb2.BoundingPoly] = ...,
        paragraphs : typing.Optional[typing.Iterable[global___Paragraph]] = ...,
        block_type : global___Block.BlockType.ValueType = ...,
        confidence : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bounding_box",b"bounding_box","property",b"property"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_type",b"block_type","bounding_box",b"bounding_box","confidence",b"confidence","paragraphs",b"paragraphs","property",b"property"]) -> None: ...
global___Block = Block

class Paragraph(google.protobuf.message.Message):
    """Structural unit of text representing a number of words in certain order."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROPERTY_FIELD_NUMBER: builtins.int
    BOUNDING_BOX_FIELD_NUMBER: builtins.int
    WORDS_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    @property
    def property(self) -> global___TextAnnotation.TextProperty:
        """Additional information detected for the paragraph."""
        pass
    @property
    def bounding_box(self) -> google.cloud.vision.v1p2beta1.geometry_pb2.BoundingPoly:
        """The bounding box for the paragraph.
        The vertices are in the order of top-left, top-right, bottom-right,
        bottom-left. When a rotation of the bounding box is detected the rotation
        is represented as around the top-left corner as defined when the text is
        read in the 'natural' orientation.
        For example:
          * when the text is horizontal it might look like:
             0----1
             |    |
             3----2
          * when it's rotated 180 degrees around the top-left corner it becomes:
             2----3
             |    |
             1----0
          and the vertice order will still be (0, 1, 2, 3).
        """
        pass
    @property
    def words(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Word]:
        """List of words in this paragraph."""
        pass
    confidence: builtins.float = ...
    """Confidence of the OCR results for the paragraph. Range [0, 1]."""

    def __init__(self,
        *,
        property : typing.Optional[global___TextAnnotation.TextProperty] = ...,
        bounding_box : typing.Optional[google.cloud.vision.v1p2beta1.geometry_pb2.BoundingPoly] = ...,
        words : typing.Optional[typing.Iterable[global___Word]] = ...,
        confidence : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bounding_box",b"bounding_box","property",b"property"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bounding_box",b"bounding_box","confidence",b"confidence","property",b"property","words",b"words"]) -> None: ...
global___Paragraph = Paragraph

class Word(google.protobuf.message.Message):
    """A word representation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROPERTY_FIELD_NUMBER: builtins.int
    BOUNDING_BOX_FIELD_NUMBER: builtins.int
    SYMBOLS_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    @property
    def property(self) -> global___TextAnnotation.TextProperty:
        """Additional information detected for the word."""
        pass
    @property
    def bounding_box(self) -> google.cloud.vision.v1p2beta1.geometry_pb2.BoundingPoly:
        """The bounding box for the word.
        The vertices are in the order of top-left, top-right, bottom-right,
        bottom-left. When a rotation of the bounding box is detected the rotation
        is represented as around the top-left corner as defined when the text is
        read in the 'natural' orientation.
        For example:
          * when the text is horizontal it might look like:
             0----1
             |    |
             3----2
          * when it's rotated 180 degrees around the top-left corner it becomes:
             2----3
             |    |
             1----0
          and the vertice order will still be (0, 1, 2, 3).
        """
        pass
    @property
    def symbols(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Symbol]:
        """List of symbols in the word.
        The order of the symbols follows the natural reading order.
        """
        pass
    confidence: builtins.float = ...
    """Confidence of the OCR results for the word. Range [0, 1]."""

    def __init__(self,
        *,
        property : typing.Optional[global___TextAnnotation.TextProperty] = ...,
        bounding_box : typing.Optional[google.cloud.vision.v1p2beta1.geometry_pb2.BoundingPoly] = ...,
        symbols : typing.Optional[typing.Iterable[global___Symbol]] = ...,
        confidence : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bounding_box",b"bounding_box","property",b"property"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bounding_box",b"bounding_box","confidence",b"confidence","property",b"property","symbols",b"symbols"]) -> None: ...
global___Word = Word

class Symbol(google.protobuf.message.Message):
    """A single symbol representation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROPERTY_FIELD_NUMBER: builtins.int
    BOUNDING_BOX_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    CONFIDENCE_FIELD_NUMBER: builtins.int
    @property
    def property(self) -> global___TextAnnotation.TextProperty:
        """Additional information detected for the symbol."""
        pass
    @property
    def bounding_box(self) -> google.cloud.vision.v1p2beta1.geometry_pb2.BoundingPoly:
        """The bounding box for the symbol.
        The vertices are in the order of top-left, top-right, bottom-right,
        bottom-left. When a rotation of the bounding box is detected the rotation
        is represented as around the top-left corner as defined when the text is
        read in the 'natural' orientation.
        For example:
          * when the text is horizontal it might look like:
             0----1
             |    |
             3----2
          * when it's rotated 180 degrees around the top-left corner it becomes:
             2----3
             |    |
             1----0
          and the vertice order will still be (0, 1, 2, 3).
        """
        pass
    text: typing.Text = ...
    """The actual UTF-8 representation of the symbol."""

    confidence: builtins.float = ...
    """Confidence of the OCR results for the symbol. Range [0, 1]."""

    def __init__(self,
        *,
        property : typing.Optional[global___TextAnnotation.TextProperty] = ...,
        bounding_box : typing.Optional[google.cloud.vision.v1p2beta1.geometry_pb2.BoundingPoly] = ...,
        text : typing.Text = ...,
        confidence : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bounding_box",b"bounding_box","property",b"property"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bounding_box",b"bounding_box","confidence",b"confidence","property",b"property","text",b"text"]) -> None: ...
global___Symbol = Symbol
