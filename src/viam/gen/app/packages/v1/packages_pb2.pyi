"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PackageType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PackageTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PackageType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PACKAGE_TYPE_UNSPECIFIED: _PackageType.ValueType
    PACKAGE_TYPE_ARCHIVE: _PackageType.ValueType
    PACKAGE_TYPE_ML_MODEL: _PackageType.ValueType
    PACKAGE_TYPE_MODULE: _PackageType.ValueType
    PACKAGE_TYPE_SLAM_MAP: _PackageType.ValueType

class PackageType(_PackageType, metaclass=_PackageTypeEnumTypeWrapper):
    ...
PACKAGE_TYPE_UNSPECIFIED: PackageType.ValueType
PACKAGE_TYPE_ARCHIVE: PackageType.ValueType
PACKAGE_TYPE_ML_MODEL: PackageType.ValueType
PACKAGE_TYPE_MODULE: PackageType.ValueType
PACKAGE_TYPE_SLAM_MAP: PackageType.ValueType
global___PackageType = PackageType

@typing_extensions.final
class FileInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    name: builtins.str
    size: builtins.int

    def __init__(self, *, name: builtins.str=..., size: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name', 'size', b'size']) -> None:
        ...
global___FileInfo = FileInfo

@typing_extensions.final
class PackageInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PLATFORM_FIELD_NUMBER: builtins.int
    FILES_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    name: builtins.str
    version: builtins.str
    type: global___PackageType.ValueType
    platform: builtins.str

    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FileInfo]:
        ...

    @property
    def metadata(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, organization_id: builtins.str=..., name: builtins.str=..., version: builtins.str=..., type: global___PackageType.ValueType=..., platform: builtins.str | None=..., files: collections.abc.Iterable[global___FileInfo] | None=..., metadata: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_platform', b'_platform', 'metadata', b'metadata', 'platform', b'platform']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_platform', b'_platform', 'files', b'files', 'metadata', b'metadata', 'name', b'name', 'organization_id', b'organization_id', 'platform', b'platform', 'type', b'type', 'version', b'version']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_platform', b'_platform']) -> typing_extensions.Literal['platform'] | None:
        ...
global___PackageInfo = PackageInfo

@typing_extensions.final
class CreatePackageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INFO_FIELD_NUMBER: builtins.int
    CONTENTS_FIELD_NUMBER: builtins.int

    @property
    def info(self) -> global___PackageInfo:
        ...
    contents: builtins.bytes
    '.tar.gz file'

    def __init__(self, *, info: global___PackageInfo | None=..., contents: builtins.bytes=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['contents', b'contents', 'info', b'info', 'package', b'package']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['contents', b'contents', 'info', b'info', 'package', b'package']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['package', b'package']) -> typing_extensions.Literal['info', 'contents'] | None:
        ...
global___CreatePackageRequest = CreatePackageRequest

@typing_extensions.final
class CreatePackageResponse(google.protobuf.message.Message):
    """Returns the package ID and version which are populated in GetPackageRequest and DeletePackageRequest to
    retrieve or delete this package.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    id: builtins.str
    version: builtins.str

    def __init__(self, *, id: builtins.str=..., version: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'version', b'version']) -> None:
        ...
global___CreatePackageResponse = CreatePackageResponse

@typing_extensions.final
class DeletePackageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    id: builtins.str
    version: builtins.str

    def __init__(self, *, id: builtins.str=..., version: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'version', b'version']) -> None:
        ...
global___DeletePackageRequest = DeletePackageRequest

@typing_extensions.final
class DeletePackageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___DeletePackageResponse = DeletePackageResponse

@typing_extensions.final
class Package(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INFO_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    CREATED_ON_FIELD_NUMBER: builtins.int
    CHECKSUM_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int

    @property
    def info(self) -> global___PackageInfo:
        ...
    url: builtins.str

    @property
    def created_on(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...
    checksum: builtins.str
    id: builtins.str

    def __init__(self, *, info: global___PackageInfo | None=..., url: builtins.str=..., created_on: google.protobuf.timestamp_pb2.Timestamp | None=..., checksum: builtins.str=..., id: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['created_on', b'created_on', 'info', b'info']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['checksum', b'checksum', 'created_on', b'created_on', 'id', b'id', 'info', b'info', 'url', b'url']) -> None:
        ...
global___Package = Package

@typing_extensions.final
class GetPackageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    INCLUDE_URL_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PLATFORM_FIELD_NUMBER: builtins.int
    id: builtins.str
    version: builtins.str
    include_url: builtins.bool
    type: global___PackageType.ValueType
    platform: builtins.str

    def __init__(self, *, id: builtins.str=..., version: builtins.str=..., include_url: builtins.bool | None=..., type: global___PackageType.ValueType | None=..., platform: builtins.str | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_include_url', b'_include_url', '_platform', b'_platform', '_type', b'_type', 'include_url', b'include_url', 'platform', b'platform', 'type', b'type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_include_url', b'_include_url', '_platform', b'_platform', '_type', b'_type', 'id', b'id', 'include_url', b'include_url', 'platform', b'platform', 'type', b'type', 'version', b'version']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_include_url', b'_include_url']) -> typing_extensions.Literal['include_url'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_platform', b'_platform']) -> typing_extensions.Literal['platform'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_type', b'_type']) -> typing_extensions.Literal['type'] | None:
        ...
global___GetPackageRequest = GetPackageRequest

@typing_extensions.final
class GetPackageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PACKAGE_FIELD_NUMBER: builtins.int

    @property
    def package(self) -> global___Package:
        ...

    def __init__(self, *, package: global___Package | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['package', b'package']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['package', b'package']) -> None:
        ...
global___GetPackageResponse = GetPackageResponse

@typing_extensions.final
class ListPackagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    INCLUDE_URL_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    name: builtins.str
    version: builtins.str
    type: global___PackageType.ValueType
    include_url: builtins.bool

    def __init__(self, *, organization_id: builtins.str=..., name: builtins.str | None=..., version: builtins.str | None=..., type: global___PackageType.ValueType | None=..., include_url: builtins.bool | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_include_url', b'_include_url', '_name', b'_name', '_type', b'_type', '_version', b'_version', 'include_url', b'include_url', 'name', b'name', 'type', b'type', 'version', b'version']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_include_url', b'_include_url', '_name', b'_name', '_type', b'_type', '_version', b'_version', 'include_url', b'include_url', 'name', b'name', 'organization_id', b'organization_id', 'type', b'type', 'version', b'version']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_include_url', b'_include_url']) -> typing_extensions.Literal['include_url'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_name', b'_name']) -> typing_extensions.Literal['name'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_type', b'_type']) -> typing_extensions.Literal['type'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_version', b'_version']) -> typing_extensions.Literal['version'] | None:
        ...
global___ListPackagesRequest = ListPackagesRequest

@typing_extensions.final
class ListPackagesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PACKAGES_FIELD_NUMBER: builtins.int

    @property
    def packages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Package]:
        ...

    def __init__(self, *, packages: collections.abc.Iterable[global___Package] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['packages', b'packages']) -> None:
        ...
global___ListPackagesResponse = ListPackagesResponse