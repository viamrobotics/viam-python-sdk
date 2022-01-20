# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/monitoring/v3/metric_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.metric_pb2
import google.api.monitored_resource_pb2
import google.api.resource_pb2
import google.monitoring.v3.alert_pb2
import google.monitoring.v3.common_pb2
import google.monitoring.v3.metric_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.rpc.status_pb2
import google.monitoring.v3.metric_service_pb2


class MetricServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListMonitoredResourceDescriptors(self, stream: 'grpclib.server.Stream[google.monitoring.v3.metric_service_pb2.ListMonitoredResourceDescriptorsRequest, google.monitoring.v3.metric_service_pb2.ListMonitoredResourceDescriptorsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetMonitoredResourceDescriptor(self, stream: 'grpclib.server.Stream[google.monitoring.v3.metric_service_pb2.GetMonitoredResourceDescriptorRequest, google.api.monitored_resource_pb2.MonitoredResourceDescriptor]') -> None:
        pass

    @abc.abstractmethod
    async def ListMetricDescriptors(self, stream: 'grpclib.server.Stream[google.monitoring.v3.metric_service_pb2.ListMetricDescriptorsRequest, google.monitoring.v3.metric_service_pb2.ListMetricDescriptorsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetMetricDescriptor(self, stream: 'grpclib.server.Stream[google.monitoring.v3.metric_service_pb2.GetMetricDescriptorRequest, google.api.metric_pb2.MetricDescriptor]') -> None:
        pass

    @abc.abstractmethod
    async def CreateMetricDescriptor(self, stream: 'grpclib.server.Stream[google.monitoring.v3.metric_service_pb2.CreateMetricDescriptorRequest, google.api.metric_pb2.MetricDescriptor]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteMetricDescriptor(self, stream: 'grpclib.server.Stream[google.monitoring.v3.metric_service_pb2.DeleteMetricDescriptorRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ListTimeSeries(self, stream: 'grpclib.server.Stream[google.monitoring.v3.metric_service_pb2.ListTimeSeriesRequest, google.monitoring.v3.metric_service_pb2.ListTimeSeriesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateTimeSeries(self, stream: 'grpclib.server.Stream[google.monitoring.v3.metric_service_pb2.CreateTimeSeriesRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def CreateServiceTimeSeries(self, stream: 'grpclib.server.Stream[google.monitoring.v3.metric_service_pb2.CreateTimeSeriesRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.monitoring.v3.MetricService/ListMonitoredResourceDescriptors': grpclib.const.Handler(
                self.ListMonitoredResourceDescriptors,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.metric_service_pb2.ListMonitoredResourceDescriptorsRequest,
                google.monitoring.v3.metric_service_pb2.ListMonitoredResourceDescriptorsResponse,
            ),
            '/google.monitoring.v3.MetricService/GetMonitoredResourceDescriptor': grpclib.const.Handler(
                self.GetMonitoredResourceDescriptor,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.metric_service_pb2.GetMonitoredResourceDescriptorRequest,
                google.api.monitored_resource_pb2.MonitoredResourceDescriptor,
            ),
            '/google.monitoring.v3.MetricService/ListMetricDescriptors': grpclib.const.Handler(
                self.ListMetricDescriptors,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.metric_service_pb2.ListMetricDescriptorsRequest,
                google.monitoring.v3.metric_service_pb2.ListMetricDescriptorsResponse,
            ),
            '/google.monitoring.v3.MetricService/GetMetricDescriptor': grpclib.const.Handler(
                self.GetMetricDescriptor,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.metric_service_pb2.GetMetricDescriptorRequest,
                google.api.metric_pb2.MetricDescriptor,
            ),
            '/google.monitoring.v3.MetricService/CreateMetricDescriptor': grpclib.const.Handler(
                self.CreateMetricDescriptor,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.metric_service_pb2.CreateMetricDescriptorRequest,
                google.api.metric_pb2.MetricDescriptor,
            ),
            '/google.monitoring.v3.MetricService/DeleteMetricDescriptor': grpclib.const.Handler(
                self.DeleteMetricDescriptor,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.metric_service_pb2.DeleteMetricDescriptorRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.monitoring.v3.MetricService/ListTimeSeries': grpclib.const.Handler(
                self.ListTimeSeries,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.metric_service_pb2.ListTimeSeriesRequest,
                google.monitoring.v3.metric_service_pb2.ListTimeSeriesResponse,
            ),
            '/google.monitoring.v3.MetricService/CreateTimeSeries': grpclib.const.Handler(
                self.CreateTimeSeries,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.metric_service_pb2.CreateTimeSeriesRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.monitoring.v3.MetricService/CreateServiceTimeSeries': grpclib.const.Handler(
                self.CreateServiceTimeSeries,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.metric_service_pb2.CreateTimeSeriesRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class MetricServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListMonitoredResourceDescriptors = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.MetricService/ListMonitoredResourceDescriptors',
            google.monitoring.v3.metric_service_pb2.ListMonitoredResourceDescriptorsRequest,
            google.monitoring.v3.metric_service_pb2.ListMonitoredResourceDescriptorsResponse,
        )
        self.GetMonitoredResourceDescriptor = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.MetricService/GetMonitoredResourceDescriptor',
            google.monitoring.v3.metric_service_pb2.GetMonitoredResourceDescriptorRequest,
            google.api.monitored_resource_pb2.MonitoredResourceDescriptor,
        )
        self.ListMetricDescriptors = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.MetricService/ListMetricDescriptors',
            google.monitoring.v3.metric_service_pb2.ListMetricDescriptorsRequest,
            google.monitoring.v3.metric_service_pb2.ListMetricDescriptorsResponse,
        )
        self.GetMetricDescriptor = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.MetricService/GetMetricDescriptor',
            google.monitoring.v3.metric_service_pb2.GetMetricDescriptorRequest,
            google.api.metric_pb2.MetricDescriptor,
        )
        self.CreateMetricDescriptor = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.MetricService/CreateMetricDescriptor',
            google.monitoring.v3.metric_service_pb2.CreateMetricDescriptorRequest,
            google.api.metric_pb2.MetricDescriptor,
        )
        self.DeleteMetricDescriptor = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.MetricService/DeleteMetricDescriptor',
            google.monitoring.v3.metric_service_pb2.DeleteMetricDescriptorRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ListTimeSeries = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.MetricService/ListTimeSeries',
            google.monitoring.v3.metric_service_pb2.ListTimeSeriesRequest,
            google.monitoring.v3.metric_service_pb2.ListTimeSeriesResponse,
        )
        self.CreateTimeSeries = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.MetricService/CreateTimeSeries',
            google.monitoring.v3.metric_service_pb2.CreateTimeSeriesRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.CreateServiceTimeSeries = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.MetricService/CreateServiceTimeSeries',
            google.monitoring.v3.metric_service_pb2.CreateTimeSeriesRequest,
            google.protobuf.empty_pb2.Empty,
        )
