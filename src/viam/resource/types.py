import re
import sys
from typing import TYPE_CHECKING, Callable, ClassVar, Mapping, Optional, Protocol, Sequence, runtime_checkable

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

from typing_extensions import Self

from viam.proto.app.robot import ComponentConfig
from viam.proto.common import GetGeometriesRequest, GetGeometriesResponse, ResourceName

if TYPE_CHECKING:
    from .base import ResourceBase

RESOURCE_NAMESPACE_RDK = "rdk"
RESOURCE_TYPE_COMPONENT = "component"
RESOURCE_TYPE_SERVICE = "service"


class Subtype:
    """Represents a known component/service (resource) API"""

    namespace: str
    """The namespace of the resource"""

    resource_type: str
    """The type of the resource, for example `component` or `service`"""

    resource_subtype: str
    """The subtype of the resource for example `servo`, `arm`, `vision`"""

    def __init__(self, namespace: str, resource_type: str, resource_subtype: str):
        self.namespace = namespace
        self.resource_type = resource_type
        self.resource_subtype = resource_subtype

    def __str__(self) -> str:
        return f"{self.namespace}:{self.resource_type}:{self.resource_subtype}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.Subtype {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Subtype):
            return str(self) == str(other)
        return False

    @classmethod
    def from_resource_name(cls, resource_name: ResourceName) -> Self:
        """Convert a ```ResourceName``` into a ```Subtype```

        Args:
            resource_name (viam.proto.common.ResourceName): The ResourceName to convert

        Returns:
            Self: A new Subtype
        """
        return cls(resource_name.namespace, resource_name.type, resource_name.subtype)

    @classmethod
    def from_string(cls, string: str) -> Self:
        """Create a ```Subtype``` from its string representation (namespace:resource_type:resource_subtype)

        Args:
            string (str): The Subtype as a string

        Raises:
            ValueError: Raised if the string does not represent a valid Subtype

        Returns:
            Self: A new Subtype
        """
        regex = re.compile(r"^([\w-]+):([\w-]+):([\w-]+)$")
        match = regex.match(string)
        if not match:
            raise ValueError(f"{string} is not a valid Subtype")
        return cls(match.group(1), match.group(2), match.group(3))


class ModelFamily:
    """Represents a family of related models"""

    namespace: str
    """The namespace of the model family"""

    family: str
    """The family name"""

    DEFAULT_FAMILY_NAME: ClassVar[str] = "builtin"

    DEFAULT: ClassVar["ModelFamily"]

    def __init__(self, namespace: str, family: str):
        self.namespace = namespace
        self.family = family

    def __str__(self) -> str:
        return f"{self.namespace}:{self.family}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.ModelFamily {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ModelFamily):
            return str(self) == str(other)
        return False


ModelFamily.DEFAULT = ModelFamily(RESOURCE_NAMESPACE_RDK, ModelFamily.DEFAULT_FAMILY_NAME)


class Model:
    """Represents a specific model within a family of models"""

    model_family: ModelFamily
    """The family to which this model belongs"""

    name: str
    """The name of the model"""

    def __init__(self, model_family: ModelFamily, name: str):
        self.model_family = model_family
        self.name = name

    def __str__(self) -> str:
        return f"{self.model_family}:{self.name}"

    def __repr__(self) -> str:
        return f"<viam.resource.types.Model {str(self)} at {hex(id(self))}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Model):
            return str(self) == str(other)
        return False

    @classmethod
    def from_string(cls, model: str, *, ignore_errors=False) -> Self:
        """Create a ```Model``` from its string representation (namespace:family:name).

        Args:
            model (str): The Model as a string
            ignore_errors (bool, optional): If namespace or family are not found in the string, default to empty string
                                            rather than raise an exception. Defaults to False.

        Raises:
            ValueError: Raised if the provided string is not a valid Model

        Returns:
            Self: The Model
        """
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
            raise ValueError(f"{model} is not a valid Model")

        return cls(model_family, name)


def resource_name_from_string(string: str) -> ResourceName:
    """Create a ResourceName from its string representation (namespace:resource_type:resource_subtype/<optional_remote:>name)

    Args:
        string (str): The ResourceName as a string

    Raises:
        ValueError: Raised if the provided string is not a valid ResourceName

    Returns:
        viam.proto.common.ResourceName: The new ResourceName
    """
    regex = re.compile(r"^([\w-]+:[\w-]+:(?:[\w-]+))\/?([\w-]+:(?:[\w-]+:)*)?(.+)?$")
    match = regex.match(string)
    if not match:
        raise ValueError(f"{string} is not a valid ResourceName")
    parts = match[1].split(":")
    if len(parts) != 3:
        raise ValueError(f"{string} is not a valid ResourceName")
    if match[2]:
        name = f"{match[2]}{match[3]}"
    else:
        name = match[3]
    return ResourceName(namespace=parts[0], type=parts[1], subtype=parts[2], name=name)


ResourceCreator: TypeAlias = Callable[[ComponentConfig, Mapping[ResourceName, "ResourceBase"]], "ResourceBase"]
Validator: TypeAlias = Callable[[ComponentConfig], Sequence[str]]


@runtime_checkable
class SupportsGetGeometries(Protocol):
    """The SupportsGetGeometries protocol defines the requirements for a resource to call get_geometries."""

    async def GetGeometries(self, request: GetGeometriesRequest, *, timeout: Optional[float] = None) -> GetGeometriesResponse:
        ...
