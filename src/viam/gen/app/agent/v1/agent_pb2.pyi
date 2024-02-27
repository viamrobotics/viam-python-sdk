"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PackageFormat:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PackageFormatEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _PackageFormat.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PACKAGE_FORMAT_UNSPECIFIED: _PackageFormat.ValueType
    "unknown/unset (autodetection may be attempted)"
    PACKAGE_FORMAT_RAW: _PackageFormat.ValueType
    "do nothing"
    PACKAGE_FORMAT_XZ: _PackageFormat.ValueType
    "decompress .xz file"
    PACKAGE_FORMAT_EXECUTABLE: _PackageFormat.ValueType
    "set executable permissions"
    PACKAGE_FORMAT_XZ_EXECUTABLE: _PackageFormat.ValueType
    "decompress and set executable"

class PackageFormat(_PackageFormat, metaclass=_PackageFormatEnumTypeWrapper): ...

PACKAGE_FORMAT_UNSPECIFIED: PackageFormat.ValueType
"unknown/unset (autodetection may be attempted)"
PACKAGE_FORMAT_RAW: PackageFormat.ValueType
"do nothing"
PACKAGE_FORMAT_XZ: PackageFormat.ValueType
"decompress .xz file"
PACKAGE_FORMAT_EXECUTABLE: PackageFormat.ValueType
"set executable permissions"
PACKAGE_FORMAT_XZ_EXECUTABLE: PackageFormat.ValueType
"decompress and set executable"
global___PackageFormat = PackageFormat

@typing_extensions.final
class GetAgentConfigRequest(google.protobuf.message.Message):
    """App side"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str

    def __init__(self, *, id: builtins.str = ...) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["id", b"id"]
    ) -> None: ...

global___GetAgentConfigRequest = GetAgentConfigRequest

@typing_extensions.final
class GetAgentConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    AGENT_CONFIG_FIELD_NUMBER: builtins.int

    @property
    def agent_config(self) -> global___AppAgentConfig: ...
    def __init__(
        self, *, agent_config: global___AppAgentConfig | None = ...
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["agent_config", b"agent_config"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["agent_config", b"agent_config"]
    ) -> None: ...

global___GetAgentConfigResponse = GetAgentConfigResponse

@typing_extensions.final
class UpdateAgentConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    AGENT_CONFIG_FIELD_NUMBER: builtins.int
    id: builtins.str

    @property
    def agent_config(self) -> global___AppAgentConfig: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        agent_config: global___AppAgentConfig | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["agent_config", b"agent_config"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "agent_config", b"agent_config", "id", b"id"
        ],
    ) -> None: ...

global___UpdateAgentConfigRequest = UpdateAgentConfigRequest

@typing_extensions.final
class UpdateAgentConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    AGENT_CONFIG_FIELD_NUMBER: builtins.int

    @property
    def agent_config(self) -> global___AppAgentConfig: ...
    def __init__(
        self, *, agent_config: global___AppAgentConfig | None = ...
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["agent_config", b"agent_config"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["agent_config", b"agent_config"]
    ) -> None: ...

global___UpdateAgentConfigResponse = UpdateAgentConfigResponse

@typing_extensions.final
class AppAgentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class SubsystemConfigsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___AppSubsystemConfig: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___AppSubsystemConfig | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    SUBSYSTEM_CONFIGS_FIELD_NUMBER: builtins.int

    @property
    def subsystem_configs(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        builtins.str, global___AppSubsystemConfig
    ]: ...
    def __init__(
        self,
        *,
        subsystem_configs: collections.abc.Mapping[
            builtins.str, global___AppSubsystemConfig
        ]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "subsystem_configs", b"subsystem_configs"
        ],
    ) -> None: ...

global___AppAgentConfig = AppAgentConfig

@typing_extensions.final
class AppSubsystemConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RELEASE_CHANNEL_FIELD_NUMBER: builtins.int
    PIN_VERSION_FIELD_NUMBER: builtins.int
    PIN_URL_FIELD_NUMBER: builtins.int
    DISABLE_SUBSYSTEM_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    release_channel: builtins.str
    pin_version: builtins.str
    pin_url: builtins.str
    disable_subsystem: builtins.bool

    @property
    def attributes(self) -> google.protobuf.struct_pb2.Struct: ...
    def __init__(
        self,
        *,
        release_channel: builtins.str = ...,
        pin_version: builtins.str = ...,
        pin_url: builtins.str = ...,
        disable_subsystem: builtins.bool = ...,
        attributes: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["attributes", b"attributes"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "attributes",
            b"attributes",
            "disable_subsystem",
            b"disable_subsystem",
            "pin_url",
            b"pin_url",
            "pin_version",
            b"pin_version",
            "release_channel",
            b"release_channel",
        ],
    ) -> None: ...

global___AppSubsystemConfig = AppSubsystemConfig

@typing_extensions.final
class DeviceAgentConfigRequest(google.protobuf.message.Message):
    """Device side"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class SubsystemVersionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str

        def __init__(
            self, *, key: builtins.str = ..., value: builtins.str = ...
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    ID_FIELD_NUMBER: builtins.int
    HOST_INFO_FIELD_NUMBER: builtins.int
    SUBSYSTEM_VERSIONS_FIELD_NUMBER: builtins.int
    id: builtins.str
    "robot partID"

    @property
    def host_info(self) -> global___HostInfo:
        """info about the host system"""

    @property
    def subsystem_versions(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """current subsystems and versions"""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        host_info: global___HostInfo | None = ...,
        subsystem_versions: collections.abc.Mapping[builtins.str, builtins.str]
        | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["host_info", b"host_info"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "host_info",
            b"host_info",
            "id",
            b"id",
            "subsystem_versions",
            b"subsystem_versions",
        ],
    ) -> None: ...

global___DeviceAgentConfigRequest = DeviceAgentConfigRequest

@typing_extensions.final
class DeviceAgentConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class SubsystemConfigsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str

        @property
        def value(self) -> global___DeviceSubsystemConfig: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___DeviceSubsystemConfig | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    SUBSYSTEM_CONFIGS_FIELD_NUMBER: builtins.int
    CHECK_INTERVAL_FIELD_NUMBER: builtins.int

    @property
    def subsystem_configs(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        builtins.str, global___DeviceSubsystemConfig
    ]:
        """subsystems to be installed/configured/updated
        note: previously installed subsystems will be removed from the system if removed from this list
        """

    @property
    def check_interval(self) -> google.protobuf.duration_pb2.Duration:
        """how often this request should be repeated"""

    def __init__(
        self,
        *,
        subsystem_configs: collections.abc.Mapping[
            builtins.str, global___DeviceSubsystemConfig
        ]
        | None = ...,
        check_interval: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["check_interval", b"check_interval"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "check_interval",
            b"check_interval",
            "subsystem_configs",
            b"subsystem_configs",
        ],
    ) -> None: ...

global___DeviceAgentConfigResponse = DeviceAgentConfigResponse

@typing_extensions.final
class DeviceSubsystemConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UPDATE_INFO_FIELD_NUMBER: builtins.int
    DISABLE_FIELD_NUMBER: builtins.int
    FORCE_RESTART_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int

    @property
    def update_info(self) -> global___SubsystemUpdateInfo:
        """data needed to download/validate the subsystem"""
    disable: builtins.bool
    "if this subsystem is disabled and should not be started by the agent"
    force_restart: builtins.bool
    "force_restart will restart the subsystem, even if no updates are available"

    @property
    def attributes(self) -> google.protobuf.struct_pb2.Struct:
        """arbitrary config sections"""

    def __init__(
        self,
        *,
        update_info: global___SubsystemUpdateInfo | None = ...,
        disable: builtins.bool = ...,
        force_restart: builtins.bool = ...,
        attributes: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "attributes", b"attributes", "update_info", b"update_info"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "attributes",
            b"attributes",
            "disable",
            b"disable",
            "force_restart",
            b"force_restart",
            "update_info",
            b"update_info",
        ],
    ) -> None: ...

