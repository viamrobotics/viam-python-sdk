# spatialmath_golden

Standalone Go program that generates `tests/spatialmath/fixtures/golden.json` — the
source-of-truth orientation conversion vectors produced by the canonical
`go.viam.com/rdk/spatialmath` package.

The fixture is consumed by the Python spatialmath parity tests to assert that the
Rust-FFI-backed Python bindings produce identical numerical results.

## Pinned rdk version

```
go.viam.com/rdk v0.98.1-0.20251023194042-e97069d07515
```

## Regenerating the fixture

From the repo root:

```bash
cd etc/spatialmath_golden
GOFLAGS=-mod=mod go mod tidy   # resolves/updates go.sum; needs network access
go run . > ../../tests/spatialmath/fixtures/golden.json
```

If the module cache is already populated and no network is available:

```bash
cd etc/spatialmath_golden
GOFLAGS=-mod=mod GOPROXY=off go mod tidy
go run . > ../../tests/spatialmath/fixtures/golden.json
```

After regenerating, commit both `go.sum` and `golden.json`.

## JSON schema

```json
{
  "quaternion_conversions": [
    {
      "name":            "<string>",
      "quat":            [w, i, j, k],
      "ov":              [ox, oy, oz, theta],
      "euler":           [roll, pitch, yaw],
      "axis_angle":      [x, y, z, theta],
      "rotation_matrix": [m0, m1, ..., m8]
    }
  ]
}
```

### Conventions

| Field | Convention |
|---|---|
| `quat` | `[w, i, j, k]` — `Real, Imag, Jmag, Kmag` of `gonum.org/v1/gonum/num/quat.Number` |
| `ov` | Orientation-vector radians: `[OX, OY, OZ, Theta]` from `OrientationVectorRadians()` |
| `euler` | `[Roll, Pitch, Yaw]` radians — ZYX Tait-Bryan (z-y′-x″ sequence) from `EulerAngles()` |
| `axis_angle` | `[RX, RY, RZ, Theta]` radians from `AxisAngles()` (= `R4AA` struct) |
| `rotation_matrix` | 9 elements in **ROW-MAJOR** order: row 0 then row 1 then row 2 |

### Row-major decision

`spatialmath.RotationMatrix` stores its data as `[9]float64` with the comment
*"m[3*r + c] is the element in the r'th row and c'th column"* (see
`rotationMatrix.go`). The generator calls `rm.At(r, c)` in row-major order
(`r` outer loop, `c` inner loop), so **no transposition is needed** — the array
is already row-major natively. Element `rotation_matrix[3*r + c]` is the value
at row `r`, column `c`.

### Identity sanity check

The `identity` quaternion `(1, 0, 0, 0)` must produce:

```
ov              = [0, 0, 1, 0]
euler           = [0, 0, 0]
axis_angle      = [0, 0, 1, 0]   (degenerate axis defaults to +Z in rdk)
rotation_matrix = [1,0,0, 0,1,0, 0,0,1]
```
