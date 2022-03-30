from dataclasses import dataclass
from viam.proto.api.common import Pose
from viam.proto.api.component.arm import JointPositions


@dataclass
class PyPose:
    """Pose is the combination of location and orientation
    Location is represented by distance which is 
    expressed as x , y, and z coordinates. 	
    Orientation is represented an orientation vector which 
    is expressed as o_x, o_y, o_z, and theta.
    Structured similarly to an angle axis, an 
    orientation vector works differently. Rather 
    than representing an orientation with an 
    arbitrary axis and a rotation around it from 
    an origin, an orientation vector represents 
    orientation such that the ox/oy/oz components 
    represent the point on the cartesian unit 
    sphere at which your end effector is pointing 
    from the origin, and that unit vector forms 
    an axis around which theta rotates. This 
    means that incrementing/decrementing theta 
    will perform an in-line rotation of the end 
    effector. Theta is defined as rotation between 
    two planes: the plane defined by the origin, 
    the point (0,0,1), and the rx,ry,rz point, 
    and the plane defined by the origin, the 
    rx,ry,rz point, and the new local Z axis. 
    So if theta is kept at zero as the 
    north/south pole is circled, the Roll 
    will correct itself to remain in-line."""
    x: float
    """millimeters from the end of the robot's arm"""
    y: float
    """millimeters from the end of the robot's arm"""
    z: float
    """millimeters from the end of the robot's arm"""
    o_x: float
    """degrees """
    o_y: float
    """ degrees """
    o_z: float
    """ degrees """
    theta: float

    def to_message(self) -> Pose:
        return Pose(
            x=self.x,
            y=self.y,
            z=self.z,
            o_x=self.o_x,
            o_y=self.o_y,
            o_z=self.o_z,
            theta=self.theta)

    @classmethod
    def from_message(cls, message: Pose) -> "PyPose":
        return cls(
            x=message.x,
            y=message.y,
            z=message.z,
            o_x=message.o_x,
            o_y=message.o_y,
            o_z=message.o_z,
            theta=message.theta)
