"""
Helpers for the ``KinematicModel`` message that arms, gantries and grippers serve from ``get_kinematic_model``.

A module usually keeps its kinematics in a kinematic model file, which is the proto JSON of the message, reads it once with
``read_kinematic_model_file``, narrows it to its resource config with ``narrow_joint_limits`` and returns the result::

    from viam.kinematics import narrow_joint_limits, read_kinematic_model_file

    model = read_kinematic_model_file("my_arm.json")
    model = narrow_joint_limits(model, {"shoulder": {"min": -90, "max": 90}})

Lengths in the message are millimeters and angles are degrees.
"""

import base64
import json
import math
import ntpath
import os
import posixpath
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

from google.protobuf import json_format
from google.protobuf.message import Message

from viam.errors import MethodNotImplementedError, NotSupportedError
from viam.proto.common import (
    Geometry,
    GetKinematicsRequest,
    GetKinematicsResponse,
    JointType,
    KinematicModel,
    KinematicsFileFormat,
    Mesh,
)
from viam.utils import struct_to_dict

__all__ = [
    "narrow_joint_limits",
    "read_kinematic_model_file",
]

_WORLD = "world"

_LIMIT_FIELDS = ("min", "max", "max_velocity", "max_acceleration")


def read_kinematic_model_file(path: Union[str, "os.PathLike[str]"]) -> KinematicModel:
    """
    Read a kinematic model file into the message it encodes.

    ::

        from viam.kinematics import read_kinematic_model_file

        model = read_kinematic_model_file("my_arm.json")
        for joint in model.joints:
            print(joint.id, joint.limits.min, joint.limits.max)

    A mesh that names a path and carries no bytes is read from that path, relative to the model file, and comes back with its bytes,
    its path as written and its content type taken from the extension. A mesh that already carries bytes is left alone.

    Args:
        path (Union[str, os.PathLike[str]]): The kinematic model file.

    Raises:
        OSError: If the model file cannot be read.
        ValueError: If the file is not a valid model. The read is strict, so an unknown field, a number that is not finite, a parent
            that is not in the model, a cycle, a mimic of something that is not a joint and a mesh that cannot be read all fail it.

    Returns:
        KinematicModel: The model, with every mesh inline.
    """
    path = os.fspath(path)
    with open(path, "rb") as f:
        data = f.read()
    try:
        return _parse_kinematic_model(data, os.path.dirname(path))
    except ValueError as e:
        raise ValueError(f"kinematic model file {path}: {e}") from e


def _parse_kinematic_model(data: Union[bytes, str], mesh_dir: str) -> KinematicModel:
    try:
        doc = json.loads(data, object_pairs_hook=_unique_keys, parse_constant=_reject_constant, parse_float=_parse_float)
    except OverflowError as e:
        raise ValueError(str(e)) from e
    except ValueError as e:
        raise ValueError(f"malformed JSON: {e}") from e
    if not isinstance(doc, dict):
        raise ValueError("malformed JSON: a kinematic model is a JSON object")
    model = KinematicModel()
    try:
        json_format.ParseDict(doc, model)
    except json_format.ParseError as e:
        raise ValueError(str(e)) from e
    _reject_non_finite(model, "")
    _validate(model)
    _load_meshes(model, mesh_dir)
    return model


