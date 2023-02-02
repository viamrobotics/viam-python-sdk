from typing_extensions import Self

from viam.proto.common import ResourceName

RESOURCE_NAMESPACE_RDK = "rdk"
RESOURCE_TYPE_COMPONENT = "component"
RESOURCE_TYPE_SERVICE = "service"


class Subtype:
    """Represents a known component/service (resource) API"""

    namespace: str
    """The namespace of the resource
    """

    resource_type: str
    """The type of the resource, e.g. `component` or `service`
    """

    resource_subtype: str
    """The subtype of the component e.g. `servo`, `arm`, `vision`
    """

    def __init__(self, namespace: str, resource_type: str, resource_subtype: str):
        self.namespace = namespace.lower()
        self.resource_type = resource_type.lower()
        self.resource_subtype = resource_subtype.lower()

    def __str__(self) -> str:
        return f"{self.namespace}/{self.resource_type}/{self.resource_subtype}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.Subtype {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: "Subtype") -> bool:
        return str(self) == str(other)

    @classmethod
    def from_resource_name(cls, resource_name: ResourceName) -> Self:
        return cls(resource_name.namespace, resource_name.type, resource_name.subtype)
