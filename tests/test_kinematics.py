import base64
import json
import math
import os
from typing import Any, Dict

import pytest
from google.protobuf import json_format
from grpclib import GRPCError
from grpclib.testing import ChannelFor

from viam.components import KinematicsReturn
from viam.components.arm import Arm, ArmClient, ArmRPCService
from viam.components.gantry import GantryClient, GantryRPCService
from viam.components.gripper import GripperClient, GripperRPCService
from viam.errors import MethodNotImplementedError, NotSupportedError
from viam.kinematics import _sva_file, narrow_joint_limits, read_kinematic_model_file
from viam.proto.common import (
    Geometry,
    GetKinematicsRequest,
    GetKinematicsResponse,
    JointLimits,
    JointType,
    KinematicJoint,
    KinematicLink,
    KinematicModel,
    KinematicsFileFormat,
    LinkPose,
    Mesh,
    MimicJoint,
    Orientation,
    Pose,
    RectangularPrism,
    Sphere,
    Vector3,
)
from viam.proto.component.arm import ArmServiceStub
from viam.resource.manager import ResourceManager

from .mocks.components import MockArm, MockGantry, MockGripper

# A pinned copy of referenceframe/testfiles/kinematic_models in rdk, taken at cefbb7080. The README in it is the contract, and the
# Go, C++ and Python loaders are all held to the same files, so refresh the whole directory from rdk rather than editing a case here.
FIXTURES = os.path.join(os.path.dirname(__file__), "data", "kinematic_models")

# What our loader says for each error kind the fixtures name. The kinds are listed in the fixture README, the wording is our own.
ERROR_KINDS = {
    "unknown_field": "no field named",
    "infinite": "is infinite",
    "nan": "is not a number",
    "malformed_json": "malformed JSON",
    "empty_model": "no links or joints",
    "missing_id": "has no id",
    "reserved_id": "reserved id",
    "shared_id": "names both a link and a joint",
    "duplicate_id": "is defined twice",
    "missing_parent": "is not a link or joint",
    "cycle": "its own ancestor",
    "mimic_self": "mimics itself",
    "mimic_not_joint": "which is not a joint",
    "mimic_with_limits": "cannot carry limits",
    "mesh_missing": "failed to read mesh",
    "mesh_path_absolute": "is absolute",
    "mesh_path_uri": "is a URI",
    "mesh_path_backslash": "uses backslashes",
    "content_type_mismatch": "disagrees",
    "collision_format": "is not stl or ply",
    "mesh_no_extension": "has no extension",
    "inline_without_type": "need a content type",
    "mesh_empty": "neither bytes nor a source path",
}

CASES = sorted(entry for entry in os.listdir(FIXTURES) if os.path.isdir(os.path.join(FIXTURES, entry)))


def expected_model(case: str) -> KinematicModel:
    with open(os.path.join(FIXTURES, case, "expected.json")) as f:
        return json_format.Parse(f.read(), KinematicModel())


class TestFixtures:
    def test_all_cases_present(self):
        assert len(CASES) == 32

    @pytest.mark.parametrize("case", CASES)
    def test_case(self, case: str):
        model_path = os.path.join(FIXTURES, case, "model.json")
        error_path = os.path.join(FIXTURES, case, "error.json")
        if os.path.exists(error_path):
            with open(error_path) as f:
                want = json.load(f)
            with pytest.raises(ValueError) as raised:
                read_kinematic_model_file(model_path)
            message = str(raised.value)
            assert ERROR_KINDS[want["kind"]] in message
            for mention in want["mentions"]:
                assert mention in message
            return
        assert read_kinematic_model_file(model_path) == expected_model(case)

    def test_missing_file(self):
        with pytest.raises(OSError):
            read_kinematic_model_file(os.path.join(FIXTURES, "nothing_here.json"))

    def test_bare_constants_are_not_json(self, tmp_path):
        path = tmp_path / "model.json"
        path.write_text('{"links": [{"id": "a"}], "joints": [{"id": "j", "limits": {"min": NaN}}]}')
        with pytest.raises(ValueError, match="malformed JSON"):
            read_kinematic_model_file(path)

    def test_literal_too_large_for_a_double(self, tmp_path):
        path = tmp_path / "model.json"
        path.write_text('{"links": [{"id": "a"}], "joints": [{"id": "j", "limits": {"max": 1e999}}]}')
        with pytest.raises(ValueError, match="is infinite"):
            read_kinematic_model_file(path)

    def test_duplicate_key(self, tmp_path):
        path = tmp_path / "model.json"
        path.write_text('{"name": "a", "name": "b", "links": [{"id": "a"}]}')
        with pytest.raises(ValueError, match="duplicate key"):
            read_kinematic_model_file(path)


