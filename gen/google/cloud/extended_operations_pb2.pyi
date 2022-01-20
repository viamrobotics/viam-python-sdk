"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.descriptor_pb2
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _OperationResponseMapping:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _OperationResponseMappingEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OperationResponseMapping.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    UNDEFINED: OperationResponseMapping.ValueType = ...  # 0
    """Do not use."""

    NAME: OperationResponseMapping.ValueType = ...  # 1
    """A field in an API-specific (custom) Operation object which carries the same
    meaning as google.longrunning.Operation.name.
    """

    STATUS: OperationResponseMapping.ValueType = ...  # 2
    """A field in an API-specific (custom) Operation object which carries the same
    meaning as google.longrunning.Operation.done. If the annotated field is of
    an enum type, `annotated_field_name == EnumType.DONE` semantics should be
    equivalent to `Operation.done == true`. If the annotated field is of type
    boolean, then it should follow the same semantics as Operation.done.
    Otherwise, a non-empty value should be treated as `Operation.done == true`.
    """

    ERROR_CODE: OperationResponseMapping.ValueType = ...  # 3
    """A field in an API-specific (custom) Operation object which carries the same
    meaning as google.longrunning.Operation.error.code.
    """

    ERROR_MESSAGE: OperationResponseMapping.ValueType = ...  # 4
    """A field in an API-specific (custom) Operation object which carries the same
    meaning as google.longrunning.Operation.error.message.
    """

class OperationResponseMapping(_OperationResponseMapping, metaclass=_OperationResponseMappingEnumTypeWrapper):
    """An enum to be used to mark the essential (for polling) fields in an
    API-specific Operation object. A custom Operation object may contain many
    different fields, but only few of them are essential to conduct a successful
    polling process.
    """
    pass

UNDEFINED: OperationResponseMapping.ValueType = ...  # 0
"""Do not use."""

NAME: OperationResponseMapping.ValueType = ...  # 1
"""A field in an API-specific (custom) Operation object which carries the same
meaning as google.longrunning.Operation.name.
"""

STATUS: OperationResponseMapping.ValueType = ...  # 2
"""A field in an API-specific (custom) Operation object which carries the same
meaning as google.longrunning.Operation.done. If the annotated field is of
an enum type, `annotated_field_name == EnumType.DONE` semantics should be
equivalent to `Operation.done == true`. If the annotated field is of type
boolean, then it should follow the same semantics as Operation.done.
Otherwise, a non-empty value should be treated as `Operation.done == true`.
"""

ERROR_CODE: OperationResponseMapping.ValueType = ...  # 3
"""A field in an API-specific (custom) Operation object which carries the same
meaning as google.longrunning.Operation.error.code.
"""

ERROR_MESSAGE: OperationResponseMapping.ValueType = ...  # 4
"""A field in an API-specific (custom) Operation object which carries the same
meaning as google.longrunning.Operation.error.message.
"""

global___OperationResponseMapping = OperationResponseMapping


operation_field: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.FieldOptions, global___OperationResponseMapping.ValueType] = ...
"""A field annotation that maps fields in an API-specific Operation object to
their standard counterparts in google.longrunning.Operation. See
OperationResponseMapping enum definition.
"""

operation_request_field: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.FieldOptions, typing.Text] = ...
"""A field annotation that maps fields in the initial request message
(the one which started the LRO) to their counterparts in the polling
request message. For non-standard LRO, the polling response may be missing
some of the information needed to make a subsequent polling request. The
missing information (for example, project or region ID) is contained in the
fields of the initial request message that this annotation must be applied
to. The string value of the annotation corresponds to the name of the
counterpart field in the polling request message that the annotated field's
value will be copied to.
"""

operation_response_field: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.FieldOptions, typing.Text] = ...
"""A field annotation that maps fields in the polling request message to their
counterparts in the initial and/or polling response message. The initial
and the polling methods return an API-specific Operation object. Some of
the fields from that response object must be reused in the subsequent
request (like operation name/ID) to fully identify the polled operation.
This annotation must be applied to the fields in the polling request
message, the string value of the annotation must correspond to the name of
the counterpart field in the Operation response object whose value will be
copied to the annotated field.
"""

operation_service: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.MethodOptions, typing.Text] = ...
"""A method annotation that maps an LRO method (the one which starts an LRO)
to the service, which will be used to poll for the operation status. The
annotation must be applied to the method which starts an LRO, the string
value of the annotation must correspond to the name of the service used to
poll for the operation status.
"""

operation_polling_method: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.MethodOptions, builtins.bool] = ...
"""A method annotation that marks methods that can be used for polling
operation status (e.g. the MyPollingService.Get(MyPollingRequest) method).
"""
