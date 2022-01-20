"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.networkservices.v1beta1.common_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class EndpointPolicy(google.protobuf.message.Message):
    """EndpointPolicy is a resource that helps apply desired configuration
    on the endpoints that match specific criteria.
    For example, this resource can be used to apply "authentication config"
    an all endpoints that serve on port 8080.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _EndpointPolicyType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _EndpointPolicyTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EndpointPolicyType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        ENDPOINT_POLICY_TYPE_UNSPECIFIED: EndpointPolicy.EndpointPolicyType.ValueType = ...  # 0
        """Default value. Must not be used."""

        SIDECAR_PROXY: EndpointPolicy.EndpointPolicyType.ValueType = ...  # 1
        """Represents a proxy deployed as a sidecar."""

        GRPC_SERVER: EndpointPolicy.EndpointPolicyType.ValueType = ...  # 2
        """Represents a proxyless gRPC backend."""

    class EndpointPolicyType(_EndpointPolicyType, metaclass=_EndpointPolicyTypeEnumTypeWrapper):
        """The type of endpoint policy."""
        pass

    ENDPOINT_POLICY_TYPE_UNSPECIFIED: EndpointPolicy.EndpointPolicyType.ValueType = ...  # 0
    """Default value. Must not be used."""

    SIDECAR_PROXY: EndpointPolicy.EndpointPolicyType.ValueType = ...  # 1
    """Represents a proxy deployed as a sidecar."""

    GRPC_SERVER: EndpointPolicy.EndpointPolicyType.ValueType = ...  # 2
    """Represents a proxyless gRPC backend."""


    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    AUTHORIZATION_POLICY_FIELD_NUMBER: builtins.int
    ENDPOINT_MATCHER_FIELD_NUMBER: builtins.int
    TRAFFIC_PORT_SELECTOR_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SERVER_TLS_POLICY_FIELD_NUMBER: builtins.int
    CLIENT_TLS_POLICY_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Name of the EndpointPolicy resource. It matches pattern
    `projects/{project}/locations/global/endpointPolicies/{endpoint_policy}`.
    """

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The timestamp when the resource was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The timestamp when the resource was updated."""
        pass
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Optional. Set of label tags associated with the EndpointPolicy resource."""
        pass
    type: global___EndpointPolicy.EndpointPolicyType.ValueType = ...
    """Required. The type of endpoint policy. This is primarily used to validate
    the configuration.
    """

    authorization_policy: typing.Text = ...
    """Optional. This field specifies the URL of AuthorizationPolicy resource that
    applies authorization policies to the inbound traffic at the
    matched endpoints. Refer to Authorization. If this field is not
    specified, authorization is disabled(no authz checks) for this
    endpoint. Applicable only when EndpointPolicyType is
    SIDECAR_PROXY.
    """

    @property
    def endpoint_matcher(self) -> google.cloud.networkservices.v1beta1.common_pb2.EndpointMatcher:
        """Required. A matcher that selects endpoints to which the policies should be applied."""
        pass
    @property
    def traffic_port_selector(self) -> google.cloud.networkservices.v1beta1.common_pb2.TrafficPortSelector:
        """Optional. Port selector for the (matched) endpoints. If no port selector is
        provided, the matched config is applied to all ports.
        """
        pass
    description: typing.Text = ...
    """Optional. A free-text description of the resource. Max length 1024 characters."""

    server_tls_policy: typing.Text = ...
    """Optional. A URL referring to ServerTlsPolicy resource. ServerTlsPolicy is used to
    determine the authentication policy to be applied to terminate the inbound
    traffic at the identified backends. If this field is not set,
    authentication is disabled(open) for this endpoint.
    """

    client_tls_policy: typing.Text = ...
    """Optional. A URL referring to a ClientTlsPolicy resource. ClientTlsPolicy can be set
    to specify the authentication for traffic from the proxy to the actual
    endpoints. More specifically, it is applied to the outgoing traffic from
    the proxy to the endpoint. This is typically used for sidecar model where
    the proxy identifies itself as endpoint to the control plane, with the
    connection between sidecar and endpoint requiring authentication. If this
    field is not set, authentication is disabled(open). Applicable only when
    EndpointPolicyType is SIDECAR_PROXY.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        type : global___EndpointPolicy.EndpointPolicyType.ValueType = ...,
        authorization_policy : typing.Text = ...,
        endpoint_matcher : typing.Optional[google.cloud.networkservices.v1beta1.common_pb2.EndpointMatcher] = ...,
        traffic_port_selector : typing.Optional[google.cloud.networkservices.v1beta1.common_pb2.TrafficPortSelector] = ...,
        description : typing.Text = ...,
        server_tls_policy : typing.Text = ...,
        client_tls_policy : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","endpoint_matcher",b"endpoint_matcher","traffic_port_selector",b"traffic_port_selector","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["authorization_policy",b"authorization_policy","client_tls_policy",b"client_tls_policy","create_time",b"create_time","description",b"description","endpoint_matcher",b"endpoint_matcher","labels",b"labels","name",b"name","server_tls_policy",b"server_tls_policy","traffic_port_selector",b"traffic_port_selector","type",b"type","update_time",b"update_time"]) -> None: ...
global___EndpointPolicy = EndpointPolicy

class ListEndpointPoliciesRequest(google.protobuf.message.Message):
    """Request used with the ListEndpointPolicies method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project and location from which the EndpointPolicies should be
    listed, specified in the format `projects/*/locations/global`.
    """

    page_size: builtins.int = ...
    """Maximum number of EndpointPolicies to return per call."""

    page_token: typing.Text = ...
    """The value returned by the last `ListEndpointPoliciesResponse`
    Indicates that this is a continuation of a prior
    `ListEndpointPolicies` call, and that the system should return the
    next page of data.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListEndpointPoliciesRequest = ListEndpointPoliciesRequest

