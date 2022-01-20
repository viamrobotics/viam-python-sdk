"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Tag(google.protobuf.message.Message):
    """Tags contain custom metadata and are attached to Data Catalog resources. Tags
    conform with the specification of their tag template.

    See [Data Catalog
    IAM](https://cloud.google.com/data-catalog/docs/concepts/iam) for information
    on the permissions needed to create or view tags.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class FieldsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___TagField: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___TagField] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    TEMPLATE_FIELD_NUMBER: builtins.int
    TEMPLATE_DISPLAY_NAME_FIELD_NUMBER: builtins.int
    COLUMN_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The resource name of the tag in URL format where tag ID is a
    system-generated identifier.

    Note: The tag itself might not be stored in the location specified in its
    name.
    """

    template: typing.Text = ...
    """Required. The resource name of the tag template this tag uses. Example:

    `projects/{PROJECT_ID}/locations/{LOCATION}/tagTemplates/{TAG_TEMPLATE_ID}`

    This field cannot be modified after creation.
    """

    template_display_name: typing.Text = ...
    """Output only. The display name of the tag template."""

    column: typing.Text = ...
    """Resources like entry can have schemas associated with them. This scope
    allows you to attach tags to an individual column based on that schema.

    To attach a tag to a nested column, separate column names with a dot
    (`.`). Example: `column.nested_column`.
    """

    @property
    def fields(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___TagField]:
        """Required. Maps the ID of a tag field to its value and additional information
        about that field.

        Tag template defines valid field IDs. A tag
        must have at least 1 field and at most 500 fields.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        template : typing.Text = ...,
        template_display_name : typing.Text = ...,
        column : typing.Text = ...,
        fields : typing.Optional[typing.Mapping[typing.Text, global___TagField]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["column",b"column","scope",b"scope"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["column",b"column","fields",b"fields","name",b"name","scope",b"scope","template",b"template","template_display_name",b"template_display_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["scope",b"scope"]) -> typing.Optional[typing_extensions.Literal["column"]]: ...
global___Tag = Tag

class TagField(google.protobuf.message.Message):
    """Contains the value and additional information on a field within
    a [Tag][google.cloud.datacatalog.v1.Tag].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class EnumValue(google.protobuf.message.Message):
        """An enum value."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        DISPLAY_NAME_FIELD_NUMBER: builtins.int
        display_name: typing.Text = ...
        """The display name of the enum value."""

        def __init__(self,
            *,
            display_name : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["display_name",b"display_name"]) -> None: ...

    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DOUBLE_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    BOOL_VALUE_FIELD_NUMBER: builtins.int
    TIMESTAMP_VALUE_FIELD_NUMBER: builtins.int
    ENUM_VALUE_FIELD_NUMBER: builtins.int
    RICHTEXT_VALUE_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    display_name: typing.Text = ...
    """Output only. The display name of this field."""

    double_value: builtins.float = ...
    """The value of a tag field with a double type."""

    string_value: typing.Text = ...
    """The value of a tag field with a string type.

    The maximum length is 2000 UTF-8 characters.
    """

    bool_value: builtins.bool = ...
    """The value of a tag field with a boolean type."""

    @property
    def timestamp_value(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The value of a tag field with a timestamp type."""
        pass
    @property
    def enum_value(self) -> global___TagField.EnumValue:
        """The value of a tag field with an enum type.

        This value must be one of the allowed values listed in this enum.
        """
        pass
    richtext_value: typing.Text = ...
    """The value of a tag field with a rich text type.

    The maximum length is 10 MiB as this value holds HTML descriptions
    including encoded images. The maximum length of the text without images
    is 100 KiB.
    """

    order: builtins.int = ...
    """Output only. The order of this field with respect to other fields in this tag. Can be
    set by [Tag][google.cloud.datacatalog.v1.TagTemplateField.order].

    For example, a higher value can indicate a more important field.
    The value can be negative. Multiple fields can have the same order, and
    field orders within a tag don't have to be sequential.
    """

    def __init__(self,
        *,
        display_name : typing.Text = ...,
        double_value : builtins.float = ...,
        string_value : typing.Text = ...,
        bool_value : builtins.bool = ...,
        timestamp_value : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        enum_value : typing.Optional[global___TagField.EnumValue] = ...,
        richtext_value : typing.Text = ...,
        order : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bool_value",b"bool_value","double_value",b"double_value","enum_value",b"enum_value","kind",b"kind","richtext_value",b"richtext_value","string_value",b"string_value","timestamp_value",b"timestamp_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bool_value",b"bool_value","display_name",b"display_name","double_value",b"double_value","enum_value",b"enum_value","kind",b"kind","order",b"order","richtext_value",b"richtext_value","string_value",b"string_value","timestamp_value",b"timestamp_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["kind",b"kind"]) -> typing.Optional[typing_extensions.Literal["double_value","string_value","bool_value","timestamp_value","enum_value","richtext_value"]]: ...
