"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v7.resources.account_budget_proposal_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetAccountBudgetProposalRequest(google.protobuf.message.Message):
    """Request message for
    [AccountBudgetProposalService.GetAccountBudgetProposal][google.ads.googleads.v7.services.AccountBudgetProposalService.GetAccountBudgetProposal].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the account-level budget proposal to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetAccountBudgetProposalRequest = GetAccountBudgetProposalRequest

class MutateAccountBudgetProposalRequest(google.protobuf.message.Message):
    """Request message for
    [AccountBudgetProposalService.MutateAccountBudgetProposal][google.ads.googleads.v7.services.AccountBudgetProposalService.MutateAccountBudgetProposal].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATION_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. The ID of the customer."""

    @property
    def operation(self) -> global___AccountBudgetProposalOperation:
        """Required. The operation to perform on an individual account-level budget proposal."""
        pass
    validate_only: builtins.bool = ...
    """If true, the request is validated but not executed. Only errors are
    returned, not results.
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operation : typing.Optional[global___AccountBudgetProposalOperation] = ...,
        validate_only : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["operation",b"operation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operation",b"operation","validate_only",b"validate_only"]) -> None: ...
global___MutateAccountBudgetProposalRequest = MutateAccountBudgetProposalRequest

class AccountBudgetProposalOperation(google.protobuf.message.Message):
    """A single operation to propose the creation of a new account-level budget or
    edit/end/remove an existing one.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    CREATE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """FieldMask that determines which budget fields are modified.  While budgets
        may be modified, proposals that propose such modifications are final.
        Therefore, update operations are not supported for proposals.

        Proposals that modify budgets have the 'update' proposal type.  Specifying
        a mask for any other proposal type is considered an error.
        """
        pass
    @property
    def create(self) -> google.ads.googleads.v7.resources.account_budget_proposal_pb2.AccountBudgetProposal:
        """Create operation: A new proposal to create a new budget, edit an
        existing budget, end an actively running budget, or remove an approved
        budget scheduled to start in the future.
        No resource name is expected for the new proposal.
        """
        pass
    remove: typing.Text = ...
    """Remove operation: A resource name for the removed proposal is expected,
    in this format:

    `customers/{customer_id}/accountBudgetProposals/{account_budget_proposal_id}`
    A request may be cancelled iff it is pending.
    """

    def __init__(self,
        *,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        create : typing.Optional[google.ads.googleads.v7.resources.account_budget_proposal_pb2.AccountBudgetProposal] = ...,
        remove : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","remove"]]: ...
global___AccountBudgetProposalOperation = AccountBudgetProposalOperation

class MutateAccountBudgetProposalResponse(google.protobuf.message.Message):
    """Response message for account-level budget mutate operations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> global___MutateAccountBudgetProposalResult:
        """The result of the mutate."""
        pass
    def __init__(self,
        *,
        result : typing.Optional[global___MutateAccountBudgetProposalResult] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["result",b"result"]) -> None: ...
global___MutateAccountBudgetProposalResponse = MutateAccountBudgetProposalResponse

class MutateAccountBudgetProposalResult(google.protobuf.message.Message):
    """The result for the account budget proposal mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___MutateAccountBudgetProposalResult = MutateAccountBudgetProposalResult
