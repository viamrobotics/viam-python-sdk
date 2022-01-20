"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.billing.budgets.v1.budget_model_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CreateBudgetRequest(google.protobuf.message.Message):
    """Request for CreateBudget"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    BUDGET_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the billing account to create the budget in. Values
    are of the form `billingAccounts/{billingAccountId}`.
    """

    @property
    def budget(self) -> google.cloud.billing.budgets.v1.budget_model_pb2.Budget:
        """Required. Budget to create."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        budget : typing.Optional[google.cloud.billing.budgets.v1.budget_model_pb2.Budget] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["budget",b"budget"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["budget",b"budget","parent",b"parent"]) -> None: ...
global___CreateBudgetRequest = CreateBudgetRequest

class UpdateBudgetRequest(google.protobuf.message.Message):
    """Request for UpdateBudget"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BUDGET_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def budget(self) -> google.cloud.billing.budgets.v1.budget_model_pb2.Budget:
        """Required. The updated budget object.
        The budget to update is specified by the budget name in the budget.
        """
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. Indicates which fields in the provided budget to update.
        Read-only fields (such as `name`) cannot be changed. If this is not
        provided, then only fields with non-default values from the request are
        updated. See
        https://developers.google.com/protocol-buffers/docs/proto3#default for more
        details about default values.
        """
        pass
    def __init__(self,
        *,
        budget : typing.Optional[google.cloud.billing.budgets.v1.budget_model_pb2.Budget] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["budget",b"budget","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["budget",b"budget","update_mask",b"update_mask"]) -> None: ...
global___UpdateBudgetRequest = UpdateBudgetRequest

class GetBudgetRequest(google.protobuf.message.Message):
    """Request for GetBudget"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Name of budget to get. Values are of the form
    `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetBudgetRequest = GetBudgetRequest

class ListBudgetsRequest(google.protobuf.message.Message):
    """Request for ListBudgets"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. Name of billing account to list budgets under. Values
    are of the form `billingAccounts/{billingAccountId}`.
    """

    page_size: builtins.int = ...
    """Optional. The maximum number of budgets to return per page.
    The default and maximum value are 100.
    """

    page_token: typing.Text = ...
    """Optional. The value returned by the last `ListBudgetsResponse` which
    indicates that this is a continuation of a prior `ListBudgets` call,
    and that the system should return the next page of data.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListBudgetsRequest = ListBudgetsRequest

class ListBudgetsResponse(google.protobuf.message.Message):
    """Response for ListBudgets"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BUDGETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def budgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.billing.budgets.v1.budget_model_pb2.Budget]:
        """List of the budgets owned by the requested billing account."""
        pass
    next_page_token: typing.Text = ...
    """If not empty, indicates that there may be more budgets that match the
    request; this value should be passed in a new `ListBudgetsRequest`.
    """

    def __init__(self,
        *,
        budgets : typing.Optional[typing.Iterable[google.cloud.billing.budgets.v1.budget_model_pb2.Budget]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["budgets",b"budgets","next_page_token",b"next_page_token"]) -> None: ...
global___ListBudgetsResponse = ListBudgetsResponse

class DeleteBudgetRequest(google.protobuf.message.Message):
    """Request for DeleteBudget"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. Name of the budget to delete. Values are of the form
    `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteBudgetRequest = DeleteBudgetRequest
