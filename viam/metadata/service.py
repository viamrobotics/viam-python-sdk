from typing import List
from grpclib.server import Stream
from viam.components.base import ComponentServiceBase
from viam.proto.api.service.metadata import (
    ResourceName,
    MetadataServiceBase,
    ResourcesRequest, ResourcesResponse
)


class MetadataService(MetadataServiceBase, ComponentServiceBase):

    def _generate_metadata(self) -> List[ResourceName]:
        md: List[ResourceName] = []

        for component in self.manager.components.values():
            for klass in component.__class__.mro():
                class_name = str(klass)
                if 'viam.components' not in class_name:
                    continue
                if 'ComponentBase' in class_name:
                    continue
                component_type = class_name \
                    .split('viam.components.')[1] \
                    .split('.')[0]

                r_name = ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype=component_type,
                    name=component.name
                )
                md.append(r_name)

        return md

    async def Resources(
        self,
        stream: Stream[ResourcesRequest, ResourcesResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        metadata = self._generate_metadata()
        response = ResourcesResponse(resources=metadata)
        await stream.send_message(response)
