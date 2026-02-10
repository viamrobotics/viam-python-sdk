# Protobuf Gap Analysis - Quick Reference

## Summary of All Gaps

### Components with Missing Methods

| Component | Method | Missing In | Priority |
|-----------|--------|------------|----------|
| **ARM** | move_through_joint_positions | Base, Client, Service | HIGH |
| **ARM** | get_3d_models | Base, Client, Service | HIGH |
| **CAMERA** | get_image | Base, Client | MEDIUM |
| **CAMERA** | render_frame | Base, Client | MEDIUM |
| **INPUT** | stream_events | Base, Client | MEDIUM |
| **INPUT** | trigger_event | Base only | MEDIUM |
| **MOVEMENT_SENSOR** | get_readings | Base only | LOW |
| **POWER_SENSOR** | get_readings | Base only | LOW |

### Gap Count by Component

| Component | Total Methods | Missing | Compliance % |
|-----------|---------------|---------|--------------|
| ARM | 11 | 2 | 82% |
| BASE | 9 | 0 | 100% ✓ |
| BOARD | 13 | 0* | 100% ✓ |
| CAMERA | 7 | 2 | 71% |
| ENCODER | 5 | 0 | 100% ✓ |
| GANTRY | 9 | 0 | 100% ✓ |
| GRIPPER | 8 | 0 | 100% ✓ |
| INPUT | 6 | 2 | 67% |
| MOTOR | 12 | 0 | 100% ✓ |
| MOVEMENT_SENSOR | 11 | 1 | 91% |
| POWER_SENSOR | 5 | 1 | 80% |
| SENSOR | 3 | 0 | 100% ✓ |
| SERVO | 6 | 0 | 100% ✓ |

*Board uses intentional alternative API pattern

### Services Status

| Service | Total Methods | Missing | Status |
|---------|---------------|---------|--------|
| VISION | 8 | 0 | ✓ Complete |
| MOTION | 8 | 0 | ✓ Complete |
| NAVIGATION | 10 | 0 | ✓ Complete |
| SLAM | 5 | 0 | ✓ Complete |
| MLMODEL | 2 | 0 | ✓ Complete |
| DISCOVERY | 2 | 0 | ✓ Complete |
| WORLDSTATESTORE | 4 | 0 | ✓ Complete |

## Action Items by Priority

### High Priority (Breaking API Gaps)
1. ARM: Implement `move_through_joint_positions` (base, client, service)
2. ARM: Implement `get_3d_models` (base, client, service)

### Medium Priority (Feature Gaps)
3. CAMERA: Clarify/implement `get_image` vs `get_images`
4. CAMERA: Clarify/implement `render_frame`
5. INPUT: Implement `stream_events` (base, client)
6. INPUT: Add `trigger_event` to base class (already in client)

### Low Priority (Base Class Declarations)
7. MOVEMENT_SENSOR: Declare `get_readings` in base class
8. POWER_SENSOR: Declare `get_readings` in base class

## Overall Statistics

- **Components Analyzed:** 13
- **Services Analyzed:** 7
- **Fully Compliant:** 13 out of 20 (65%)
- **Total Gap Items:** 8 unique methods across 5 components
- **Total Missing Implementations:** 15 (counting base + client + service separately)

## Files That Need Changes

### High Priority Files
```
src/viam/components/arm/arm.py           # Add 2 abstract methods
src/viam/components/arm/client.py        # Add 2 methods
src/viam/components/arm/service.py       # Add 2 RPC handlers
```

### Medium Priority Files
```
src/viam/components/camera/camera.py     # Add 2 abstract methods
src/viam/components/camera/client.py     # Add 2 methods
src/viam/components/input/input.py       # Add 2 abstract methods
src/viam/components/input/client.py      # Add 1 method
```

### Low Priority Files
```
src/viam/components/movement_sensor/movement_sensor.py  # Add 1 abstract method
src/viam/components/power_sensor/power_sensor.py        # Add 1 abstract method
```

## Next Steps

1. Review this analysis with the team
2. Prioritize which gaps to address based on user demand and API stability
3. Create tickets for each gap that needs to be filled
4. Consider if any gaps are intentional design decisions (like Board)
5. Update documentation to explain any intentional API differences
