# Protobuf vs Implementation Gap Analysis

This report identifies discrepancies between protobuf definitions and Python SDK implementations.

## Summary of Findings

### Components with Missing Methods

#### ARM Component
**MISSING IN BASE CLASS (arm.py):**
- `move_through_joint_positions` - Move through multiple joint positions (from `MoveThroughJointPositions`)

**MISSING IN CLIENT (client.py):**
- `get_3d_models` - Get 3D models for the arm (from `Get3DModels`)
- `move_through_joint_positions` - Move through multiple joint positions

**MISSING IN SERVICE (service.py):**
- `Get3DModels` - RPC handler for getting 3D models
- `MoveThroughJointPositions` - RPC handler for moving through joint positions

#### BOARD Component  
**MISSING IN BASE CLASS (board.py):**
- `get_digital_interrupt_value` (from `GetDigitalInterruptValue`)
- `get_gpio` (from `GetGPIO`)
- `pwm` (from `PWM`)
- `pwm_frequency` (from `PWMFrequency`)
- `read_analog_reader` (from `ReadAnalogReader`)
- `set_gpio` (from `SetGPIO`)
- `write_analog` (from `WriteAnalog`)

Note: Board has alternative API pattern using `gpio_pin_by_name()`, `analog_by_name()`, and `digital_interrupt_by_name()` which return helper objects. The base methods may be intentionally not exposed as they're accessed through these helper objects.

**MISSING IN CLIENT (client.py):**
- Same methods as base class

#### CAMERA Component
**MISSING IN BASE CLASS (camera.py):**
- `get_image` (from `GetImage`) - Get single image
- `render_frame` (from `RenderFrame`) - Render frame

**MISSING IN CLIENT (client.py):**
- Same methods as base class

Note: Camera has `get_images()` (plural) which may be the intended API, but `GetImage` (singular) exists in protobuf.

#### INPUT (INPUT_CONTROLLER) Component
**MISSING IN BASE CLASS (input.py):**
- `stream_events` (from `StreamEvents`) - Stream input events
- `trigger_event` (from `TriggerEvent`) - Trigger a specific event

**MISSING IN CLIENT (client.py):**
- `stream_events` - Stream input events

Note: `trigger_event` is implemented in client but not in base class.

#### MOVEMENT_SENSOR Component
**MISSING IN BASE CLASS (movement_sensor.py):**
- `get_readings` (from `GetReadings`) - Get all sensor readings at once

Note: This is implemented in client but not declared in base class abstract methods.

#### POWER_SENSOR Component
**MISSING IN BASE CLASS (power_sensor.py):**
- `get_readings` (from `GetReadings`) - Get all sensor readings at once

Note: This is implemented in client but not declared in base class abstract methods.

### Services with Missing Methods

#### VISION Service
**MISSING IN SERVICE (service.py):**
- `GetClassificationsFromCamera` - RPC handler for getting classifications from camera

Note: This method exists in base class and client but the service RPC handler is missing.

#### WORLDSTATESTORE Service  
**MISSING IN SERVICE (service.py):**
- `StreamTransformChanges` - RPC handler for streaming transform changes (implemented but not properly registered)

Note: The handler exists but may not be properly wired up in the service base class registration.

### Fully Compliant Components

The following components have all protobuf methods properly implemented:
- ✓ BASE
- ✓ ENCODER
- ✓ GANTRY
- ✓ GRIPPER
- ✓ MOTOR
- ✓ POSE_TRACKER
- ✓ SENSOR
- ✓ SERVO
- ✓ SWITCH
- ✓ BUTTON
- ✓ AUDIO_IN
- ✓ AUDIO_OUT

### Fully Compliant Services

The following services have all protobuf methods properly implemented:
- ✓ MOTION
- ✓ NAVIGATION
- ✓ SLAM
- ✓ MLMODEL
- ✓ DISCOVERY

## Detailed Analysis by Component

### 1. ARM Component

**Protobuf Methods (11):**
GetEndPosition, MoveToPosition, GetJointPositions, MoveToJointPositions, MoveThroughJointPositions, Stop, IsMoving, DoCommand, GetKinematics, GetGeometries, Get3DModels

**Base Class Methods (7):**
get_end_position, move_to_position, get_joint_positions, move_to_joint_positions, stop, is_moving, get_kinematics

**Client Methods (9):**
get_end_position, move_to_position, get_joint_positions, move_to_joint_positions, stop, is_moving, get_kinematics, do_command, get_geometries

**Service Handlers (9):**
GetEndPosition, MoveToPosition, GetJointPositions, MoveToJointPositions, Stop, IsMoving, DoCommand, GetKinematics, GetGeometries

**Gaps:**
- MoveThroughJointPositions: Not in base, client, or service
- Get3DModels: Not in base, client, or service

### 2. BOARD Component

**Protobuf Methods (13):**
GetGPIO, SetGPIO, PWM, SetPWM, PWMFrequency, SetPWMFrequency, ReadAnalogReader, WriteAnalog, GetDigitalInterruptValue, StreamTicks, SetPowerMode, GetGeometries, DoCommand

**Note:** Board uses a different API pattern with helper objects rather than direct methods. The Python SDK intentionally provides `gpio_pin_by_name()`, `analog_by_name()`, and `digital_interrupt_by_name()` which return objects with methods like `get()`, `set()`, `read()`, `write()`, `value()`. This is a design choice and may not be a true gap.

### 3. CAMERA Component

**Protobuf Methods (7):**
GetImage, GetImages, RenderFrame, GetPointCloud, GetProperties, GetGeometries, DoCommand

**Base Class Methods (3):**
get_images, get_point_cloud, get_properties

**Gaps:**
- GetImage (singular): Exists in protobuf but Python only has get_images (plural)
- RenderFrame: Not implemented

### 4. INPUT Component

**Protobuf Methods (6):**
GetControls, GetEvents, StreamEvents, TriggerEvent, GetGeometries, DoCommand

**Base Class Methods (2):**
get_controls, get_events

**Gaps:**
- stream_events: Not in base or client
- trigger_event: In client but not in base class

## App Clients

The app clients (app_client.py, data_client.py, billing_client.py, ml_training_client.py, provisioning_client.py) are extensive and have ~218 protobuf methods total. A comprehensive analysis would require significant effort. Spot checking suggests these are generally well-maintained.

## Recommendations

### High Priority (Breaking API Gaps)
1. **ARM**: Add `move_through_joint_positions` to base, client, and service
2. **ARM**: Add `get_3d_models` to base, client, and service
3. **CAMERA**: Add `get_image` (singular) or document why `get_images` is preferred
4. **CAMERA**: Add `render_frame` if needed
5. **INPUT**: Add `stream_events` to base and client
6. **INPUT**: Add `trigger_event` to base class (already in client)
7. **VISION**: Add `GetClassificationsFromCamera` service handler

### Medium Priority (Sensor Readings)
8. **MOVEMENT_SENSOR**: Add `get_readings` to base class (already in client)
9. **POWER_SENSOR**: Add `get_readings` to base class (already in client)

### Low Priority (Investigate)
10. **BOARD**: Review if the alternative API pattern is intentional or if direct protobuf methods should be exposed
11. **WORLDSTATESTORE**: Verify `StreamTransformChanges` service handler registration

## Notes

- Common methods like `DoCommand`, `GetGeometries`, `GetKinematics`, and `Get3DModels` are often inherited from ComponentBase and may not appear in individual base classes
- Some gaps may be intentional design choices (e.g., Board's helper object pattern)
- The Python SDK generally uses snake_case while protobuf uses PascalCase
- Client implementations are generally more complete than base class abstractions
