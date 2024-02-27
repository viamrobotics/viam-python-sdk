"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import sys

import google.protobuf.descriptor
import google.protobuf.message

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Credentials(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    type: builtins.str
    "type is the type of credentials being used."
    payload: builtins.str
    "payload is an opaque string used that are of the given type above."

    def __init__(
        self, *, type: builtins.str = ..., payload: builtins.str = ...
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["payload", b"payload", "type", b"type"],
    ) -> None: ...

global___Credentials = Credentials

@typing_extensions.final
class AuthenticateRequest(google.protobuf.message.Message):
    """An AuthenticateRequest contains the credentials used to authenticate."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITY_FIELD_NUMBER: builtins.int
    CREDENTIALS_FIELD_NUMBER: builtins.int
    entity: builtins.str

    @property
    def credentials(self) -> global___Credentials: ...
    def __init__(
        self,
        *,
        entity: builtins.str = ...,
        credentials: global___Credentials | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["credentials", b"credentials"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "credentials", b"credentials", "entity", b"entity"
        ],
    ) -> None: ...

global___AuthenticateRequest = AuthenticateRequest

@typing_extensions.final
class AuthenticateResponse(google.protobuf.message.Message):
    """An AuthenticateResponse is returned after successful authentication."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCESS_TOKEN_FIELD_NUMBER: builtins.int
    access_token: builtins.str
    "access_token is a JWT where only the expiration should be deemed\n    important.\n    Future(erd): maybe a refresh_token\n    "

    def __init__(self, *, access_token: builtins.str = ...) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["access_token", b"access_token"]
    ) -> None: ...

global___AuthenticateResponse = AuthenticateResponse

@typing_extensions.final
class AuthenticateToRequest(google.protobuf.message.Message):
    """An AuthenticateToRequest contains the entity to authenticate to."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITY_FIELD_NUMBER: builtins.int
    entity: builtins.str

    def __init__(self, *, entity: builtins.str = ...) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["entity", b"entity"]
    ) -> None: ...

global___AuthenticateToRequest = AuthenticateToRequest

@typing_extensions.final
class AuthenticateToResponse(google.protobuf.message.Message):
    """An AuthenticateResponse is returned after successful authentication."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCESS_TOKEN_FIELD_NUMBER: builtins.int
    access_token: builtins.str
    "access_token is a JWT where only the expiration should be deemed\n    important.\n    Future(erd): maybe a refresh_token\n    "

    def __init__(self, *, access_token: builtins.str = ...) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["access_token", b"access_token"]
    ) -> None: ...

global___AuthenticateToResponse = AuthenticateToResponse
