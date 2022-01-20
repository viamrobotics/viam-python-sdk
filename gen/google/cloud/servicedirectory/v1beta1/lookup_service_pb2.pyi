"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.servicedirectory.v1beta1.service_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ResolveServiceRequest(google.protobuf.message.Message):
    """The request message for [LookupService.ResolveService][google.cloud.servicedirectory.v1beta1.LookupService.ResolveService].
    Looks up a service by its name, returns the service and its endpoints.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    MAX_ENDPOINTS_FIELD_NUMBER: builtins.int
    ENDPOINT_FILTER_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the service to resolve."""

    max_endpoints: builtins.int = ...
    """Optional. The maximum number of endpoints to return. Defaults to 25. Maximum is 100.
    If a value less than one is specified, the Default is used.
    If a value greater than the Maximum is specified, the Maximum is used.
    """

    endpoint_filter: typing.Text = ...
    """Optional. The filter applied to the endpoints of the resolved service.

    General `filter` string syntax:
    `<field> <operator> <value> (<logical connector>)`

    *   `<field>` can be `name`, `address`, `port`, or `metadata.<key>` for
        map field
    *   `<operator>` can be `<`, `>`, `<=`, `>=`, `!=`, `=`, `:`. Of which `:`
        means `HAS`, and is roughly the same as `=`
    *   `<value>` must be the same data type as field
    *   `<logical connector>` can be `AND`, `OR`, `NOT`

    Examples of valid filters:

    *   `metadata.owner` returns endpoints that have a annotation with the key
        `owner`, this is the same as `metadata:owner`
    *   `metadata.protocol=gRPC` returns endpoints that have key/value
        `protocol=gRPC`
    *   `address=192.108.1.105` returns endpoints that have this address
    *   `port>8080` returns endpoints that have port number larger than 8080
    *
    `name>projects/my-project/locations/us-east1/namespaces/my-namespace/services/my-service/endpoints/endpoint-c`
        returns endpoints that have name that is alphabetically later than the
        string, so "endpoint-e" is returned but "endpoint-a" is not
    *   `metadata.owner!=sd AND metadata.foo=bar` returns endpoints that have
        `owner` in annotation key but value is not `sd` AND have key/value
         `foo=bar`
    *   `doesnotexist.foo=bar` returns an empty list. Note that endpoint
        doesn't have a field called "doesnotexist". Since the filter does not
        match any endpoint, it returns no results

    For more information about filtering, see
    [API Filtering](https://aip.dev/160).
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        max_endpoints : builtins.int = ...,
        endpoint_filter : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint_filter",b"endpoint_filter","max_endpoints",b"max_endpoints","name",b"name"]) -> None: ...
global___ResolveServiceRequest = ResolveServiceRequest

class ResolveServiceResponse(google.protobuf.message.Message):
    """The response message for [LookupService.ResolveService][google.cloud.servicedirectory.v1beta1.LookupService.ResolveService]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SERVICE_FIELD_NUMBER: builtins.int
    @property
    def service(self) -> google.cloud.servicedirectory.v1beta1.service_pb2.Service: ...
    def __init__(self,
        *,
        service : typing.Optional[google.cloud.servicedirectory.v1beta1.service_pb2.Service] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["service",b"service"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["service",b"service"]) -> None: ...
global___ResolveServiceResponse = ResolveServiceResponse