def planar_arm() -> KinematicModel:
    return KinematicModel(
        name="planar",
        links=[
            KinematicLink(id="base", parent="world"),
            KinematicLink(id="upper", parent="shoulder", pose=LinkPose(translation=Vector3(x=100))),
        ],
        joints=[
            KinematicJoint(
                id="shoulder",
                parent="base",
                type=JointType.JOINT_TYPE_REVOLUTE,
                axis=Vector3(z=1),
                limits=JointLimits(min=-180, max=180, max_velocity=90),
            ),
            KinematicJoint(id="wrist", parent="upper", type=JointType.JOINT_TYPE_CONTINUOUS, axis=Vector3(z=1)),
            KinematicJoint(
                id="follower",
                parent="wrist",
                type=JointType.JOINT_TYPE_REVOLUTE,
                axis=Vector3(z=1),
                mimic=MimicJoint(joint="wrist", multiplier=-1),
            ),
        ],
    )


class TestNarrowJointLimits:
    def test_narrows_and_leaves_the_input_alone(self):
        model = planar_arm()
        out = narrow_joint_limits(model, {"shoulder": {"min": -90, "max_velocity": 30, "max_acceleration": 400}})
        assert model == planar_arm()
        shoulder = out.joints[0].limits
        assert (shoulder.min, shoulder.max, shoulder.max_velocity, shoulder.max_acceleration) == (-90, 180, 30, 400)
        assert out.joints[1] == model.joints[1]

    def test_empty_request_changes_nothing(self):
        assert narrow_joint_limits(planar_arm(), {}) == planar_arm()
        assert narrow_joint_limits(planar_arm(), {"shoulder": {}}) == planar_arm()

    def test_lock_in_place(self):
        out = narrow_joint_limits(planar_arm(), {"shoulder": {"min": 10, "max": 10}})
        assert (out.joints[0].limits.min, out.joints[0].limits.max) == (10, 10)

    def test_bounding_a_continuous_joint_makes_it_revolute(self):
        out = narrow_joint_limits(planar_arm(), {"wrist": {"max_velocity": 10}})
        assert out.joints[1].type == JointType.JOINT_TYPE_CONTINUOUS
        out = narrow_joint_limits(planar_arm(), {"wrist": {"min": -720}})
        assert out.joints[1].type == JointType.JOINT_TYPE_REVOLUTE
        assert out.joints[1].limits.min == -720
        assert not out.joints[1].limits.HasField("max")

    def test_bound_that_went_through_radians(self):
        model = planar_arm()
        model.joints[0].limits.max = math.degrees(math.radians(180)) + 1e-9
        out = narrow_joint_limits(model, {"shoulder": {"max": 180}})
        assert out.joints[0].limits.max == 180

    @pytest.mark.parametrize("field,value", [("min", -math.degrees(2.0)), ("max", math.degrees(2.0)), ("max_velocity", math.degrees(1.1))])
    def test_the_models_own_limit_is_not_a_widening(self, field: str, value: float):
        model = planar_arm()
        setattr(model.joints[0].limits, field, value)
        assert narrow_joint_limits(model, {"shoulder": {field: value}}) == model
        assert narrow_joint_limits(model, {"shoulder": {field: round(value, 6)}}).joints[0].limits.HasField(field)

    @pytest.mark.parametrize(
        "limits,says",
        [
            ({"shoulder": {"min": -181}}, 'joint "shoulder": min -181 is below'),
            ({"shoulder": {"max": 180.5}}, 'joint "shoulder": max 180.5 is above'),
            ({"shoulder": {"max_velocity": 91}}, 'joint "shoulder": max_velocity 91 is above'),
            ({"shoulder": {"min": 10, "max": 5}}, 'joint "shoulder": min 10.0 is above max 5.0'),
            ({"shoulder": {"max_velocity": -1}}, "cannot be negative"),
            ({"shoulder": {"max": float("inf")}}, "must be a finite number"),
            ({"shoulder": {"max": float("nan")}}, "must be a finite number"),
            ({"shoulder": {"max": "10"}}, "must be a finite number"),
            ({"shoulder": {"maximum": 10}}, 'unknown limit "maximum"'),
            ({"shoulder": 10}, "have to be a mapping"),
            ({"elbow": {"max": 10}}, 'no joint "elbow" in model "planar"'),
            ({"base": {"max": 10}}, 'no joint "base"'),
            ({"follower": {"max": 10}}, "mimic joint"),
            # ids are taken in order, so the first bad joint is the one named
            ({"shoulder": {"min": -181}, "elbow": {"max": 10}}, "elbow"),
        ],
    )
    def test_refused(self, limits: Dict[str, Any], says: str):
        model = planar_arm()
        with pytest.raises(ValueError) as raised:
            narrow_joint_limits(model, limits)
        assert says in str(raised.value)
        assert model == planar_arm()


