import abc

from viam.proto.api.common import Pose
from viam.proto.api.component.arm import JointPositions
from viam.message_wrappers.wrappers import PyPose

from ..component_base import ComponentBase


class Arm(ComponentBase):
    """
    Abstract representation of a robotics Arm that
    exists in three-dimensional space. This acts 
    as an abstract base class for any drivers representing 
    specific arm implementations. This cannot be used 
    on its own. 

    If you override the init function,
    you must call the super init function.
    """

    @abc.abstractmethod
    async def get_end_position(self) -> PyPose:
        """
        Purpose: 
        Get the current position of the end of
        the robot's arm expressed as X, Y, Z, ox,
        oy, oz, theta

        Arguments:
        None 

        Returns:
        Pose: Current position of the end 
        of the robot's arm
        """
        ...

    @abc.abstractmethod
    async def move_to_position(self, pose: PyPose):
        """
        Purpose: 
        Move the end of the robot's arm to the 
        requested position

        Arguments:
            pose (PyPose): The position to move the end 
            of the robot's arm to

        Returns: 
        None
        """
        ...

    @abc.abstractmethod
    async def move_to_joint_positions(self, positions: JointPositions):
        """
        Purpose:
        Move every joint on a robot's arm to 
        specified angles which are expressed in 
        degrees

        Arguments:
            JointPositions: A list of joint 
            positions represented in degrees. 
            The numbers are ordered spatially 
            from the base toward the end effector.
            This specifies the degrees by which
            to turn each joint on the robot's arm

        Returns:
        None

        """
        ...

    @abc.abstractmethod
    async def get_joint_positions(self) -> JointPositions:
        """
        Purpose:
        Get the current joint positions for this arm

        Arguments:
            Note

        Returns:
            A list of joint positions represented
            in degrees. The numbers are ordered 
            spatially from the base toward the 
            end effector. This specifies the 
            current position of each joint on 
            the robot's arm


        """
        ...
