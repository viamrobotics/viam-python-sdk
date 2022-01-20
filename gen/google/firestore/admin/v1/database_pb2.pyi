"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Database(google.protobuf.message.Message):
    """A Cloud Firestore Database.
    Currently only one database is allowed per cloud project; this database
    must have a `database_id` of '(default)'.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _DatabaseType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _DatabaseTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DatabaseType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        DATABASE_TYPE_UNSPECIFIED: Database.DatabaseType.ValueType = ...  # 0
        """The default value. This value is used if the database type is omitted."""

        FIRESTORE_NATIVE: Database.DatabaseType.ValueType = ...  # 1
        """Firestore Native Mode"""

        DATASTORE_MODE: Database.DatabaseType.ValueType = ...  # 2
        """Firestore in Datastore Mode."""

    class DatabaseType(_DatabaseType, metaclass=_DatabaseTypeEnumTypeWrapper):
        """The type of the database.
        See https://cloud.google.com/datastore/docs/firestore-or-datastore for
        information about how to choose.
        """
        pass

    DATABASE_TYPE_UNSPECIFIED: Database.DatabaseType.ValueType = ...  # 0
    """The default value. This value is used if the database type is omitted."""

    FIRESTORE_NATIVE: Database.DatabaseType.ValueType = ...  # 1
    """Firestore Native Mode"""

    DATASTORE_MODE: Database.DatabaseType.ValueType = ...  # 2
    """Firestore in Datastore Mode."""


    class _ConcurrencyMode:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ConcurrencyModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ConcurrencyMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        CONCURRENCY_MODE_UNSPECIFIED: Database.ConcurrencyMode.ValueType = ...  # 0
        """Not used."""

        OPTIMISTIC: Database.ConcurrencyMode.ValueType = ...  # 1
        """Use optimistic concurrency control by default. This setting is available
        for Cloud Firestore customers.
        """

        PESSIMISTIC: Database.ConcurrencyMode.ValueType = ...  # 2
        """Use pessimistic concurrency control by default. This setting is available
        for Cloud Firestore customers.
        This is the default setting for Cloud Firestore.
        """

        OPTIMISTIC_WITH_ENTITY_GROUPS: Database.ConcurrencyMode.ValueType = ...  # 3
        """Use optimistic concurrency control with entity groups by default. This is
        the only available setting for Cloud Datastore customers.
        This is the default setting for Cloud Datastore.
        """

    class ConcurrencyMode(_ConcurrencyMode, metaclass=_ConcurrencyModeEnumTypeWrapper):
        """The type of concurrency control mode for transactions."""
        pass

    CONCURRENCY_MODE_UNSPECIFIED: Database.ConcurrencyMode.ValueType = ...  # 0
    """Not used."""

    OPTIMISTIC: Database.ConcurrencyMode.ValueType = ...  # 1
    """Use optimistic concurrency control by default. This setting is available
    for Cloud Firestore customers.
    """

    PESSIMISTIC: Database.ConcurrencyMode.ValueType = ...  # 2
    """Use pessimistic concurrency control by default. This setting is available
    for Cloud Firestore customers.
    This is the default setting for Cloud Firestore.
    """

    OPTIMISTIC_WITH_ENTITY_GROUPS: Database.ConcurrencyMode.ValueType = ...  # 3
    """Use optimistic concurrency control with entity groups by default. This is
    the only available setting for Cloud Datastore customers.
    This is the default setting for Cloud Datastore.
    """


    NAME_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    CONCURRENCY_MODE_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The resource name of the Database.
    Format: `projects/{project}/databases/{database}`
    """

    location_id: typing.Text = ...
    """The location of the database. Available databases are listed at
    https://cloud.google.com/firestore/docs/locations.
    """

    type: global___Database.DatabaseType.ValueType = ...
    """The type of the database.
    See https://cloud.google.com/datastore/docs/firestore-or-datastore for
    information about how to choose.
    """

    concurrency_mode: global___Database.ConcurrencyMode.ValueType = ...
    """The concurrency control mode to use for this database."""

    etag: typing.Text = ...
    """This checksum is computed by the server based on the value of other
    fields, and may be sent on update and delete requests to ensure the
    client has an up-to-date value before proceeding.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        location_id : typing.Text = ...,
        type : global___Database.DatabaseType.ValueType = ...,
        concurrency_mode : global___Database.ConcurrencyMode.ValueType = ...,
        etag : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["concurrency_mode",b"concurrency_mode","etag",b"etag","location_id",b"location_id","name",b"name","type",b"type"]) -> None: ...
global___Database = Database