class TestSVAFile:
    def test_document(self):
        model = planar_arm()
        model.joints[1].limits.min = -360
        model.joints[1].limits.max = 360
        model.output_frames.append("upper")
        model.links[0].collision.append(Geometry(center=Pose(z=5, o_z=1), box=RectangularPrism(dims_mm=Vector3(x=1, y=2, z=3)), label="b"))
        model.links[0].collision.append(Geometry(center=Pose(o_x=1, theta=90), sphere=Sphere(radius_mm=4)))
        model.links[0].visual.append(Geometry(mesh=Mesh(content_type="glb", mesh=b"glb")))
        model.links[1].pose.orientation_vector.CopyFrom(Orientation(o_z=1, theta=45))
        model.links[1].collision.append(
            Geometry(mesh=Mesh(content_type="ply", mesh=b"ply", original_file_source_path_diagnostic="a/b.ply"))
        )
        file = _sva_file(model)
        assert file is not None
        assert json.loads(file) == {
            "name": "planar",
            "kinematic_param_type": "SVA",
            "output_frames": ["upper"],
            "links": [
                {
                    "id": "base",
                    "parent": "world",
                    "translation": {"x": 0, "y": 0, "z": 0},
                    "geometry": {"type": "box", "x": 1, "y": 2, "z": 3, "translation": {"x": 0, "y": 0, "z": 5}, "label": "b"},
                    "geometries": [
                        {
                            "type": "sphere",
                            "r": 4,
                            "translation": {"x": 0, "y": 0, "z": 0},
                            "orientation": {"type": "ov_degrees", "value": {"th": 90, "x": 1, "y": 0, "z": 0}},
                        }
                    ],
                },
                {
                    "id": "upper",
                    "parent": "shoulder",
                    "translation": {"x": 100, "y": 0, "z": 0},
                    "orientation": {"type": "ov_degrees", "value": {"th": 45, "x": 0, "y": 0, "z": 1}},
                    "geometry": {
                        "type": "mesh",
                        "mesh_data": base64.b64encode(b"ply").decode(),
                        "mesh_content_type": "ply",
                        "mesh_file_path": "a/b.ply",
                        "translation": {"x": 0, "y": 0, "z": 0},
                    },
                },
            ],
            "joints": [
                {
                    "id": "shoulder",
                    "type": "revolute",
                    "parent": "base",
                    "axis": {"x": 0, "y": 0, "z": 1},
                    "min": -180,
                    "max": 180,
                    "max_velocity": 90,
                },
                {"id": "wrist", "type": "revolute", "parent": "upper", "axis": {"x": 0, "y": 0, "z": 1}, "min": -360, "max": 360},
                {
                    "id": "follower",
                    "type": "revolute",
                    "parent": "wrist",
                    "axis": {"x": 0, "y": 0, "z": 1},
                    "mimic": {"joint": "wrist", "multiplier": -1, "offset": 0},
                },
            ],
        }

    def test_unbounded_joint_has_no_file(self):
        assert _sva_file(planar_arm()) is None

    def test_collision_mesh_without_bytes_has_no_file(self):
        model = KinematicModel(links=[KinematicLink(id="a", collision=[Geometry(mesh=Mesh(content_type="ply"))])])
        assert _sva_file(model) is None

    @pytest.mark.parametrize("case", [case for case in CASES if not case.startswith("error_")])
    def test_fixtures(self, case: str):
        model = expected_model(case)
        bounded = all(j.HasField("mimic") or (j.limits.HasField("min") and j.limits.HasField("max")) for j in model.joints)
        file = _sva_file(model)
        assert (file is not None) == bounded
        if file is not None:
            doc = json.loads(file)
            assert [link["id"] for link in doc["links"]] == [link.id for link in model.links]
            assert [joint["id"] for joint in doc["joints"]] == [joint.id for joint in model.joints]


