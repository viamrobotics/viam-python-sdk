# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/income_range_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.income_range_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v9.services.income_range_view_service_pb2


class IncomeRangeViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetIncomeRangeView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.income_range_view_service_pb2.GetIncomeRangeViewRequest, google.ads.googleads.v9.resources.income_range_view_pb2.IncomeRangeView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.IncomeRangeViewService/GetIncomeRangeView': grpclib.const.Handler(
                self.GetIncomeRangeView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.income_range_view_service_pb2.GetIncomeRangeViewRequest,
                google.ads.googleads.v9.resources.income_range_view_pb2.IncomeRangeView,
            ),
        }


class IncomeRangeViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetIncomeRangeView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.IncomeRangeViewService/GetIncomeRangeView',
            google.ads.googleads.v9.services.income_range_view_service_pb2.GetIncomeRangeViewRequest,
            google.ads.googleads.v9.resources.income_range_view_pb2.IncomeRangeView,
        )
