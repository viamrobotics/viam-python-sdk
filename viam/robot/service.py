import asyncio
from typing import Dict
from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.proto.api.robot import (
    RobotServiceBase,
    Status,
    MotorStatus, ServoStatus,
    StatusRequest, StatusResponse,
    StatusStreamRequest, StatusStreamResponse,
    ConfigRequest, ConfigResponse,
    DoActionRequest, DoActionResponse,
    ExecuteFunctionRequest, ExecuteFunctionResponse,
    ExecuteSourceRequest, ExecuteSourceResponse,
    ResourceRunCommandRequest, ResourceRunCommandResponse,
    NavigationServiceModeRequest, NavigationServiceModeResponse,
    NavigationServiceSetModeRequest, NavigationServiceSetModeResponse,
    NavigationServiceLocationRequest, NavigationServiceLocationResponse,
    NavigationServiceWaypointsRequest, NavigationServiceWaypointsResponse,
    NavigationServiceAddWaypointRequest, NavigationServiceAddWaypointResponse,
    NavigationServiceRemoveWaypointRequest,
    NavigationServiceRemoveWaypointResponse,
)

# Import all components
from viam.components.motor import MotorBase
from viam.components.servo import ServoBase


class RobotService(RobotServiceBase, ComponentServiceBase):

    async def _generate_status(self) -> Status:
        motor_statuses: Dict[str, MotorStatus] = {}
        servo_statuses: Dict[str, ServoStatus] = {}

        for component in self.manager.components.values():
            if isinstance(component, MotorBase):
                s = MotorStatus()
                s.on = await component.is_powered()
                s.position = await component.get_position()
                features = await component.get_features()
                s.position_supported = features['position_reporting']
                motor_statuses[component.name] = s
            if isinstance(component, ServoBase):
                s = ServoStatus()
                s.angle = await component.get_position()
                servo_statuses[component.name] = s

        return Status(
            motors=motor_statuses,
            servos=servo_statuses,
        )

    async def Status(
        self,
        stream: Stream[StatusRequest, StatusResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        status = await self._generate_status()
        response = StatusResponse(status=status)
        await stream.send_message(response)

    async def StatusStream(
        self,
        stream: Stream[StatusStreamRequest, StatusStreamResponse]
    ) -> None:
        request = stream.recv_message()
        assert request is not None
        interval = 1  # seconds
        while True:
            status = await self._generate_status()
            response = StatusStreamResponse(status=status)
            await stream.send_message(response)
            await asyncio.sleep(interval)

    async def Config(
        self,
        stream: Stream[ConfigRequest, ConfigResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = ConfigResponse()
        await stream.send_message(response)

    async def DoAction(
        self,
        stream: Stream[DoActionRequest, DoActionResponse]
    ) -> None:
        pass

    async def ExecuteFunction(
        self,
        stream: Stream[ExecuteFunctionRequest, ExecuteFunctionResponse]
    ) -> None:
        pass

    async def ExecuteSource(
        self,
        stream: Stream[ExecuteSourceRequest, ExecuteSourceResponse]
    ) -> None:
        pass

    async def ResourceRunCommand(
        self,
        stream: Stream[ResourceRunCommandRequest, ResourceRunCommandResponse]
    ) -> None:
        pass

    async def NavigationServiceMode(
        self,
        stream: Stream[NavigationServiceModeRequest,
                       NavigationServiceModeResponse]
    ) -> None:
        pass

    async def NavigationServiceSetMode(
        self,
        stream: Stream[NavigationServiceSetModeRequest,
                       NavigationServiceSetModeResponse]
    ) -> None:
        pass

    async def NavigationServiceLocation(
        self,
        stream: Stream[NavigationServiceLocationRequest,
                       NavigationServiceLocationResponse]
    ) -> None:
        pass

    async def NavigationServiceWaypoints(
        self,
        stream: Stream[NavigationServiceWaypointsRequest,
                       NavigationServiceWaypointsResponse]
    ) -> None:
        pass

    async def NavigationServiceAddWaypoint(
        self,
        stream: Stream[NavigationServiceAddWaypointRequest,
                       NavigationServiceAddWaypointResponse]
    ) -> None:
        pass

    async def NavigationServiceRemoveWaypoint(
        self,
        stream: Stream[NavigationServiceRemoveWaypointRequest,
                       NavigationServiceRemoveWaypointResponse]
    ) -> None:
        pass
