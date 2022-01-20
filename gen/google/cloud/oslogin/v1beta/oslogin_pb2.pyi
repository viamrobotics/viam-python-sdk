"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.oslogin.common.common_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class LoginProfile(google.protobuf.message.Message):
    """The user profile information used for logging in to a virtual machine on
    Google Compute Engine.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class SshPublicKeysEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> google.cloud.oslogin.common.common_pb2.SshPublicKey: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[google.cloud.oslogin.common.common_pb2.SshPublicKey] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    POSIX_ACCOUNTS_FIELD_NUMBER: builtins.int
    SSH_PUBLIC_KEYS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. A unique user ID."""

    @property
    def posix_accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.oslogin.common.common_pb2.PosixAccount]:
        """The list of POSIX accounts associated with the user."""
        pass
    @property
    def ssh_public_keys(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, google.cloud.oslogin.common.common_pb2.SshPublicKey]:
        """A map from SSH public key fingerprint to the associated key object."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        posix_accounts : typing.Optional[typing.Iterable[google.cloud.oslogin.common.common_pb2.PosixAccount]] = ...,
        ssh_public_keys : typing.Optional[typing.Mapping[typing.Text, google.cloud.oslogin.common.common_pb2.SshPublicKey]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","posix_accounts",b"posix_accounts","ssh_public_keys",b"ssh_public_keys"]) -> None: ...
global___LoginProfile = LoginProfile

class DeletePosixAccountRequest(google.protobuf.message.Message):
    """A request message for deleting a POSIX account entry."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. A reference to the POSIX account to update. POSIX accounts are identified
    by the project ID they are associated with. A reference to the POSIX
    account is in format `users/{user}/projects/{project}`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeletePosixAccountRequest = DeletePosixAccountRequest

class DeleteSshPublicKeyRequest(google.protobuf.message.Message):
    """A request message for deleting an SSH public key."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The fingerprint of the public key to update. Public keys are identified by
    their SHA-256 fingerprint. The fingerprint of the public key is in format
    `users/{user}/sshPublicKeys/{fingerprint}`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteSshPublicKeyRequest = DeleteSshPublicKeyRequest

class GetLoginProfileRequest(google.protobuf.message.Message):
    """A request message for retrieving the login profile information for a user."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    SYSTEM_ID_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The unique ID for the user in format `users/{user}`."""

    project_id: typing.Text = ...
    """The project ID of the Google Cloud Platform project."""

    system_id: typing.Text = ...
    """A system ID for filtering the results of the request."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        project_id : typing.Text = ...,
        system_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","project_id",b"project_id","system_id",b"system_id"]) -> None: ...
global___GetLoginProfileRequest = GetLoginProfileRequest

class GetSshPublicKeyRequest(google.protobuf.message.Message):
    """A request message for retrieving an SSH public key."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The fingerprint of the public key to retrieve. Public keys are identified
    by their SHA-256 fingerprint. The fingerprint of the public key is in
    format `users/{user}/sshPublicKeys/{fingerprint}`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetSshPublicKeyRequest = GetSshPublicKeyRequest

class ImportSshPublicKeyRequest(google.protobuf.message.Message):
    """A request message for importing an SSH public key."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    SSH_PUBLIC_KEY_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The unique ID for the user in format `users/{user}`."""

    @property
    def ssh_public_key(self) -> google.cloud.oslogin.common.common_pb2.SshPublicKey:
        """Required. The SSH public key and expiration time."""
        pass
    project_id: typing.Text = ...
    """The project ID of the Google Cloud Platform project."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        ssh_public_key : typing.Optional[google.cloud.oslogin.common.common_pb2.SshPublicKey] = ...,
        project_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ssh_public_key",b"ssh_public_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","project_id",b"project_id","ssh_public_key",b"ssh_public_key"]) -> None: ...
global___ImportSshPublicKeyRequest = ImportSshPublicKeyRequest

class ImportSshPublicKeyResponse(google.protobuf.message.Message):
    """A response message for importing an SSH public key."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOGIN_PROFILE_FIELD_NUMBER: builtins.int
    @property
    def login_profile(self) -> global___LoginProfile:
        """The login profile information for the user."""
        pass
    def __init__(self,
        *,
        login_profile : typing.Optional[global___LoginProfile] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["login_profile",b"login_profile"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["login_profile",b"login_profile"]) -> None: ...
global___ImportSshPublicKeyResponse = ImportSshPublicKeyResponse

class UpdateSshPublicKeyRequest(google.protobuf.message.Message):
    """A request message for updating an SSH public key."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    SSH_PUBLIC_KEY_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The fingerprint of the public key to update. Public keys are identified by
    their SHA-256 fingerprint. The fingerprint of the public key is in format
    `users/{user}/sshPublicKeys/{fingerprint}`.
    """

    @property
    def ssh_public_key(self) -> google.cloud.oslogin.common.common_pb2.SshPublicKey:
        """Required. The SSH public key and expiration time."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Mask to control which fields get updated. Updates all if not present."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        ssh_public_key : typing.Optional[google.cloud.oslogin.common.common_pb2.SshPublicKey] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ssh_public_key",b"ssh_public_key","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","ssh_public_key",b"ssh_public_key","update_mask",b"update_mask"]) -> None: ...
global___UpdateSshPublicKeyRequest = UpdateSshPublicKeyRequest