class ListEndpointPoliciesResponse(google.protobuf.message.Message):
    """Response returned by the ListEndpointPolicies method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENDPOINT_POLICIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def endpoint_policies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EndpointPolicy]:
        """List of EndpointPolicy resources."""
        pass
    next_page_token: typing.Text = ...
    """If there might be more results than those appearing in this response, then
    `next_page_token` is included. To get the next set of results, call this
    method again using the value of `next_page_token` as `page_token`.
    """

    def __init__(self,
        *,
        endpoint_policies : typing.Optional[typing.Iterable[global___EndpointPolicy]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_policies",b"endpoint_policies","next_page_token",b"next_page_token"]) -> None: ...
global___ListEndpointPoliciesResponse = ListEndpointPoliciesResponse

class GetEndpointPolicyRequest(google.protobuf.message.Message):
    """Request used with the GetEndpointPolicy method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. A name of the EndpointPolicy to get. Must be in the format
    `projects/*/locations/global/endpointPolicies/*`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetEndpointPolicyRequest = GetEndpointPolicyRequest

class CreateEndpointPolicyRequest(google.protobuf.message.Message):
    """Request used with the CreateEndpointPolicy method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    ENDPOINT_POLICY_ID_FIELD_NUMBER: builtins.int
    ENDPOINT_POLICY_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The parent resource of the EndpointPolicy. Must be in the
    format `projects/*/locations/global`.
    """

    endpoint_policy_id: typing.Text = ...
    """Required. Short name of the EndpointPolicy resource to be created.
    E.g. "CustomECS".
    """

    @property
    def endpoint_policy(self) -> global___EndpointPolicy:
        """Required. EndpointPolicy resource to be created."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        endpoint_policy_id : typing.Text = ...,
        endpoint_policy : typing.Optional[global___EndpointPolicy] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["endpoint_policy",b"endpoint_policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_policy",b"endpoint_policy","endpoint_policy_id",b"endpoint_policy_id","parent",b"parent"]) -> None: ...
global___CreateEndpointPolicyRequest = CreateEndpointPolicyRequest

class UpdateEndpointPolicyRequest(google.protobuf.message.Message):
    """Request used with the UpdateEndpointPolicy method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    ENDPOINT_POLICY_FIELD_NUMBER: builtins.int
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. Field mask is used to specify the fields to be overwritten in the
        EndpointPolicy resource by the update.
        The fields specified in the update_mask are relative to the resource, not
        the full request. A field will be overwritten if it is in the mask. If the
        user does not provide a mask then all fields will be overwritten.
        """
        pass
    @property
    def endpoint_policy(self) -> global___EndpointPolicy:
        """Required. Updated EndpointPolicy resource."""
        pass
    def __init__(self,
        *,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        endpoint_policy : typing.Optional[global___EndpointPolicy] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["endpoint_policy",b"endpoint_policy","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_policy",b"endpoint_policy","update_mask",b"update_mask"]) -> None: ...
global___UpdateEndpointPolicyRequest = UpdateEndpointPolicyRequest

class DeleteEndpointPolicyRequest(google.protobuf.message.Message):
    """Request used with the DeleteEndpointPolicy method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. A name of the EndpointPolicy to delete. Must be in the format
    `projects/*/locations/global/endpointPolicies/*`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteEndpointPolicyRequest = DeleteEndpointPolicyRequest