global___DeviceSubsystemConfig = DeviceSubsystemConfig

@typing_extensions.final
class HostInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PLATFORM_FIELD_NUMBER: builtins.int
    DISTRO_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    platform: builtins.str
    "platform is the docker styled combination of kernel and architecture. Ex: linux/amd64, darwin/arm64"
    distro: builtins.str
    "ID and VERSION_ID fields from /etc/os-release, colon seperated. Ex: ubuntu:22.04, debian:11"

    @property
    def tags(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """additional tags for specific hardware or software that's present and may affect software selection
        ex: "jetson", "rpi4", "systemd", etc.
        """

    def __init__(
        self,
        *,
        platform: builtins.str = ...,
        distro: builtins.str = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "distro", b"distro", "platform", b"platform", "tags", b"tags"
        ],
    ) -> None: ...

global___HostInfo = HostInfo

@typing_extensions.final
class SubsystemUpdateInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILENAME_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    SHA256_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    filename: builtins.str
    "unpacked filename as it is expected on disk (regardless of url)"
    url: builtins.str
    "url to download from"
    version: builtins.str
    "version expected at the url"
    sha256: builtins.bytes
    "sha256 sum of file as downloaded"
    format: global___PackageFormat.ValueType
    "determines if decompression or executable permissions are needed"

    def __init__(
        self,
        *,
        filename: builtins.str = ...,
        url: builtins.str = ...,
        version: builtins.str = ...,
        sha256: builtins.bytes = ...,
        format: global___PackageFormat.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "filename",
            b"filename",
            "format",
            b"format",
            "sha256",
            b"sha256",
            "url",
            b"url",
            "version",
            b"version",
        ],
    ) -> None: ...

global___SubsystemUpdateInfo = SubsystemUpdateInfo
