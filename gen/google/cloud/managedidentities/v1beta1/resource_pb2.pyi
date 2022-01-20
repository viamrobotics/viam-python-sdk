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

class Domain(google.protobuf.message.Message):
    """Represents a managed Microsoft Active Directory domain.
    If the domain is being changed, it will be placed into the UPDATING state,
    which indicates that the resource is being reconciled. At this point, Get
    will reflect an intermediate state.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _State:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STATE_UNSPECIFIED: Domain.State.ValueType = ...  # 0
        """Not set."""

        CREATING: Domain.State.ValueType = ...  # 1
        """The domain is being created."""

        READY: Domain.State.ValueType = ...  # 2
        """The domain has been created and is fully usable."""

        UPDATING: Domain.State.ValueType = ...  # 3
        """The domain's configuration is being updated."""

        DELETING: Domain.State.ValueType = ...  # 4
        """The domain is being deleted."""

        REPAIRING: Domain.State.ValueType = ...  # 5
        """The domain is being repaired and may be unusable. Details
        can be found in the `status_message` field.
        """

        PERFORMING_MAINTENANCE: Domain.State.ValueType = ...  # 6
        """The domain is undergoing maintenance."""

        UNAVAILABLE: Domain.State.ValueType = ...  # 7
        """The domain is not serving requests."""

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """Represents the different states of a managed domain."""
        pass

    STATE_UNSPECIFIED: Domain.State.ValueType = ...  # 0
    """Not set."""

    CREATING: Domain.State.ValueType = ...  # 1
    """The domain is being created."""

    READY: Domain.State.ValueType = ...  # 2
    """The domain has been created and is fully usable."""

    UPDATING: Domain.State.ValueType = ...  # 3
    """The domain's configuration is being updated."""

    DELETING: Domain.State.ValueType = ...  # 4
    """The domain is being deleted."""

    REPAIRING: Domain.State.ValueType = ...  # 5
    """The domain is being repaired and may be unusable. Details
    can be found in the `status_message` field.
    """

    PERFORMING_MAINTENANCE: Domain.State.ValueType = ...  # 6
    """The domain is undergoing maintenance."""

    UNAVAILABLE: Domain.State.ValueType = ...  # 7
    """The domain is not serving requests."""


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
    LABELS_FIELD_NUMBER: builtins.int
    AUTHORIZED_NETWORKS_FIELD_NUMBER: builtins.int
    RESERVED_IP_RANGE_FIELD_NUMBER: builtins.int
    LOCATIONS_FIELD_NUMBER: builtins.int
    ADMIN_FIELD_NUMBER: builtins.int
    FQDN_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    STATUS_MESSAGE_FIELD_NUMBER: builtins.int
    TRUSTS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The unique name of the domain using the form:
    `projects/{project_id}/locations/global/domains/{domain_name}`.
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Optional. Resource labels that can contain user-provided metadata."""
        pass
    @property
    def authorized_networks(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Optional. The full names of the Google Compute Engine
        [networks](/compute/docs/networks-and-firewalls#networks) the domain
        instance is connected to. Networks can be added using UpdateDomain.
        The domain is only available on networks listed in `authorized_networks`.
        If CIDR subnets overlap between networks, domain creation will fail.
        """
        pass
    reserved_ip_range: typing.Text = ...
    """Required. The CIDR range of internal addresses that are reserved for this
    domain. Reserved networks must be /24 or larger. Ranges must be
    unique and non-overlapping with existing subnets in
    [Domain].[authorized_networks].
    """

    @property
    def locations(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Required. Locations where domain needs to be provisioned.
        [regions][compute/docs/regions-zones/]
        e.g. us-west1 or us-east4
        Service supports up to 4 locations at once. Each location will use a /26
        block.
        """
        pass
    admin: typing.Text = ...
    """Optional. The name of delegated administrator account used to perform
    Active Directory operations. If not specified, `setupadmin` will be used.
    """

    fqdn: typing.Text = ...
    """Output only. The fully-qualified domain name of the exposed domain used by
    clients to connect to the service. Similar to what would be chosen for an
    Active Directory set up on an internal network.
    """

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time the instance was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The last update time."""
        pass
    state: global___Domain.State.ValueType = ...
    """Output only. The current state of this domain."""

    status_message: typing.Text = ...
    """Output only. Additional information about the current status of this
    domain, if available.
    """

    @property
    def trusts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Trust]:
        """Output only. The current trusts associated with the domain."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        authorized_networks : typing.Optional[typing.Iterable[typing.Text]] = ...,
        reserved_ip_range : typing.Text = ...,
        locations : typing.Optional[typing.Iterable[typing.Text]] = ...,
        admin : typing.Text = ...,
        fqdn : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        state : global___Domain.State.ValueType = ...,
        status_message : typing.Text = ...,
        trusts : typing.Optional[typing.Iterable[global___Trust]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["admin",b"admin","authorized_networks",b"authorized_networks","create_time",b"create_time","fqdn",b"fqdn","labels",b"labels","locations",b"locations","name",b"name","reserved_ip_range",b"reserved_ip_range","state",b"state","status_message",b"status_message","trusts",b"trusts","update_time",b"update_time"]) -> None: ...
global___Domain = Domain

class Trust(google.protobuf.message.Message):
    """Represents a relationship between two domains. This allows a controller in
    one domain to authenticate a user in another domain.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _State:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STATE_UNSPECIFIED: Trust.State.ValueType = ...  # 0
        """Not set."""

        CREATING: Trust.State.ValueType = ...  # 1
        """The domain trust is being created."""

        UPDATING: Trust.State.ValueType = ...  # 2
        """The domain trust is being updated."""

        DELETING: Trust.State.ValueType = ...  # 3
        """The domain trust is being deleted."""

        CONNECTED: Trust.State.ValueType = ...  # 4
        """The domain trust is connected."""

        DISCONNECTED: Trust.State.ValueType = ...  # 5
        """The domain trust is disconnected."""

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """Represents the different states of a domain trust."""
        pass

    STATE_UNSPECIFIED: Trust.State.ValueType = ...  # 0
    """Not set."""

    CREATING: Trust.State.ValueType = ...  # 1
    """The domain trust is being created."""

    UPDATING: Trust.State.ValueType = ...  # 2
    """The domain trust is being updated."""

    DELETING: Trust.State.ValueType = ...  # 3
    """The domain trust is being deleted."""

    CONNECTED: Trust.State.ValueType = ...  # 4
    """The domain trust is connected."""

    DISCONNECTED: Trust.State.ValueType = ...  # 5
    """The domain trust is disconnected."""


    class _TrustType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TrustTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TrustType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TRUST_TYPE_UNSPECIFIED: Trust.TrustType.ValueType = ...  # 0
        """Not set."""

        FOREST: Trust.TrustType.ValueType = ...  # 1
        """The forest trust."""

        EXTERNAL: Trust.TrustType.ValueType = ...  # 2
        """The external domain trust."""

    class TrustType(_TrustType, metaclass=_TrustTypeEnumTypeWrapper):
        """Represents the different inter-forest trust types."""
        pass

    TRUST_TYPE_UNSPECIFIED: Trust.TrustType.ValueType = ...  # 0
    """Not set."""

    FOREST: Trust.TrustType.ValueType = ...  # 1
    """The forest trust."""

    EXTERNAL: Trust.TrustType.ValueType = ...  # 2
    """The external domain trust."""


    class _TrustDirection:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TrustDirectionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TrustDirection.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TRUST_DIRECTION_UNSPECIFIED: Trust.TrustDirection.ValueType = ...  # 0
        """Not set."""

        INBOUND: Trust.TrustDirection.ValueType = ...  # 1
        """The inbound direction represents the trusting side."""

        OUTBOUND: Trust.TrustDirection.ValueType = ...  # 2
        """The outboud direction represents the trusted side."""

        BIDIRECTIONAL: Trust.TrustDirection.ValueType = ...  # 3
        """The bidirectional direction represents the trusted / trusting side."""

    class TrustDirection(_TrustDirection, metaclass=_TrustDirectionEnumTypeWrapper):
        """Represents the direction of trust.
        See
        [System.DirectoryServices.ActiveDirectory.TrustDirection](https://docs.microsoft.com/en-us/dotnet/api/system.directoryservices.activedirectory.trustdirection?view=netframework-4.7.2)
        for more information.
        """
        pass

    TRUST_DIRECTION_UNSPECIFIED: Trust.TrustDirection.ValueType = ...  # 0
    """Not set."""

    INBOUND: Trust.TrustDirection.ValueType = ...  # 1
    """The inbound direction represents the trusting side."""

    OUTBOUND: Trust.TrustDirection.ValueType = ...  # 2
    """The outboud direction represents the trusted side."""

    BIDIRECTIONAL: Trust.TrustDirection.ValueType = ...  # 3
    """The bidirectional direction represents the trusted / trusting side."""


    TARGET_DOMAIN_NAME_FIELD_NUMBER: builtins.int
    TRUST_TYPE_FIELD_NUMBER: builtins.int
    TRUST_DIRECTION_FIELD_NUMBER: builtins.int
    SELECTIVE_AUTHENTICATION_FIELD_NUMBER: builtins.int
    TARGET_DNS_IP_ADDRESSES_FIELD_NUMBER: builtins.int
    TRUST_HANDSHAKE_SECRET_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    STATE_DESCRIPTION_FIELD_NUMBER: builtins.int
    LAST_TRUST_HEARTBEAT_TIME_FIELD_NUMBER: builtins.int
    target_domain_name: typing.Text = ...
    """The fully qualified target domain name which will be in trust with the
    current domain.
    """

    trust_type: global___Trust.TrustType.ValueType = ...
    """The type of trust represented by the trust resource."""

    trust_direction: global___Trust.TrustDirection.ValueType = ...
    """The trust direction, which decides if the current domain is trusted,
    trusting, or both.
    """

    selective_authentication: builtins.bool = ...
    """The trust authentication type, which decides whether the trusted side has
    forest/domain wide access or selective access to an approved set of
    resources.
    """

    @property
    def target_dns_ip_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The target DNS server IP addresses which can resolve the remote domain
        involved in the trust.
        """
        pass
    trust_handshake_secret: typing.Text = ...
    """Input only. The trust secret used for the handshake
    with the target domain. It will not be stored.
    """

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time the instance was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The last update time."""
        pass
    state: global___Trust.State.ValueType = ...
    """Output only. The current state of the trust."""

    state_description: typing.Text = ...
    """Output only. Additional information about the current state of the
    trust, if available.
    """

    @property
    def last_trust_heartbeat_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The last heartbeat time when the trust was known to be
        connected.
        """
        pass
    def __init__(self,
        *,
        target_domain_name : typing.Text = ...,
        trust_type : global___Trust.TrustType.ValueType = ...,
        trust_direction : global___Trust.TrustDirection.ValueType = ...,
        selective_authentication : builtins.bool = ...,
        target_dns_ip_addresses : typing.Optional[typing.Iterable[typing.Text]] = ...,
        trust_handshake_secret : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        state : global___Trust.State.ValueType = ...,
        state_description : typing.Text = ...,
        last_trust_heartbeat_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","last_trust_heartbeat_time",b"last_trust_heartbeat_time","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","last_trust_heartbeat_time",b"last_trust_heartbeat_time","selective_authentication",b"selective_authentication","state",b"state","state_description",b"state_description","target_dns_ip_addresses",b"target_dns_ip_addresses","target_domain_name",b"target_domain_name","trust_direction",b"trust_direction","trust_handshake_secret",b"trust_handshake_secret","trust_type",b"trust_type","update_time",b"update_time"]) -> None: ...
global___Trust = Trust
