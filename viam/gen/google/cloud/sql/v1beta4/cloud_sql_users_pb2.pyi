"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SqlUsersDeleteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HOST_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    host: typing.Text = ...
    """Host of the user in the instance."""

    instance: typing.Text = ...
    """Database instance ID. This does not include the project ID."""

    name: typing.Text = ...
    """Name of the user in the instance."""

    project: typing.Text = ...
    """Project ID of the project that contains the instance."""

    def __init__(self,
        *,
        host : typing.Text = ...,
        instance : typing.Text = ...,
        name : typing.Text = ...,
        project : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host",b"host","instance",b"instance","name",b"name","project",b"project"]) -> None: ...
global___SqlUsersDeleteRequest = SqlUsersDeleteRequest

class SqlUsersUpdateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HOST_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    host: typing.Text = ...
    """Optional. Host of the user in the instance."""

    instance: typing.Text = ...
    """Database instance ID. This does not include the project ID."""

    name: typing.Text = ...
    """Name of the user in the instance."""

    project: typing.Text = ...
    """Project ID of the project that contains the instance."""

    @property
    def body(self) -> global___User: ...
    def __init__(self,
        *,
        host : typing.Text = ...,
        instance : typing.Text = ...,
        name : typing.Text = ...,
        project : typing.Text = ...,
        body : typing.Optional[global___User] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["body",b"body"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body",b"body","host",b"host","instance",b"instance","name",b"name","project",b"project"]) -> None: ...
global___SqlUsersUpdateRequest = SqlUsersUpdateRequest

class SqlUsersInsertRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INSTANCE_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    instance: typing.Text = ...
    """Database instance ID. This does not include the project ID."""

    project: typing.Text = ...
    """Project ID of the project that contains the instance."""

    @property
    def body(self) -> global___User: ...
    def __init__(self,
        *,
        instance : typing.Text = ...,
        project : typing.Text = ...,
        body : typing.Optional[global___User] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["body",b"body"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body",b"body","instance",b"instance","project",b"project"]) -> None: ...
global___SqlUsersInsertRequest = SqlUsersInsertRequest

class SqlUsersListRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INSTANCE_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    instance: typing.Text = ...
    """Database instance ID. This does not include the project ID."""

    project: typing.Text = ...
    """Project ID of the project that contains the instance."""

    def __init__(self,
        *,
        instance : typing.Text = ...,
        project : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["instance",b"instance","project",b"project"]) -> None: ...
global___SqlUsersListRequest = SqlUsersListRequest

class UserPasswordValidationPolicy(google.protobuf.message.Message):
    """User level password validation policy."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ALLOWED_FAILED_ATTEMPTS_FIELD_NUMBER: builtins.int
    PASSWORD_EXPIRATION_DURATION_FIELD_NUMBER: builtins.int
    ENABLE_FAILED_ATTEMPTS_CHECK_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    allowed_failed_attempts: builtins.int = ...
    """Number of failed login attempts allowed before user get locked."""

    @property
    def password_expiration_duration(self) -> google.protobuf.duration_pb2.Duration:
        """Expiration duration after password is updated."""
        pass
    enable_failed_attempts_check: builtins.bool = ...
    """If true, failed login attempts check will be enabled."""

    @property
    def status(self) -> global___PasswordStatus:
        """Output only. Read-only password status."""
        pass
    def __init__(self,
        *,
        allowed_failed_attempts : builtins.int = ...,
        password_expiration_duration : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        enable_failed_attempts_check : builtins.bool = ...,
        status : typing.Optional[global___PasswordStatus] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["password_expiration_duration",b"password_expiration_duration","status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allowed_failed_attempts",b"allowed_failed_attempts","enable_failed_attempts_check",b"enable_failed_attempts_check","password_expiration_duration",b"password_expiration_duration","status",b"status"]) -> None: ...
global___UserPasswordValidationPolicy = UserPasswordValidationPolicy

class PasswordStatus(google.protobuf.message.Message):
    """Read-only password status."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOCKED_FIELD_NUMBER: builtins.int
    PASSWORD_EXPIRATION_TIME_FIELD_NUMBER: builtins.int
    locked: builtins.bool = ...
    """If true, user does not have login privileges."""

    @property
    def password_expiration_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The expiration time of the current password."""
        pass
    def __init__(self,
        *,
        locked : builtins.bool = ...,
        password_expiration_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["password_expiration_time",b"password_expiration_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["locked",b"locked","password_expiration_time",b"password_expiration_time"]) -> None: ...
global___PasswordStatus = PasswordStatus

class User(google.protobuf.message.Message):
    """A Cloud SQL user resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _SqlUserType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _SqlUserTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SqlUserType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        BUILT_IN: User.SqlUserType.ValueType = ...  # 0
        """The database's built-in user type."""

        CLOUD_IAM_USER: User.SqlUserType.ValueType = ...  # 1
        """Cloud IAM user."""

        CLOUD_IAM_SERVICE_ACCOUNT: User.SqlUserType.ValueType = ...  # 2
        """Cloud IAM service account."""

    class SqlUserType(_SqlUserType, metaclass=_SqlUserTypeEnumTypeWrapper):
        """The user type."""
        pass

    BUILT_IN: User.SqlUserType.ValueType = ...  # 0
    """The database's built-in user type."""

    CLOUD_IAM_USER: User.SqlUserType.ValueType = ...  # 1
    """Cloud IAM user."""

    CLOUD_IAM_SERVICE_ACCOUNT: User.SqlUserType.ValueType = ...  # 2
    """Cloud IAM service account."""


    KIND_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    INSTANCE_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    SQLSERVER_USER_DETAILS_FIELD_NUMBER: builtins.int
    PASSWORD_POLICY_FIELD_NUMBER: builtins.int
    kind: typing.Text = ...
    """This is always `sql#user`."""

    password: typing.Text = ...
    """The password for the user."""

    etag: typing.Text = ...
    """This field is deprecated and will be removed from a future version of the
    API.
    """

    name: typing.Text = ...
    """The name of the user in the Cloud SQL instance. Can be omitted for
    `update` because it is already specified in the URL.
    """

    host: typing.Text = ...
    """Optional. The host from which the user can connect. For `insert`
    operations, host defaults to an empty string. For `update`
    operations, host is specified as part of the request URL. The host name
    cannot be updated after insertion.  For a MySQL instance, it's required;
    for a PostgreSQL or SQL Server instance, it's optional.
    """

    instance: typing.Text = ...
    """The name of the Cloud SQL instance. This does not include the project ID.
    Can be omitted for <b>update</b> because it is already specified on the
    URL.
    """

    project: typing.Text = ...
    """The project ID of the project containing the Cloud SQL database. The Google
    apps domain is prefixed if applicable. Can be omitted for
    <b>update</b> because it is already specified on the URL.
    """

    type: global___User.SqlUserType.ValueType = ...
    """The user type. It determines the method to authenticate the user during
    login. The default is the database's built-in user type.
    """

    @property
    def sqlserver_user_details(self) -> global___SqlServerUserDetails: ...
    @property
    def password_policy(self) -> global___UserPasswordValidationPolicy:
        """User level password validation policy."""
        pass
    def __init__(self,
        *,
        kind : typing.Text = ...,
        password : typing.Text = ...,
        etag : typing.Text = ...,
        name : typing.Text = ...,
        host : typing.Text = ...,
        instance : typing.Text = ...,
        project : typing.Text = ...,
        type : global___User.SqlUserType.ValueType = ...,
        sqlserver_user_details : typing.Optional[global___SqlServerUserDetails] = ...,
        password_policy : typing.Optional[global___UserPasswordValidationPolicy] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["password_policy",b"password_policy","sqlserver_user_details",b"sqlserver_user_details","user_details",b"user_details"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["etag",b"etag","host",b"host","instance",b"instance","kind",b"kind","name",b"name","password",b"password","password_policy",b"password_policy","project",b"project","sqlserver_user_details",b"sqlserver_user_details","type",b"type","user_details",b"user_details"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["user_details",b"user_details"]) -> typing.Optional[typing_extensions.Literal["sqlserver_user_details"]]: ...
global___User = User

class SqlServerUserDetails(google.protobuf.message.Message):
    """Represents a Sql Server user on the Cloud SQL instance."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DISABLED_FIELD_NUMBER: builtins.int
    SERVER_ROLES_FIELD_NUMBER: builtins.int
    disabled: builtins.bool = ...
    """If the user has been disabled"""

    @property
    def server_roles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The server roles for this user"""
        pass
    def __init__(self,
        *,
        disabled : builtins.bool = ...,
        server_roles : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["disabled",b"disabled","server_roles",b"server_roles"]) -> None: ...
global___SqlServerUserDetails = SqlServerUserDetails

class UsersListResponse(google.protobuf.message.Message):
    """User list response."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KIND_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    kind: typing.Text = ...
    """This is always <b>sql#usersList</b>."""

    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___User]:
        """List of user resources in the instance."""
        pass
    next_page_token: typing.Text = ...
    """An identifier that uniquely identifies the operation. You can use this
    identifier to retrieve the Operations resource that has information about
    the operation.
    """

    def __init__(self,
        *,
        kind : typing.Text = ...,
        items : typing.Optional[typing.Iterable[global___User]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["items",b"items","kind",b"kind","next_page_token",b"next_page_token"]) -> None: ...
global___UsersListResponse = UsersListResponse
