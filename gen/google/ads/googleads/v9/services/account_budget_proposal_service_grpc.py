# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/account_budget_proposal_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.account_budget_proposal_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.ads.googleads.v9.services.account_budget_proposal_service_pb2


class AccountBudgetProposalServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetAccountBudgetProposal(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.account_budget_proposal_service_pb2.GetAccountBudgetProposalRequest, google.ads.googleads.v9.resources.account_budget_proposal_pb2.AccountBudgetProposal]') -> None:
        pass

    @abc.abstractmethod
    async def MutateAccountBudgetProposal(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.account_budget_proposal_service_pb2.MutateAccountBudgetProposalRequest, google.ads.googleads.v9.services.account_budget_proposal_service_pb2.MutateAccountBudgetProposalResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.AccountBudgetProposalService/GetAccountBudgetProposal': grpclib.const.Handler(
                self.GetAccountBudgetProposal,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.account_budget_proposal_service_pb2.GetAccountBudgetProposalRequest,
                google.ads.googleads.v9.resources.account_budget_proposal_pb2.AccountBudgetProposal,
            ),
            '/google.ads.googleads.v9.services.AccountBudgetProposalService/MutateAccountBudgetProposal': grpclib.const.Handler(
                self.MutateAccountBudgetProposal,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.account_budget_proposal_service_pb2.MutateAccountBudgetProposalRequest,
                google.ads.googleads.v9.services.account_budget_proposal_service_pb2.MutateAccountBudgetProposalResponse,
            ),
        }


class AccountBudgetProposalServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAccountBudgetProposal = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.AccountBudgetProposalService/GetAccountBudgetProposal',
            google.ads.googleads.v9.services.account_budget_proposal_service_pb2.GetAccountBudgetProposalRequest,
            google.ads.googleads.v9.resources.account_budget_proposal_pb2.AccountBudgetProposal,
        )
        self.MutateAccountBudgetProposal = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.AccountBudgetProposalService/MutateAccountBudgetProposal',
            google.ads.googleads.v9.services.account_budget_proposal_service_pb2.MutateAccountBudgetProposalRequest,
            google.ads.googleads.v9.services.account_budget_proposal_service_pb2.MutateAccountBudgetProposalResponse,
        )