def bounded_arm() -> KinematicModel:
    model = planar_arm()
    del model.joints[1:]
    model.links[0].collision.append(
        Geometry(label="c", mesh=Mesh(content_type="ply", mesh=b"ply", original_file_source_path_diagnostic="c.ply"))
    )
    model.links[0].visual.append(
        Geometry(label="v", mesh=Mesh(content_type="glb", mesh=b"glb", original_file_source_path_diagnostic="v.glb"))
    )
    return model


class ModelOnlyArm(MockArm):
    """An arm written against the typed model, which leaves the deprecated get_kinematics alone."""

    get_kinematics = Arm.get_kinematics


@pytest.fixture
def arm() -> MockArm:
    arm = MockArm("arm")
    arm.kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_URDF, b"<robot/>", {})
    return arm


@pytest.fixture
def model_arm() -> ModelOnlyArm:
    arm = ModelOnlyArm("arm")
    arm.kinematic_model = bounded_arm()
    return arm


async def get_kinematics(arm: MockArm, **flags: bool) -> GetKinematicsResponse:
    async with ChannelFor([ArmRPCService(ResourceManager([arm]))]) as channel:
        return await ArmServiceStub(channel).GetKinematics(GetKinematicsRequest(name=arm.name, **flags))


class TestService:
    async def test_file_only_resource(self, arm: MockArm):
        for flags in ({}, {"include_collision_meshes": True}):
            response = await get_kinematics(arm, **flags)
            assert (response.format, response.kinematics_data) == (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_URDF, b"<robot/>")
            assert not response.HasField("model")

    async def test_no_flags_serves_file_and_whole_model(self, model_arm: ModelOnlyArm):
        response = await get_kinematics(model_arm)
        want = bounded_arm()
        want.name = "arm"
        assert response.model == want
        assert response.format == KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA
        doc = json.loads(response.kinematics_data)
        assert doc["name"] == "arm"
        assert doc["joints"][0]["max_velocity"] == 90
        assert doc["links"][0]["geometry"]["mesh_data"] == base64.b64encode(b"ply").decode()
        # the resource is asked for every mesh, since a client that sends no flags expects them whole
        assert (model_arm.include_collision_meshes, model_arm.include_visual_meshes) == (True, True)
        # and the model it holds is not the one we renamed
        assert model_arm.kinematic_model.name == "planar"

    @pytest.mark.parametrize("collision,visual", [(True, False), (False, True), (True, True)])
    async def test_flags_serve_the_model_alone(self, model_arm: ModelOnlyArm, collision: bool, visual: bool):
        response = await get_kinematics(model_arm, include_collision_meshes=collision, include_visual_meshes=visual)
        assert response.kinematics_data == b""
        assert response.format == KinematicsFileFormat.KINEMATICS_FILE_FORMAT_UNSPECIFIED
        base = response.model.links[0]
        assert base.collision[0].mesh.mesh == (b"ply" if collision else b"")
        assert base.visual[0].mesh.mesh == (b"glb" if visual else b"")
        # a mesh that lost its bytes still says where it came from
        assert base.collision[0].mesh.original_file_source_path_diagnostic == "c.ply"
        assert base.visual[0].mesh.content_type == "glb"
        assert (model_arm.include_collision_meshes, model_arm.include_visual_meshes) == (collision, visual)
        assert model_arm.kinematic_model == bounded_arm()

    async def test_unbounded_model_has_no_file(self, model_arm: ModelOnlyArm):
        model_arm.kinematic_model = planar_arm()
        response = await get_kinematics(model_arm)
        assert response.kinematics_data == b""
        assert len(response.model.joints) == 3

    async def test_resource_with_both(self, arm: MockArm):
        arm.kinematic_model = bounded_arm()
        response = await get_kinematics(arm)
        assert (response.format, response.kinematics_data) == (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_URDF, b"<robot/>")
        assert response.model.name == "arm"
        assert response.model.joints == bounded_arm().joints

    async def test_resource_forwarding_to_a_server_without_a_model(self, arm: MockArm):
        class Forwarding(MockArm):
            async def get_kinematic_model(self, **kwargs) -> KinematicModel:
                raise NotSupportedError("the arm behind this one sent no kinematic model")

        forwarding = Forwarding("arm")
        forwarding.kinematics = arm.kinematics
        for flags in ({}, {"include_visual_meshes": True}):
            response = await get_kinematics(forwarding, **flags)
            assert response.kinematics_data == b"<robot/>"
            assert not response.HasField("model")

    async def test_resource_with_neither(self):
        class Bare(ModelOnlyArm):
            get_kinematic_model = Arm.get_kinematic_model

        bare = Bare("arm")
        with pytest.raises(MethodNotImplementedError):
            await bare.get_kinematics()
        with pytest.raises(MethodNotImplementedError):
            await bare.get_kinematic_model()
        with pytest.raises(GRPCError):
            await get_kinematics(bare)