global___TagField = TagField

class TagTemplate(google.protobuf.message.Message):
    """A tag template defines a tag that can have one or more typed fields.

    The template is used to create tags that are attached to GCP resources.
    [Tag template roles]
    (https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles)
    provide permissions to create, edit, and use the template. For example,
    see the [TagTemplate User]
    (https://cloud.google.com/data-catalog/docs/how-to/template-user) role
    that includes a permission to use the tag template to tag resources.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class FieldsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___TagTemplateField: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___TagTemplateField] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    IS_PUBLICLY_READABLE_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The resource name of the tag template in URL format.

    Note: The tag template itself and its child resources might not be
    stored in the location specified in its name.
    """

    display_name: typing.Text = ...
    """Display name for this template. Defaults to an empty string.

    The name must contain only Unicode letters, numbers (0-9), underscores (_),
    dashes (-), spaces ( ), and can't start or end with spaces.
    The maximum length is 200 characters.
    """

    is_publicly_readable: builtins.bool = ...
    """Indicates whether this is a public tag template.

    Every user has view access to a *public* tag template by default.
    This means that:

      * Every user can use this tag template to tag an entry.
      * If an entry is tagged using the tag template, the tag is always
        shown in the response to ``ListTags`` called on the entry.
      * To get the template using the GetTagTemplate method, you
        need view access either on the project or the organization the tag
        template resides in but no other permission is needed.
      * Operations on the tag template other than viewing (for example,
        editing IAM policies) follow standard IAM structures.

    Tags created with a public tag template are referred to as public tags.

    You can search for a public tag by value with a
    simple search query instead of using a ``tag:`` predicate.

    Public tag templates may not appear in search results depending on scope,
    see:
    [include_public_tag_templates][google.cloud.datacatalog.v1.SearchCatalogRequest.Scope.include_public_tag_templates]

    Note: If an [IAM domain
    restriction](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-domains)
    is configured in the tag template's location, the public access will not be
    enabled but the simple search for tag values will still work.
    """

    @property
    def fields(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___TagTemplateField]:
        """Required. Map of tag template field IDs to the settings for the field.
        This map is an exhaustive list of the allowed fields. The map must contain
        at least one field and at most 500 fields.

        The keys to this map are tag template field IDs. The IDs have the
        following limitations:

        * Can contain uppercase and lowercase letters, numbers (0-9) and
          underscores (_).
        * Must be at least 1 character and at most 64 characters long.
        * Must start with a letter or underscore.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        is_publicly_readable : builtins.bool = ...,
        fields : typing.Optional[typing.Mapping[typing.Text, global___TagTemplateField]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["display_name",b"display_name","fields",b"fields","is_publicly_readable",b"is_publicly_readable","name",b"name"]) -> None: ...
global___TagTemplate = TagTemplate

class TagTemplateField(google.protobuf.message.Message):
    """The template for an individual field within a tag template."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    IS_REQUIRED_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The resource name of the tag template field in URL format. Example:

    `projects/{PROJECT_ID}/locations/{LOCATION}/tagTemplates/{TAG_TEMPLATE}/fields/{FIELD}`

    Note: The tag template field itself might not be stored in the location
    specified in its name.

    The name must contain only letters (a-z, A-Z), numbers (0-9),
    or underscores (_), and must start with a letter or underscore.
    The maximum length is 64 characters.
    """

    display_name: typing.Text = ...
    """The display name for this field. Defaults to an empty string.

    The name must contain only Unicode letters, numbers (0-9), underscores (_),
    dashes (-), spaces ( ), and can't start or end with spaces.
    The maximum length is 200 characters.
    """

    @property
    def type(self) -> global___FieldType:
        """Required. The type of value this tag field can contain."""
        pass
    is_required: builtins.bool = ...
    """If true, this field is required. Defaults to false."""

    description: typing.Text = ...
    """The description for this field. Defaults to an empty string."""

    order: builtins.int = ...
    """The order of this field with respect to other fields in this tag
    template.

    For example, a higher value can indicate a more important field.
    The value can be negative. Multiple fields can have the same order and
    field orders within a tag don't have to be sequential.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        type : typing.Optional[global___FieldType] = ...,
        is_required : builtins.bool = ...,
        description : typing.Text = ...,
        order : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["type",b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","display_name",b"display_name","is_required",b"is_required","name",b"name","order",b"order","type",b"type"]) -> None: ...
global___TagTemplateField = TagTemplateField

class FieldType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _PrimitiveType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _PrimitiveTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PrimitiveType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        PRIMITIVE_TYPE_UNSPECIFIED: FieldType.PrimitiveType.ValueType = ...  # 0
        """The default invalid value for a type."""

        DOUBLE: FieldType.PrimitiveType.ValueType = ...  # 1
        """A double precision number."""

        STRING: FieldType.PrimitiveType.ValueType = ...  # 2
        """An UTF-8 string."""

        BOOL: FieldType.PrimitiveType.ValueType = ...  # 3
        """A boolean value."""

        TIMESTAMP: FieldType.PrimitiveType.ValueType = ...  # 4
        """A timestamp."""

        RICHTEXT: FieldType.PrimitiveType.ValueType = ...  # 5
        """A Richtext description."""

    class PrimitiveType(_PrimitiveType, metaclass=_PrimitiveTypeEnumTypeWrapper):
        pass

    PRIMITIVE_TYPE_UNSPECIFIED: FieldType.PrimitiveType.ValueType = ...  # 0
    """The default invalid value for a type."""

    DOUBLE: FieldType.PrimitiveType.ValueType = ...  # 1
    """A double precision number."""

    STRING: FieldType.PrimitiveType.ValueType = ...  # 2
    """An UTF-8 string."""

    BOOL: FieldType.PrimitiveType.ValueType = ...  # 3
    """A boolean value."""

    TIMESTAMP: FieldType.PrimitiveType.ValueType = ...  # 4
    """A timestamp."""

    RICHTEXT: FieldType.PrimitiveType.ValueType = ...  # 5
    """A Richtext description."""


    class EnumType(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class EnumValue(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            DISPLAY_NAME_FIELD_NUMBER: builtins.int
            display_name: typing.Text = ...
            """Required. The display name of the enum value. Must not be an empty string.

            The name must contain only Unicode letters, numbers (0-9), underscores
            (_), dashes (-), spaces ( ), and can't start or end with spaces. The
            maximum length is 200 characters.
            """

            def __init__(self,
                *,
                display_name : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["display_name",b"display_name"]) -> None: ...

        ALLOWED_VALUES_FIELD_NUMBER: builtins.int
        @property
        def allowed_values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FieldType.EnumType.EnumValue]:
            """The set of allowed values for this enum.

            This set must not be empty and can include up to 100 allowed values.
            The display names of the values in this set must not be empty and must
            be case-insensitively unique within this set.

            The order of items in this set is preserved. This field can be used to
            create, remove, and reorder enum values. To rename enum values, use the
            `RenameTagTemplateFieldEnumValue` method.
            """
            pass
        def __init__(self,
            *,
            allowed_values : typing.Optional[typing.Iterable[global___FieldType.EnumType.EnumValue]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["allowed_values",b"allowed_values"]) -> None: ...

    PRIMITIVE_TYPE_FIELD_NUMBER: builtins.int
    ENUM_TYPE_FIELD_NUMBER: builtins.int
    primitive_type: global___FieldType.PrimitiveType.ValueType = ...
    """Primitive types, such as string, boolean, etc."""

    @property
    def enum_type(self) -> global___FieldType.EnumType:
        """An enum type."""
        pass
    def __init__(self,
        *,
        primitive_type : global___FieldType.PrimitiveType.ValueType = ...,
        enum_type : typing.Optional[global___FieldType.EnumType] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["enum_type",b"enum_type","primitive_type",b"primitive_type","type_decl",b"type_decl"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["enum_type",b"enum_type","primitive_type",b"primitive_type","type_decl",b"type_decl"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type_decl",b"type_decl"]) -> typing.Optional[typing_extensions.Literal["primitive_type","enum_type"]]: ...
global___FieldType = FieldType
