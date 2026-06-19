// main.go — generates golden spatialmath conversion vectors using the canonical
// go.viam.com/rdk/spatialmath package. Run with:
//
//	go run . > ../../tests/spatialmath/fixtures/golden.json
//
// The output JSON is the source of truth for the Python parity tests that
// validate the Rust-FFI-backed spatialmath bindings produce identical results.
package main

import (
	"encoding/json"
	"fmt"
	"os"

	"gonum.org/v1/gonum/num/quat"

	"go.viam.com/rdk/spatialmath"
)

// entry mirrors the JSON schema expected by the Python parity tests.
type entry struct {
	Name           string     `json:"name"`
	Quat           [4]float64 `json:"quat"`            // [w, i, j, k]
	OV             [4]float64 `json:"ov"`              // [ox, oy, oz, theta_rad]
	Euler          [3]float64 `json:"euler"`           // [roll, pitch, yaw] radians (ZYX / Tait-Bryan)
	AxisAngle      [4]float64 `json:"axis_angle"`      // [x, y, z, theta_rad]
	RotationMatrix [9]float64 `json:"rotation_matrix"` // 9 elements ROW-MAJOR (row0, row1, row2)
}

// output is the top-level JSON object.
type output struct {
	QuaternionConversions []entry `json:"quaternion_conversions"`
}

func convert(name string, w, i, j, k float64) entry {
	q := &spatialmath.Quaternion{Real: w, Imag: i, Jmag: j, Kmag: k}

	// Orientation vector (radians)
	ov := q.OrientationVectorRadians()

	// Euler angles (roll=X, pitch=Y, yaw=Z; ZYX Tait-Bryan, radians)
	ea := q.EulerAngles()

	// Axis angle
	aa := q.AxisAngles()

	// Rotation matrix — rdk stores as row-major [9]float64 internally.
	// rm.At(row, col) == mat[3*row + col], so iterating At(r,c) for r,c in
	// 0..2 produces row-major order directly. No transposition is needed.
	rm := q.RotationMatrix()
	var mat [9]float64
	for r := 0; r < 3; r++ {
		for c := 0; c < 3; c++ {
			mat[3*r+c] = rm.At(r, c)
		}
	}

	return entry{
		Name: name,
		Quat: [4]float64{
			quat.Number(*q).Real,
			quat.Number(*q).Imag,
			quat.Number(*q).Jmag,
			quat.Number(*q).Kmag,
		},
		OV:             [4]float64{ov.OX, ov.OY, ov.OZ, ov.Theta},
		Euler:          [3]float64{ea.Roll, ea.Pitch, ea.Yaw},
		AxisAngle:      [4]float64{aa.RX, aa.RY, aa.RZ, aa.Theta},
		RotationMatrix: mat,
	}
}

func main() {
	inputs := []struct {
		name       string
		w, i, j, k float64
	}{
		// identity: no rotation
		{"identity", 1, 0, 0, 0},
		// x90: 90-degree rotation about the X axis
		{"x90", 0.7071067811865476, 0.7071067811865476, 0, 0},
		// y180: 180-degree rotation about the Y axis
		{"y180", 0, 0, 1, 0},
		// tumble: equal parts rotation — 120° about axis (1/√3, 1/√3, 1/√3)
		{"tumble", 0.5, 0.5, 0.5, 0.5},
	}

	entries := make([]entry, 0, len(inputs))
	for _, inp := range inputs {
		entries = append(entries, convert(inp.name, inp.w, inp.i, inp.j, inp.k))
	}

	out := output{QuaternionConversions: entries}
	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")
	if err := enc.Encode(out); err != nil {
		fmt.Fprintf(os.Stderr, "json encode error: %v\n", err)
		os.Exit(1)
	}
}