class TestClient:
    async def test_arm(self, model_arm: ModelOnlyArm):
        async with ChannelFor([ArmRPCService(ResourceManager([model_arm]))]) as channel:
            client = ArmClient(model_arm.name, channel)
            model = await client.get_kinematic_model(include_collision_meshes=True, extra={"1": "2"}, timeout=1.1)
            assert model.joints == bounded_arm().joints
            assert model.links[0].collision[0].mesh.mesh == b"ply"
            assert model.links[0].visual[0].mesh.mesh == b""
            assert model_arm.extra == {"1": "2"}
            assert model_arm.timeout is not None

            # the deprecated call still answers, from the file the server wrote out of the model
            kinematics: KinematicsReturn = await client.get_kinematics()
            assert kinematics[0] == KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA
            assert len(kinematics) == 4

    async def test_server_without_a_model(self, arm: MockArm):
        async with ChannelFor([ArmRPCService(ResourceManager([arm]))]) as channel:
            with pytest.raises(NotSupportedError, match="sent no kinematic model"):
                await ArmClient(arm.name, channel).get_kinematic_model()

    async def test_gantry_and_gripper(self):
        gantry = MockGantry("gantry", [1], [2])
        gripper = MockGripper("gripper")
        gantry.kinematic_model = bounded_arm()
        gripper.kinematic_model = bounded_arm()
        async with ChannelFor([GantryRPCService(ResourceManager([gantry])), GripperRPCService(ResourceManager([gripper]))]) as channel:
            for client in (GantryClient("gantry", channel), GripperClient("gripper", channel)):
                model = await client.get_kinematic_model(include_visual_meshes=True)
                assert model.name == client.name
                assert model.links[0].visual[0].mesh.mesh == b"glb"
                assert model.links[0].collision[0].mesh.mesh == b""
