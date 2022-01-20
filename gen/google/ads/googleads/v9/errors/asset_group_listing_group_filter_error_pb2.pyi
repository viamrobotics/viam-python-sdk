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

class AssetGroupListingGroupFilterErrorEnum(google.protobuf.message.Message):
    """Proto file describing asset group asset errors.

    Container for enum describing possible asset group listing group filter
    errors.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AssetGroupListingGroupFilterError:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AssetGroupListingGroupFilterErrorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AssetGroupListingGroupFilterError.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 0
        """Enum unspecified."""

        UNKNOWN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 1
        """The received error code is not known in this version."""

        TREE_TOO_DEEP: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 2
        """Listing group tree is too deep."""

        UNIT_CANNOT_HAVE_CHILDREN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 3
        """Listing Group UNIT node cannot have children."""

        SUBDIVISION_MUST_HAVE_EVERYTHING_ELSE_CHILD: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 4
        """Listing Group SUBDIVISION node must have everything else child."""

        DIFFERENT_DIMENSION_TYPE_BETWEEN_SIBLINGS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 5
        """Dimension type of Listing Group must be the same as that of its siblings."""

        SAME_DIMENSION_VALUE_BETWEEN_SIBLINGS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 6
        """The sibling Listing Groups target exactly the same dimension value."""

        SAME_DIMENSION_TYPE_BETWEEN_ANCESTORS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 7
        """The dimension type is the same as one of the ancestor Listing Groups."""

        MULTIPLE_ROOTS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 8
        """Each Listing Group tree must have a single root."""

        INVALID_DIMENSION_VALUE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 9
        """Invalid Listing Group dimension value."""

        MUST_REFINE_HIERARCHICAL_PARENT_TYPE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 10
        """Hierarchical dimension must refine a dimension of the same type."""

        INVALID_PRODUCT_BIDDING_CATEGORY: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 11
        """Invalid Product Bidding Category."""

        CHANGING_CASE_VALUE_WITH_CHILDREN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 12
        """Modifying case value is allowed only while updating the entire subtree at
        the same time.
        """

        SUBDIVISION_HAS_CHILDREN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 13
        """Subdivision node has children which must be removed first."""

        CANNOT_REFINE_HIERARCHICAL_EVERYTHING_ELSE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 14
        """Dimension can't subdivide everything-else node in its own hierarchy."""

    class AssetGroupListingGroupFilterError(_AssetGroupListingGroupFilterError, metaclass=_AssetGroupListingGroupFilterErrorEnumTypeWrapper):
        """Enum describing possible asset group listing group filter errors."""
        pass

    UNSPECIFIED: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 0
    """Enum unspecified."""

    UNKNOWN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 1
    """The received error code is not known in this version."""

    TREE_TOO_DEEP: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 2
    """Listing group tree is too deep."""

    UNIT_CANNOT_HAVE_CHILDREN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 3
    """Listing Group UNIT node cannot have children."""

    SUBDIVISION_MUST_HAVE_EVERYTHING_ELSE_CHILD: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 4
    """Listing Group SUBDIVISION node must have everything else child."""

    DIFFERENT_DIMENSION_TYPE_BETWEEN_SIBLINGS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 5
    """Dimension type of Listing Group must be the same as that of its siblings."""

    SAME_DIMENSION_VALUE_BETWEEN_SIBLINGS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 6
    """The sibling Listing Groups target exactly the same dimension value."""

    SAME_DIMENSION_TYPE_BETWEEN_ANCESTORS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 7
    """The dimension type is the same as one of the ancestor Listing Groups."""

    MULTIPLE_ROOTS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 8
    """Each Listing Group tree must have a single root."""

    INVALID_DIMENSION_VALUE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 9
    """Invalid Listing Group dimension value."""

    MUST_REFINE_HIERARCHICAL_PARENT_TYPE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 10
    """Hierarchical dimension must refine a dimension of the same type."""

    INVALID_PRODUCT_BIDDING_CATEGORY: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 11
    """Invalid Product Bidding Category."""

    CHANGING_CASE_VALUE_WITH_CHILDREN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 12
    """Modifying case value is allowed only while updating the entire subtree at
    the same time.
    """

    SUBDIVISION_HAS_CHILDREN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 13
    """Subdivision node has children which must be removed first."""

    CANNOT_REFINE_HIERARCHICAL_EVERYTHING_ELSE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError.ValueType = ...  # 14
    """Dimension can't subdivide everything-else node in its own hierarchy."""


    def __init__(self,
        ) -> None: ...
global___AssetGroupListingGroupFilterErrorEnum = AssetGroupListingGroupFilterErrorEnum
