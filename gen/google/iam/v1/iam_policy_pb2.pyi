"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.iam.v1.options_pb2
import google.iam.v1.policy_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SetIamPolicyRequest(google.protobuf.message.Message):
    """Request message for `SetIamPolicy` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_FIELD_NUMBER: builtins.int
    POLICY_FIELD_NUMBER: builtins.int
    resource: typing.Text = ...
    """REQUIRED: The resource for which the policy is being specified.
    See the operation documentation for the appropriate value for this field.
    """

    @property
    def policy(self) -> google.iam.v1.policy_pb2.Policy:
        """REQUIRED: The complete policy to be applied to the `resource`. The size of
        the policy is limited to a few 10s of KB. An empty policy is a
        valid policy but certain Cloud Platform services (such as Projects)
        might reject them.
        """
        pass
    def __init__(self,
        *,
        resource : typing.Text = ...,
        policy : typing.Optional[google.iam.v1.policy_pb2.Policy] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["policy",b"policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["policy",b"policy","resource",b"resource"]) -> None: ...
global___SetIamPolicyRequest = SetIamPolicyRequest

class GetIamPolicyRequest(google.protobuf.message.Message):
    """Request message for `GetIamPolicy` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    resource: typing.Text = ...
    """REQUIRED: The resource for which the policy is being requested.
    See the operation documentation for the appropriate value for this field.
    """

    @property
    def options(self) -> google.iam.v1.options_pb2.GetPolicyOptions:
        """OPTIONAL: A `GetPolicyOptions` object for specifying options to
        `GetIamPolicy`. This field is only used by Cloud IAM.
        """
        pass
    def __init__(self,
        *,
        resource : typing.Text = ...,
        options : typing.Optional[google.iam.v1.options_pb2.GetPolicyOptions] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options",b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["options",b"options","resource",b"resource"]) -> None: ...
global___GetIamPolicyRequest = GetIamPolicyRequest

class TestIamPermissionsRequest(google.protobuf.message.Message):
    """Request message for `TestIamPermissions` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    resource: typing.Text = ...
    """REQUIRED: The resource for which the policy detail is being requested.
    See the operation documentation for the appropriate value for this field.
    """

    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The set of permissions to check for the `resource`. Permissions with
        wildcards (such as '*' or 'storage.*') are not allowed. For more
        information see
        [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).
        """
        pass
    def __init__(self,
        *,
        resource : typing.Text = ...,
        permissions : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["permissions",b"permissions","resource",b"resource"]) -> None: ...
global___TestIamPermissionsRequest = TestIamPermissionsRequest

class TestIamPermissionsResponse(google.protobuf.message.Message):
    """Response message for `TestIamPermissions` method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PERMISSIONS_FIELD_NUMBER: builtins.int
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """A subset of `TestPermissionsRequest.permissions` that the caller is
        allowed.
        """
        pass
    def __init__(self,
        *,
        permissions : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["permissions",b"permissions"]) -> None: ...
global___TestIamPermissionsResponse = TestIamPermissionsResponse
