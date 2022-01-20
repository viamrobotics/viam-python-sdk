# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/runtimeconfig/v1beta1/runtimeconfig.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.cloud.runtimeconfig.v1beta1.resources_pb2
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.timestamp_pb2
import google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2


class RuntimeConfigManagerBase(abc.ABC):

    @abc.abstractmethod
    async def ListConfigs(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListConfigsRequest, google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListConfigsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetConfig(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.GetConfigRequest, google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig]') -> None:
        pass

    @abc.abstractmethod
    async def CreateConfig(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.CreateConfigRequest, google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateConfig(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.UpdateConfigRequest, google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteConfig(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.DeleteConfigRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ListVariables(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListVariablesRequest, google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListVariablesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetVariable(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.GetVariableRequest, google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable]') -> None:
        pass

    @abc.abstractmethod
    async def WatchVariable(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.WatchVariableRequest, google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable]') -> None:
        pass

    @abc.abstractmethod
    async def CreateVariable(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.CreateVariableRequest, google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateVariable(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.UpdateVariableRequest, google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteVariable(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.DeleteVariableRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ListWaiters(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListWaitersRequest, google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListWaitersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetWaiter(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.GetWaiterRequest, google.cloud.runtimeconfig.v1beta1.resources_pb2.Waiter]') -> None:
        pass

    @abc.abstractmethod
    async def CreateWaiter(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.CreateWaiterRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteWaiter(self, stream: 'grpclib.server.Stream[google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.DeleteWaiterRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/ListConfigs': grpclib.const.Handler(
                self.ListConfigs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListConfigsRequest,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListConfigsResponse,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/GetConfig': grpclib.const.Handler(
                self.GetConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.GetConfigRequest,
                google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/CreateConfig': grpclib.const.Handler(
                self.CreateConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.CreateConfigRequest,
                google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/UpdateConfig': grpclib.const.Handler(
                self.UpdateConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.UpdateConfigRequest,
                google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/DeleteConfig': grpclib.const.Handler(
                self.DeleteConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.DeleteConfigRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/ListVariables': grpclib.const.Handler(
                self.ListVariables,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListVariablesRequest,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListVariablesResponse,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/GetVariable': grpclib.const.Handler(
                self.GetVariable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.GetVariableRequest,
                google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/WatchVariable': grpclib.const.Handler(
                self.WatchVariable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.WatchVariableRequest,
                google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/CreateVariable': grpclib.const.Handler(
                self.CreateVariable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.CreateVariableRequest,
                google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/UpdateVariable': grpclib.const.Handler(
                self.UpdateVariable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.UpdateVariableRequest,
                google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/DeleteVariable': grpclib.const.Handler(
                self.DeleteVariable,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.DeleteVariableRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/ListWaiters': grpclib.const.Handler(
                self.ListWaiters,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListWaitersRequest,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListWaitersResponse,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/GetWaiter': grpclib.const.Handler(
                self.GetWaiter,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.GetWaiterRequest,
                google.cloud.runtimeconfig.v1beta1.resources_pb2.Waiter,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/CreateWaiter': grpclib.const.Handler(
                self.CreateWaiter,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.CreateWaiterRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/DeleteWaiter': grpclib.const.Handler(
                self.DeleteWaiter,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.DeleteWaiterRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class RuntimeConfigManagerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListConfigs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/ListConfigs',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListConfigsRequest,
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListConfigsResponse,
        )
        self.GetConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/GetConfig',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.GetConfigRequest,
            google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig,
        )
        self.CreateConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/CreateConfig',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.CreateConfigRequest,
            google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig,
        )
        self.UpdateConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/UpdateConfig',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.UpdateConfigRequest,
            google.cloud.runtimeconfig.v1beta1.resources_pb2.RuntimeConfig,
        )
        self.DeleteConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/DeleteConfig',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.DeleteConfigRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ListVariables = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/ListVariables',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListVariablesRequest,
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListVariablesResponse,
        )
        self.GetVariable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/GetVariable',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.GetVariableRequest,
            google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable,
        )
        self.WatchVariable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/WatchVariable',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.WatchVariableRequest,
            google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable,
        )
        self.CreateVariable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/CreateVariable',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.CreateVariableRequest,
            google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable,
        )
        self.UpdateVariable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/UpdateVariable',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.UpdateVariableRequest,
            google.cloud.runtimeconfig.v1beta1.resources_pb2.Variable,
        )
        self.DeleteVariable = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/DeleteVariable',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.DeleteVariableRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ListWaiters = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/ListWaiters',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListWaitersRequest,
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.ListWaitersResponse,
        )
        self.GetWaiter = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/GetWaiter',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.GetWaiterRequest,
            google.cloud.runtimeconfig.v1beta1.resources_pb2.Waiter,
        )
        self.CreateWaiter = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/CreateWaiter',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.CreateWaiterRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteWaiter = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.runtimeconfig.v1beta1.RuntimeConfigManager/DeleteWaiter',
            google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2.DeleteWaiterRequest,
            google.protobuf.empty_pb2.Empty,
        )
