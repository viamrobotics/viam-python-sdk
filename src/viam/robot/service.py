from typing import Any, Dict, List, Set

from grpclib.server import Stream

from viam import logging
from viam.components.movement_sensor import MovementSensor
from viam.components.sensor import Sensor
from viam.errors import ViamGRPCError
from viam.proto.common import ResourceName
from viam.proto.robot import (
    ResourceNamesRequest,
    ResourceNamesResponse,
    StopAllRequest,
    StopAllResponse,
    UnimplementedRobotServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import resource_names_for_resource, struct_to_dict

LOGGER = logging.getLogger(__name__)


class RobotService(UnimplementedRobotServiceBase, ResourceRPCServiceBase):
    def _generate_metadata(self) -> List[ResourceName]:
        md: Set[ResourceName] = set()

        for resource in self.manager.resources.values():
            # If the resource is a MovementSensor, DO NOT include Sensor as well (it will get added via MovementSensor)
            if resource.API == Sensor.API and MovementSensor.get_resource_name(resource.name) in self.manager.resources:
                continue

            md.update(resource_names_for_resource(resource))

        return list(md)

    async def ResourceNames(self, stream: Stream[ResourceNamesRequest, ResourceNamesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        metadata = self._generate_metadata()
        response = ResourceNamesResponse(resources=metadata)
        await stream.send_message(response)

    async def StopAll(self, stream: Stream[StopAllRequest, StopAllResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None

        extra: Dict[ResourceName, Dict[str, Any]] = {}
        for ex in request.extra:
            extra[ex.name] = struct_to_dict(ex.params)

        errors: List[str] = []
        for component in self.manager.resources.values():
            if callable(getattr(component, "stop", None)):
                try:
                    rn = component.get_resource_name(component.name)
                    if rn in extra:
                        try:
                            await component.stop(extra=extra[rn])  # type: ignore
                        except TypeError:
                            await component.stop()  # type: ignore
                    else:
                        await component.stop()  # type: ignore
                except Exception:
                    LOGGER.exception(f"Failed to stop component named {component.name}")
                    errors.append(component.name)

        if errors:
            raise ViamGRPCError(f'Failed to stop components named {", ".join(errors)}')
        await stream.send_message(StopAllResponse())
