import re
from typing import TYPE_CHECKING, Callable, ClassVar, Mapping, TypeAlias

from typing_extensions import Self

from viam.proto.common import ResourceName

if TYPE_CHECKING:
    from viam.components.component_base import ComponentBase

RESOURCE_NAMESPACE_RDK = "rdk"
RESOURCE_TYPE_COMPONENT = "component"
RESOURCE_TYPE_SERVICE = "service"


class Subtype:
    """Represents a known component/service (resource) API"""

    namespace: str
    """The namespace of the resource"""

    resource_type: str
    """The type of the resource, e.g. `component` or `service`"""

    resource_subtype: str
    """The subtype of the resource e.g. `servo`, `arm`, `vision`"""

    def __init__(self, namespace: str, resource_type: str, resource_subtype: str):
        self.namespace = namespace.lower()
        self.resource_type = resource_type.lower()
        self.resource_subtype = resource_subtype.lower()

    def __str__(self) -> str:
        return f"{self.namespace}:{self.resource_type}:{self.resource_subtype}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.Subtype {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: "Subtype") -> bool:
        return str(self) == str(other)

    @classmethod
    def from_resource_name(cls, resource_name: ResourceName) -> Self:
        return cls(resource_name.namespace, resource_name.type, resource_name.subtype)


class ModelFamily:
    """Represents a family of related models"""

    namespace: str
    """The namespace of the model family"""

    family: str
    """The family name"""

    DEFAULT_FAMILY_NAME: ClassVar[str] = "builtin"

    DEFAULT: ClassVar["ModelFamily"]

    def __init__(self, namespace: str, family: str):
        self.namespace = namespace.lower()
        self.family = family.lower()

    def __str__(self) -> str:
        return f"{self.namespace}:{self.family}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.ModelFamily {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: "ModelFamily") -> bool:
        return str(self) == str(other)


ModelFamily.DEFAULT = ModelFamily(RESOURCE_NAMESPACE_RDK, ModelFamily.DEFAULT_FAMILY_NAME)


class Model:
    """Represents a specific model within a family of models"""

    model_family: ModelFamily
    """The family to which this model belongs"""

    name: str
    """The name of the model"""

    def __init__(self, model_family: ModelFamily, name: str):
        self.model_family = model_family
        self.name = name.lower()

    def __str__(self) -> str:
        return f"{self.model_family}:{self.name}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.Model {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: "Model") -> bool:
        return str(self) == str(other)

    @classmethod
    def from_string(cls, model: str, *, ignore_errors=False) -> Self:
        regex = re.compile(r"^([\w-]+):([\w-]+):([\w-]+)$")
        match = regex.match(model)
        if match:
            namespace = match.group(1)
            family = match.group(2)
            name = match.group(3)
            model_family = ModelFamily(namespace, family)
        elif ignore_errors:
            model_family = ModelFamily("", "")
            name = model
        else:
            raise TypeError(f"{model} is not a valid Model")

        return cls(model_family, name)


def resource_name_from_string(string: str) -> ResourceName:
    parts = string.split(":")
    if len(parts) != 4:
        raise TypeError(f"{string} is not a valid ResourceName")
    return ResourceName(namespace=parts[0], type=parts[1], subtype=parts[2], name=parts[3])


ComponentCreator: TypeAlias = Callable[[Mapping[ResourceName, ComponentBase]], ComponentBase]
