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

class TrafficDirectorLogEntry(google.protobuf.message.Message):
    """A common proto for describing how the Traffic Director handles
    xDS-connections/requests/responses.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ClientType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ClientTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ClientType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        CLIENT_TYPE_UNSPECIFIED: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 0
        """Unspecified."""

        ENVOY: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 1
        """Envoy client."""

        GRPC_JAVA: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 2
        """gRPC Java client."""

        GRPC_CPP: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 3
        """gRPC C++ client."""

        GRPC_PYTHON: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 4
        """gRPC Python client."""

        GRPC_GO: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 5
        """gRPC Go client."""

        GRPC_RUBY: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 6
        """gRPC Ruby client."""

        GRPC_PHP: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 7
        """gRPC Ruby client."""

        GRPC_NODE: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 8
        """gRPC Node client."""

        GRPC_CSHARP: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 9
        """gRPC CSharp client."""

        UNKNOWN: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 10
        """unknown client type."""

    class ClientType(_ClientType, metaclass=_ClientTypeEnumTypeWrapper):
        """Defines possible values of client type."""
        pass

    CLIENT_TYPE_UNSPECIFIED: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 0
    """Unspecified."""

    ENVOY: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 1
    """Envoy client."""

    GRPC_JAVA: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 2
    """gRPC Java client."""

    GRPC_CPP: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 3
    """gRPC C++ client."""

    GRPC_PYTHON: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 4
    """gRPC Python client."""

    GRPC_GO: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 5
    """gRPC Go client."""

    GRPC_RUBY: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 6
    """gRPC Ruby client."""

    GRPC_PHP: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 7
    """gRPC Ruby client."""

    GRPC_NODE: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 8
    """gRPC Node client."""

    GRPC_CSHARP: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 9
    """gRPC CSharp client."""

    UNKNOWN: TrafficDirectorLogEntry.ClientType.ValueType = ...  # 10
    """unknown client type."""


    class _TransportApiVersion:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TransportApiVersionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TransportApiVersion.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TRANSPORT_API_VERSION_UNSPECIFIED: TrafficDirectorLogEntry.TransportApiVersion.ValueType = ...  # 0
        """Unspecified."""

        V2: TrafficDirectorLogEntry.TransportApiVersion.ValueType = ...  # 1
        """v2 xDS version."""

        V3: TrafficDirectorLogEntry.TransportApiVersion.ValueType = ...  # 2
        """v3 xDS version."""

    class TransportApiVersion(_TransportApiVersion, metaclass=_TransportApiVersionEnumTypeWrapper):
        """Defines possible values of API version."""
        pass

    TRANSPORT_API_VERSION_UNSPECIFIED: TrafficDirectorLogEntry.TransportApiVersion.ValueType = ...  # 0
    """Unspecified."""

    V2: TrafficDirectorLogEntry.TransportApiVersion.ValueType = ...  # 1
    """v2 xDS version."""

    V3: TrafficDirectorLogEntry.TransportApiVersion.ValueType = ...  # 2
    """v3 xDS version."""


    NODE_ID_FIELD_NUMBER: builtins.int
    NODE_IP_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CLIENT_TYPE_FIELD_NUMBER: builtins.int
    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    TRANSPORT_API_VERSION_FIELD_NUMBER: builtins.int
    node_id: typing.Text = ...
    """An ID of xDS-client connecting to the Traffic Director."""

    node_ip: typing.Text = ...
    """The string representation of IPv4 or IPv6 address of xDS-client
    connecting to the Traffic Director.
    IPv4 address must be in the format defined in RFC791, four octets separated
    by a period. Size of a string is between 7-15 characters. Example: 1.2.3.4
    IPv6 address must be in one of the formats defined in RFC4291. Size of a
    string is between 7-39 characters. Example: 2001:DB8:0:0:8:800:200C:417A
    """

    description: typing.Text = ...
    """A free text describing details of the event."""

    client_type: global___TrafficDirectorLogEntry.ClientType.ValueType = ...
    """Type of xDS-client connecting to Traffic Director"""

    client_version: typing.Text = ...
    """The version of xDS-client connecting to Traffic Director."""

    transport_api_version: global___TrafficDirectorLogEntry.TransportApiVersion.ValueType = ...
    """The xDS API version used by xDS clients connecting to Traffic Director."""

    def __init__(self,
        *,
        node_id : typing.Text = ...,
        node_ip : typing.Text = ...,
        description : typing.Text = ...,
        client_type : global___TrafficDirectorLogEntry.ClientType.ValueType = ...,
        client_version : typing.Text = ...,
        transport_api_version : global___TrafficDirectorLogEntry.TransportApiVersion.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_type",b"client_type","client_version",b"client_version","description",b"description","node_id",b"node_id","node_ip",b"node_ip","transport_api_version",b"transport_api_version"]) -> None: ...
global___TrafficDirectorLogEntry = TrafficDirectorLogEntry
