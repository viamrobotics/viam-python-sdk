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

class BiddingStrategyErrorEnum(google.protobuf.message.Message):
    """Proto file describing bidding strategy errors.

    Container for enum describing possible bidding strategy errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _BiddingStrategyError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _BiddingStrategyErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BiddingStrategyError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        DUPLICATE_NAME: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 2
        """Each bidding strategy must have a unique name."""

        CANNOT_CHANGE_BIDDING_STRATEGY_TYPE: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 3
        """Bidding strategy type is immutable."""

        CANNOT_REMOVE_ASSOCIATED_STRATEGY: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 4
        """Only bidding strategies not linked to campaigns, adgroups or adgroup
        criteria can be removed.
        """

        BIDDING_STRATEGY_NOT_SUPPORTED: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 5
        """The specified bidding strategy is not supported."""

        INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 6
        """The bidding strategy is incompatible with the campaign's bidding
        strategy goal type.
        """

    class BiddingStrategyError(_BiddingStrategyError, metaclass=_BiddingStrategyErrorEnumTypeWrapper):
        """Enum describing possible bidding strategy errors."""
        pass

    UNSPECIFIED: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    DUPLICATE_NAME: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 2
    """Each bidding strategy must have a unique name."""

    CANNOT_CHANGE_BIDDING_STRATEGY_TYPE: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 3
    """Bidding strategy type is immutable."""

    CANNOT_REMOVE_ASSOCIATED_STRATEGY: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 4
    """Only bidding strategies not linked to campaigns, adgroups or adgroup
    criteria can be removed.
    """

    BIDDING_STRATEGY_NOT_SUPPORTED: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 5
    """The specified bidding strategy is not supported."""

    INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE: BiddingStrategyErrorEnum.BiddingStrategyError.ValueType = ...  # 6
    """The bidding strategy is incompatible with the campaign's bidding
    strategy goal type.
    """


    def __init__(self,
        ) -> None: ...
global___BiddingStrategyErrorEnum = BiddingStrategyErrorEnum
