"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.enums.conversion_value_rule_status_pb2
import google.ads.googleads.v8.enums.value_rule_device_type_pb2
import google.ads.googleads.v8.enums.value_rule_geo_location_match_type_pb2
import google.ads.googleads.v8.enums.value_rule_operation_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ConversionValueRule(google.protobuf.message.Message):
    """Proto file describing the Conversion Value Rule resource.

    A conversion value rule
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ValueRuleAction(google.protobuf.message.Message):
        """Action applied when rule is applied."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        OPERATION_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        operation: google.ads.googleads.v8.enums.value_rule_operation_pb2.ValueRuleOperationEnum.ValueRuleOperation.ValueType = ...
        """Specifies applied operation."""

        value: builtins.float = ...
        """Specifies applied value."""

        def __init__(self,
            *,
            operation : google.ads.googleads.v8.enums.value_rule_operation_pb2.ValueRuleOperationEnum.ValueRuleOperation.ValueType = ...,
            value : builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["operation",b"operation","value",b"value"]) -> None: ...

    class ValueRuleGeoLocationCondition(google.protobuf.message.Message):
        """Condition on Geo dimension."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        EXCLUDED_GEO_TARGET_CONSTANTS_FIELD_NUMBER: builtins.int
        EXCLUDED_GEO_MATCH_TYPE_FIELD_NUMBER: builtins.int
        GEO_TARGET_CONSTANTS_FIELD_NUMBER: builtins.int
        GEO_MATCH_TYPE_FIELD_NUMBER: builtins.int
        @property
        def excluded_geo_target_constants(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """Geo locations that advertisers want to exclude."""
            pass
        excluded_geo_match_type: google.ads.googleads.v8.enums.value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType.ValueType = ...
        """Excluded Geo location match type."""

        @property
        def geo_target_constants(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """Geo locations that advertisers want to include."""
            pass
        geo_match_type: google.ads.googleads.v8.enums.value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType.ValueType = ...
        """Included Geo location match type."""

        def __init__(self,
            *,
            excluded_geo_target_constants : typing.Optional[typing.Iterable[typing.Text]] = ...,
            excluded_geo_match_type : google.ads.googleads.v8.enums.value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType.ValueType = ...,
            geo_target_constants : typing.Optional[typing.Iterable[typing.Text]] = ...,
            geo_match_type : google.ads.googleads.v8.enums.value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType.ValueType = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["excluded_geo_match_type",b"excluded_geo_match_type","excluded_geo_target_constants",b"excluded_geo_target_constants","geo_match_type",b"geo_match_type","geo_target_constants",b"geo_target_constants"]) -> None: ...

    class ValueRuleDeviceCondition(google.protobuf.message.Message):
        """Condition on Device dimension."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        DEVICE_TYPES_FIELD_NUMBER: builtins.int
        @property
        def device_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[google.ads.googleads.v8.enums.value_rule_device_type_pb2.ValueRuleDeviceTypeEnum.ValueRuleDeviceType.ValueType]:
            """Value for device type condition."""
            pass
        def __init__(self,
            *,
            device_types : typing.Optional[typing.Iterable[google.ads.googleads.v8.enums.value_rule_device_type_pb2.ValueRuleDeviceTypeEnum.ValueRuleDeviceType.ValueType]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["device_types",b"device_types"]) -> None: ...

    class ValueRuleAudienceCondition(google.protobuf.message.Message):
        """Condition on Audience dimension."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        USER_LISTS_FIELD_NUMBER: builtins.int
        USER_INTERESTS_FIELD_NUMBER: builtins.int
        @property
        def user_lists(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """User Lists."""
            pass
        @property
        def user_interests(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """User Interests."""
            pass
        def __init__(self,
            *,
            user_lists : typing.Optional[typing.Iterable[typing.Text]] = ...,
            user_interests : typing.Optional[typing.Iterable[typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["user_interests",b"user_interests","user_lists",b"user_lists"]) -> None: ...

    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    GEO_LOCATION_CONDITION_FIELD_NUMBER: builtins.int
    DEVICE_CONDITION_FIELD_NUMBER: builtins.int
    AUDIENCE_CONDITION_FIELD_NUMBER: builtins.int
    OWNER_CUSTOMER_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the conversion value rule.
    Conversion value rule resource names have the form:

    `customers/{customer_id}/conversionValueRules/{conversion_value_rule_id}`
    """

    id: builtins.int = ...
    """Output only. The ID of the conversion value rule."""

    @property
    def action(self) -> global___ConversionValueRule.ValueRuleAction:
        """Action applied when the rule is triggered."""
        pass
    @property
    def geo_location_condition(self) -> global___ConversionValueRule.ValueRuleGeoLocationCondition:
        """Condition for Geo location that must be satisfied for the value rule to
        apply.
        """
        pass
    @property
    def device_condition(self) -> global___ConversionValueRule.ValueRuleDeviceCondition:
        """Condition for device type that must be satisfied for the value rule to
        apply.
        """
        pass
    @property
    def audience_condition(self) -> global___ConversionValueRule.ValueRuleAudienceCondition:
        """Condition for audience that must be satisfied for the value rule to apply."""
        pass
    owner_customer: typing.Text = ...
    """Output only. The resource name of the conversion value rule's owner customer.
    When the value rule is inherited from a manager
    customer, owner_customer will be the resource name of the manager whereas
    the customer in the resource_name will be of the requesting serving
    customer.
    ** Read-only **
    """

    status: google.ads.googleads.v8.enums.conversion_value_rule_status_pb2.ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...
    """The status of the conversion value rule."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        id : builtins.int = ...,
        action : typing.Optional[global___ConversionValueRule.ValueRuleAction] = ...,
        geo_location_condition : typing.Optional[global___ConversionValueRule.ValueRuleGeoLocationCondition] = ...,
        device_condition : typing.Optional[global___ConversionValueRule.ValueRuleDeviceCondition] = ...,
        audience_condition : typing.Optional[global___ConversionValueRule.ValueRuleAudienceCondition] = ...,
        owner_customer : typing.Text = ...,
        status : google.ads.googleads.v8.enums.conversion_value_rule_status_pb2.ConversionValueRuleStatusEnum.ConversionValueRuleStatus.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["action",b"action","audience_condition",b"audience_condition","device_condition",b"device_condition","geo_location_condition",b"geo_location_condition"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action",b"action","audience_condition",b"audience_condition","device_condition",b"device_condition","geo_location_condition",b"geo_location_condition","id",b"id","owner_customer",b"owner_customer","resource_name",b"resource_name","status",b"status"]) -> None: ...
global___ConversionValueRule = ConversionValueRule
