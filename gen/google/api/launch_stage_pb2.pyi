"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _LaunchStage:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _LaunchStageEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LaunchStage.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    LAUNCH_STAGE_UNSPECIFIED: LaunchStage.ValueType = ...  # 0
    """Do not use this default value."""

    UNIMPLEMENTED: LaunchStage.ValueType = ...  # 6
    """The feature is not yet implemented. Users can not use it."""

    PRELAUNCH: LaunchStage.ValueType = ...  # 7
    """Prelaunch features are hidden from users and are only visible internally."""

    EARLY_ACCESS: LaunchStage.ValueType = ...  # 1
    """Early Access features are limited to a closed group of testers. To use
    these features, you must sign up in advance and sign a Trusted Tester
    agreement (which includes confidentiality provisions). These features may
    be unstable, changed in backward-incompatible ways, and are not
    guaranteed to be released.
    """

    ALPHA: LaunchStage.ValueType = ...  # 2
    """Alpha is a limited availability test for releases before they are cleared
    for widespread use. By Alpha, all significant design issues are resolved
    and we are in the process of verifying functionality. Alpha customers
    need to apply for access, agree to applicable terms, and have their
    projects allowlisted. Alpha releases don’t have to be feature complete,
    no SLAs are provided, and there are no technical support obligations, but
    they will be far enough along that customers can actually use them in
    test environments or for limited-use tests -- just like they would in
    normal production cases.
    """

    BETA: LaunchStage.ValueType = ...  # 3
    """Beta is the point at which we are ready to open a release for any
    customer to use. There are no SLA or technical support obligations in a
    Beta release. Products will be complete from a feature perspective, but
    may have some open outstanding issues. Beta releases are suitable for
    limited production use cases.
    """

    GA: LaunchStage.ValueType = ...  # 4
    """GA features are open to all developers and are considered stable and
    fully qualified for production use.
    """

    DEPRECATED: LaunchStage.ValueType = ...  # 5
    """Deprecated features are scheduled to be shut down and removed. For more
    information, see the “Deprecation Policy” section of our [Terms of
    Service](https://cloud.google.com/terms/)
    and the [Google Cloud Platform Subject to the Deprecation
    Policy](https://cloud.google.com/terms/deprecation) documentation.
    """

class LaunchStage(_LaunchStage, metaclass=_LaunchStageEnumTypeWrapper):
    """The launch stage as defined by [Google Cloud Platform
    Launch Stages](http://cloud.google.com/terms/launch-stages).
    """
    pass

LAUNCH_STAGE_UNSPECIFIED: LaunchStage.ValueType = ...  # 0
"""Do not use this default value."""

UNIMPLEMENTED: LaunchStage.ValueType = ...  # 6
"""The feature is not yet implemented. Users can not use it."""

PRELAUNCH: LaunchStage.ValueType = ...  # 7
"""Prelaunch features are hidden from users and are only visible internally."""

EARLY_ACCESS: LaunchStage.ValueType = ...  # 1
"""Early Access features are limited to a closed group of testers. To use
these features, you must sign up in advance and sign a Trusted Tester
agreement (which includes confidentiality provisions). These features may
be unstable, changed in backward-incompatible ways, and are not
guaranteed to be released.
"""

ALPHA: LaunchStage.ValueType = ...  # 2
"""Alpha is a limited availability test for releases before they are cleared
for widespread use. By Alpha, all significant design issues are resolved
and we are in the process of verifying functionality. Alpha customers
need to apply for access, agree to applicable terms, and have their
projects allowlisted. Alpha releases don’t have to be feature complete,
no SLAs are provided, and there are no technical support obligations, but
they will be far enough along that customers can actually use them in
test environments or for limited-use tests -- just like they would in
normal production cases.
"""

BETA: LaunchStage.ValueType = ...  # 3
"""Beta is the point at which we are ready to open a release for any
customer to use. There are no SLA or technical support obligations in a
Beta release. Products will be complete from a feature perspective, but
may have some open outstanding issues. Beta releases are suitable for
limited production use cases.
"""

GA: LaunchStage.ValueType = ...  # 4
"""GA features are open to all developers and are considered stable and
fully qualified for production use.
"""

DEPRECATED: LaunchStage.ValueType = ...  # 5
"""Deprecated features are scheduled to be shut down and removed. For more
information, see the “Deprecation Policy” section of our [Terms of
Service](https://cloud.google.com/terms/)
and the [Google Cloud Platform Subject to the Deprecation
Policy](https://cloud.google.com/terms/deprecation) documentation.
"""

global___LaunchStage = LaunchStage