def _unique_keys(pairs: List[Tuple[str, Any]]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate key {key!r}")
        out[key] = value
    return out


def _reject_constant(token: str) -> float:
    # the json module reads a bare NaN or Infinity, which is not JSON and which the other SDKs refuse
    raise ValueError(f"{token} is not a JSON value")


def _parse_float(token: str) -> float:
    # a literal too large for a double reads as infinity, which a file is not allowed to say any other way either
    value = float(token)
    if math.isinf(value):
        raise OverflowError(f"{token} is infinite, leave a bound out to make it unbounded")
    return value


def _reject_non_finite(msg: Message, prefix: str) -> None:
    # proto JSON reads the strings "Infinity", "-Infinity" and "NaN" into a double, and a file has to leave a bound out to say unbounded
    for fd, value in msg.ListFields():
        name = prefix + fd.name
        if fd.message_type is not None and fd.message_type.GetOptions().map_entry:
            items = [(f"{name}[{k}]", v) for k, v in value.items()]
        elif isinstance(value, (Message, float, int, str, bytes)):
            items = [(name, value)]
        else:
            items = [(f"{name}[{i}]", v) for i, v in enumerate(value)]
        for item_name, item in items:
            if isinstance(item, Message):
                _reject_non_finite(item, item_name + ".")
            elif isinstance(item, float) and not math.isfinite(item):
                what = "not a number" if math.isnan(item) else "infinite"
                raise ValueError(f"{item_name} is {what}, leave a bound out to make it unbounded")


def _validate(model: KinematicModel) -> None:
    nodes = [("link", link.id, link.parent) for link in model.links]
    nodes += [("joint", joint.id, joint.parent) for joint in model.joints]
    if not nodes:
        raise ValueError("model has no links or joints")
    kinds: Dict[str, str] = {}
    parents: Dict[str, str] = {}
    for kind, id, parent in nodes:
        if id == "":
            raise ValueError(f"a {kind} has no id")
        if id == _WORLD:
            raise ValueError(f'a {kind} cannot use the reserved id "{_WORLD}"')
        other = kinds.get(id)
        if other == kind:
            raise ValueError(f'{kind} "{id}" is defined twice')
        if other is not None:
            raise ValueError(f'"{id}" names both a {other} and a {kind}')
        kinds[id] = kind
        parents[id] = parent
    # a reader that builds frames treats a parent it does not know as the world, so a misspelled parent has to be caught here or the
    # link quietly moves to the root
    for kind, id, parent in nodes:
        if parent not in ("", _WORLD) and parent not in kinds:
            raise ValueError(f'{kind} "{id}": parent "{parent}" is not a link or joint in the model')
    for _, id, _ in nodes:
        seen = set()
        cur = id
        while cur not in ("", _WORLD):
            if cur in seen:
                raise ValueError(f'{kinds[cur]} "{cur}" is its own ancestor')
            seen.add(cur)
            cur = parents[cur]
    for joint in model.joints:
        if not joint.HasField("mimic"):
            continue
        if joint.mimic.joint == joint.id:
            raise ValueError(f'joint "{joint.id}" mimics itself')
        if kinds.get(joint.mimic.joint) != "joint":
            raise ValueError(f'joint "{joint.id}" mimics "{joint.mimic.joint}", which is not a joint in the model')
        if any(joint.limits.HasField(field) for field in _LIMIT_FIELDS):
            raise ValueError(f'joint "{joint.id}" is a mimic joint and cannot carry limits, it takes them from the joint it mimics')


def _mesh_of(geometry: Geometry) -> Optional[Mesh]:
    return geometry.mesh if geometry.WhichOneof("geometry_type") == "mesh" else None


def _load_meshes(model: KinematicModel, mesh_dir: str) -> None:
    # a file is read once, however many links name it
    cache: Dict[str, bytes] = {}
    for link in model.links:
        for role, geometries in (("collision", link.collision), ("visual", link.visual)):
            for i, geometry in enumerate(geometries):
                try:
                    _load_mesh(_mesh_of(geometry), role == "collision", mesh_dir, cache)
                except ValueError as e:
                    raise ValueError(f'link "{link.id}" {role} geometry {i}: {e}') from e
    for joint in model.joints:
        if not joint.HasField("geometry"):
            continue
        try:
            _load_mesh(_mesh_of(joint.geometry), True, mesh_dir, cache)
        except ValueError as e:
            raise ValueError(f'joint "{joint.id}" geometry: {e}') from e


def _extension(source: str) -> str:
    base = source.rsplit("/", 1)[-1]
    return base.rsplit(".", 1)[1].lower() if "." in base else ""


def _load_mesh(mesh: Optional[Mesh], collision: bool, mesh_dir: str, cache: Dict[str, bytes]) -> None:
    if mesh is None:
        return
    source = mesh.original_file_source_path_diagnostic
    has_bytes = len(mesh.mesh) > 0
    if not has_bytes and source == "":
        raise ValueError("mesh has neither bytes nor a source path")
    content_type = mesh.content_type.lower()
    if content_type == "model/gltf-binary":
        # the MIME spelling a viewer sends, which the message documents as glb
        content_type = "glb"
    ext = _extension(source)
    if not has_bytes:
        # the path has to survive a module install and a trip over the wire, so it is relative, uses forward slashes and is not a URI
        if "://" in source:
            raise ValueError(f'mesh path "{source}" is a URI, paths are relative to the model file')
        if "\\" in source:
            raise ValueError(f'mesh path "{source}" uses backslashes, use forward slashes')
        if posixpath.isabs(source) or ntpath.isabs(source):
            raise ValueError(f'mesh path "{source}" is absolute, paths are relative to the model file')
        if ext == "":
            raise ValueError(f'mesh path "{source}" has no extension to take the content type from')
        if content_type not in ("", ext):
            raise ValueError(f'mesh content type "{mesh.content_type}" disagrees with the extension of "{source}"')
        content_type = ext
    elif content_type == "":
        # a mesh that carries its bytes keeps whatever path it was written out with, which can still name the content type
        content_type = ext
    if content_type == "":
        raise ValueError("inline mesh bytes need a content type")
    # a collision mesh gets parsed by whoever plans with the model, a visual mesh never does, so only the first is held to a format
    if collision and content_type not in ("stl", "ply"):
        raise ValueError(f'collision mesh content type "{content_type}" is not stl or ply')
    mesh.content_type = content_type
    if has_bytes:
        return
    if source not in cache:
        resolved = os.path.normpath(os.path.join(mesh_dir, source))
        try:
            with open(resolved, "rb") as f:
                cache[source] = f.read()
        except OSError as e:
            raise ValueError(f'failed to read mesh "{source}" at {resolved}: {e}') from e
    mesh.mesh = cache[source]


def narrow_joint_limits(model: KinematicModel, limits: Mapping[str, Mapping[str, float]]) -> KinematicModel:
    """
    Narrow the joint limits of a model to what a resource's configuration asks of each joint.

    The argument is keyed by joint id and takes the attribute shape a module is expected to accept, in the units of the message:
    degrees, degrees per second and degrees per second squared for a revolute joint, millimeters for a prismatic one. A key left out
    leaves that limit as it is::

        from viam.kinematics import narrow_joint_limits
        from viam.utils import struct_to_dict

        attributes = struct_to_dict(config.attributes)
        # "joint_limits": {"joint_2": {"min": -31, "max": -29}, "joint_3": {"max_velocity": 30}}
        model = narrow_joint_limits(model, attributes.get("joint_limits", {}))

    Position, velocity and acceleration are checked on their own. A joint the model has no bound for accepts any value, and a min
    equal to max locks a joint where it stands.

    Args:
        model (KinematicModel): The model to narrow. It is not modified.
        limits (Mapping[str, Mapping[str, float]]): For each joint id, any of ``min``, ``max``, ``max_velocity`` and
            ``max_acceleration``.

    Raises:
        ValueError: If a value would widen a limit the model already holds, since a widened limit is the one that reaches hardware,
            and also if a joint is not in the model, a joint is a mimic joint, a value is not a finite number, a speed is negative
            or a min ends up above its max. The error names the joint.

    Returns:
        KinematicModel: A copy of the model with the narrowed limits.
    """
    out = KinematicModel()
    out.CopyFrom(model)
    joints = {joint.id: joint for joint in out.joints}
    # ids in order, so the joint an error names does not change from one run to the next
    for id in sorted(limits):
        request = limits[id]
        if not isinstance(request, Mapping):
            raise ValueError(f'joint "{id}": limits have to be a mapping, got {type(request).__name__}')
        for field, value in request.items():
            if field not in _LIMIT_FIELDS:
                raise ValueError(f'joint "{id}": unknown limit "{field}", expected one of {", ".join(_LIMIT_FIELDS)}')
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError(f'joint "{id}": {field} must be a finite number, got {value!r}')
        for field in ("max_velocity", "max_acceleration"):
            if request.get(field, 0) < 0:
                raise ValueError(f'joint "{id}": {field} cannot be negative, got {request[field]}')
        joint = joints.get(id)
        if joint is None:
            raise ValueError(f'no joint "{id}" in model "{model.name}"')
        if joint.HasField("mimic"):
            raise ValueError(f'joint "{id}" is a mimic joint and cannot carry limits, it takes them from the joint it mimics')

        # a bound that has been through radians and back no longer lands on the degrees it started from, so we accept a value up to
        # the bound as the error prints it as well as the bound itself. That way neither a value copied out of a message nor the
        # model's own limit handed back is refused.
        for field in _LIMIT_FIELDS:
            if field not in request or not joint.limits.HasField(field):
                continue
            value = request[field]
            exact = getattr(joint.limits, field)
            bound = round(exact, 6)
            if field == "min" and value < min(exact, bound):
                raise ValueError(f'joint "{id}": min {value} is below the model\'s min {bound}')
            if field != "min" and value > max(exact, bound):
                raise ValueError(f'joint "{id}": {field} {value} is above the model\'s {field} {bound}')
        for field, value in request.items():
            setattr(joint.limits, field, value)
        if joint.limits.HasField("min") and joint.limits.HasField("max") and joint.limits.min > joint.limits.max:
            raise ValueError(f'joint "{id}": min {joint.limits.min} is above max {joint.limits.max}')
        # a continuous joint is a revolute joint with neither bound, so it stops being one as soon as it has either
        if joint.type == JointType.JOINT_TYPE_CONTINUOUS and (joint.limits.HasField("min") or joint.limits.HasField("max")):
            joint.type = JointType.JOINT_TYPE_REVOLUTE
    return out


class _NotWritable(Exception):
    pass


def _sva_file(model: KinematicModel) -> Optional[bytes]:
    """
    Write the model as the SVA JSON file a client that predates the message reads from the deprecated bytes fields. Visual geometry
    is left out, since that file never had a place for it. Returns None for a model the file cannot describe, which is a joint with
    no position bound, a collision mesh without its bytes, a point cloud geometry or a joint with no type.
    """
    try:
        doc: Dict[str, Any] = {"name": model.name, "kinematic_param_type": "SVA"}
        doc["links"] = [_sva_link(link) for link in model.links]
        doc["joints"] = [_sva_joint(joint) for joint in model.joints]
        if model.output_frames:
            doc["output_frames"] = list(model.output_frames)
        return json.dumps(doc, allow_nan=False).encode()
    except (_NotWritable, ValueError):
        return None


def _sva_vector(v) -> Dict[str, float]:
    return {"x": v.x, "y": v.y, "z": v.z}


def _sva_link(link) -> Dict[str, Any]:
    out: Dict[str, Any] = {"id": link.id, "translation": _sva_vector(link.pose.translation)}
    if link.parent:
        out["parent"] = link.parent
    # the file keeps whichever representation the model has and takes degrees only for an orientation vector
    which = link.pose.WhichOneof("orientation")
    if which == "quaternion":
        q = link.pose.quaternion
        out["orientation"] = {"type": "quaternion", "value": {"W": q.w, "X": q.x, "Y": q.y, "Z": q.z}}
    elif which == "orientation_vector":
        ov = link.pose.orientation_vector
        out["orientation"] = {"type": "ov_degrees", "value": {"th": ov.theta, "x": ov.o_x, "y": ov.o_y, "z": ov.o_z}}
    elif which == "euler_angles":
        e = link.pose.euler_angles
        value = {"roll": math.radians(e.roll), "pitch": math.radians(e.pitch), "yaw": math.radians(e.yaw)}
        out["orientation"] = {"type": "euler_angles", "value": value}
    elif which == "axis_angles":
        aa = link.pose.axis_angles
        out["orientation"] = {"type": "axis_angles", "value": {"th": math.radians(aa.theta), "x": aa.rx, "y": aa.ry, "z": aa.rz}}
    geometries = [_sva_geometry(g) for g in link.collision]
    # the first geometry stays under the key a reader that knows only one geometry per link looks at
    if geometries:
        out["geometry"] = geometries[0]
    if len(geometries) > 1:
        out["geometries"] = geometries[1:]
    return out


def _sva_joint(joint) -> Dict[str, Any]:
    if joint.type in (JointType.JOINT_TYPE_REVOLUTE, JointType.JOINT_TYPE_CONTINUOUS):
        joint_type = "revolute"
    elif joint.type == JointType.JOINT_TYPE_PRISMATIC:
        joint_type = "prismatic"
    else:
        raise _NotWritable()
    out: Dict[str, Any] = {"id": joint.id, "type": joint_type, "parent": joint.parent, "axis": _sva_vector(joint.axis)}
    if joint.HasField("mimic"):
        out["mimic"] = {"joint": joint.mimic.joint, "multiplier": joint.mimic.multiplier, "offset": joint.mimic.offset}
    else:
        # JSON has no infinity, so a joint with a bound left out cannot be written
        if not (joint.limits.HasField("min") and joint.limits.HasField("max")):
            raise _NotWritable()
        out["min"] = joint.limits.min
        out["max"] = joint.limits.max
        for field in ("max_velocity", "max_acceleration"):
            if joint.limits.HasField(field):
                out[field] = getattr(joint.limits, field)
    if joint.HasField("geometry"):
        out["geometry"] = _sva_geometry(joint.geometry)
    return out


def _sva_geometry(geometry: Geometry) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    which = geometry.WhichOneof("geometry_type")
    if which == "box":
        out.update(type="box", **_sva_vector(geometry.box.dims_mm))
    elif which == "sphere":
        out.update(type="sphere", r=geometry.sphere.radius_mm)
    elif which == "capsule":
        out.update(type="capsule", r=geometry.capsule.radius_mm, l=geometry.capsule.length_mm)
    elif which == "mesh" and geometry.mesh.mesh:
        out.update(type="mesh", mesh_data=base64.b64encode(geometry.mesh.mesh).decode(), mesh_content_type=geometry.mesh.content_type)
        if geometry.mesh.original_file_source_path_diagnostic:
            out["mesh_file_path"] = geometry.mesh.original_file_source_path_diagnostic
    else:
        raise _NotWritable()
    center = geometry.center
    out["translation"] = _sva_vector(center)
    # an unset orientation and the identity both read as no orientation
    if not (center.o_x == 0 and center.o_y == 0 and center.o_z >= 0 and center.theta == 0):
        out["orientation"] = {"type": "ov_degrees", "value": {"th": center.theta, "x": center.o_x, "y": center.o_y, "z": center.o_z}}
    if geometry.label:
        out["label"] = geometry.label
    return out


def _drop_mesh_bytes(geometries) -> None:
    for geometry in geometries:
        if geometry.WhichOneof("geometry_type") == "mesh":
            geometry.mesh.ClearField("mesh")


async def kinematics_response(resource, request: GetKinematicsRequest, **kwargs) -> GetKinematicsResponse:
    """
    Build the GetKinematics reply for an arm, gantry or gripper, which is shared by their three servers.

    A request that asks for either mesh role comes from a client that reads the typed model, so its reply carries the model alone,
    with bytes only for the roles asked for and every other mesh reduced to its path and content type. A request with no flags may
    come from a client that predates them, so it gets the deprecated file fields beside the model, with every mesh whole. The file
    is what the resource returns from get_kinematics when it still implements it, and otherwise it is written from the model.
    """
    collision, visual = request.include_collision_meshes, request.include_visual_meshes
    extra = struct_to_dict(request.extra)
    model: Optional[KinematicModel] = None
    try:
        served = await resource.get_kinematic_model(
            include_collision_meshes=collision or not visual,
            include_visual_meshes=visual or not collision,
            extra=extra,
            **kwargs,
        )
    except (MethodNotImplementedError, NotSupportedError):
        # a resource that forwards to an arm on a machine that predates the model has none to give, and still has the file
        pass
    else:
        # we work on a copy, since a resource is free to hand out the one model it holds, and name it for the resource, since that is
        # what every client addresses it by
        model = KinematicModel()
        model.CopyFrom(served)
        model.name = request.name

    if model is not None and (collision or visual):
        for link in model.links:
            if not collision:
                _drop_mesh_bytes(link.collision)
            if not visual:
                _drop_mesh_bytes(link.visual)
        if not collision:
            _drop_mesh_bytes(joint.geometry for joint in model.joints)
        return GetKinematicsResponse(model=model)

    format, data, meshes = KinematicsFileFormat.KINEMATICS_FILE_FORMAT_UNSPECIFIED, b"", {}
    try:
        kinematics = await resource.get_kinematics(
            include_collision_meshes=collision,
            include_visual_meshes=visual,
            extra=extra,
            **kwargs,
        )
    except (MethodNotImplementedError, NotSupportedError):
        if model is None:
            raise
        file = _sva_file(model)
        if file is not None:
            format, data = KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, file
    else:
        format, data = kinematics[0], kinematics[1]
        if len(kinematics) > 2:
            meshes = kinematics[2]
        if model is None and len(kinematics) > 3:
            model = kinematics[3]
    return GetKinematicsResponse(format=format, kinematics_data=data, meshes_by_urdf_filepath=meshes, model=model)
