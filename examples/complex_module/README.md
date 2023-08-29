# VIAM Complex Module Example

This example goes through how to create custom modular resources using Viam's python SDK, and how to connect it to a Robot.

This is a limited document. For a more in-depth understanding of modules, see the [documentation](https://docs.viam.com/program/extend/modular-resources/).

## Purpose

Modular resources allow you to define custom components and services, and add them to your robot. Viam ships with many component types, but you're not limited to only using those types -- you can create your own using modules.

For more information, see the [documentation](https://docs.viam.com/program/extend/modular-resources/). For a simpler example, take a look at the [simple module example](https://github.com/viamrobotics/viam-python-sdk/tree/main/examples/simple_module), which only contains one custom resource model in one file.

## Project structure

The definition of the new resources are in the `src` directory. Within this directory are the `proto`, `gizmo`, `arm`, and `summation` subdirectories.

The `proto` directory contains the `gizmo.proto` and `summation.proto` definitions of all the message types and calls that can be made to the Gizmo component and Summation service. It also has the compiled python output of the protobuf definition.

The `gizmo` directory contains all the necessary definitions for creating a custom `Gizmo` component type. The `api.py` file defines what a `Gizmo` can do (mirroring the `proto` definition), implements the gRPC `GizmoService` for receiving calls, and the gRPC `GizmoClient` for making calls. See the [API docs](https://docs.viam.com/program/extend/modular-resources/#apis) for more info. The `my_gizmo.py` file in contains the unique implementation of a `Gizmo`. This is defined as a specific `Model`. See the [Model docs](https://docs.viam.com/program/extend/modular-resources/#models) for more info. This implementation uses the `validate_config` function to specify an implicit dependency on a `motor` by default and throw an error if there is an `invalid` attribute.

Similarly, the `summation` directory contains the analogous definitions for the `Summation` service type. The files in this directory mirror the files in the `gizmo` directory.

The `arm` directory contains all the necessary definitions for creating a custom modular `Arm` component type. Since it is subclassing an already existing component supported by the Viam SDK, there is no need for an `api.py` file. For a more in-depth tutorial on how to write a modular component from an existing resource, see the [documentation](https://python.viam.dev/examples/example.html#create-custom-modules).

The `base` directory contains all the necessary definitions for creating a custom modular `Base` component type. Like the previous `Arm` implementation, the `base` directory is subclassing an already existing component supported by the Viam SDK, so an `api.py` is not necessary. A more in-depth tutorial on how to write custom modular components from existing resources can be found in the [documentation](https://python.viam.dev/examples/example.html#create-custom-modules).

There is also a `main.py` file, which creates a module, adds the desired resources, and starts the module. This file is called by the `run.sh` script, which is the entrypoint for this module. Read further to learn how to connect this module to your robot.

Outside the `src` directory, there is a `client.py` file. You can use this file to test the module once you have connected to your robot and configured the module. You will have to update the credentials and robot address in that file.

## Configuring and using the module

These steps assume that you have a robot available at [app.viam.com](app.viam.com).

The `run.sh` script is the entrypoint for this module. To connect this module with your robot, you must add this module's entrypoint to the robot's config. For example, the entrypoint file may be at `/home/viam-python-sdk/examples/complex_module/run.sh` and you must add this file path to your configuration. See the [documentation](https://docs.viam.com/program/extend/modular-resources/#use-a-modular-resource-with-your-robot) for more details.

Once the module has been added to your robot, add a `Gizmo` component that uses the `MyGizmo` model. See the [documentation](https://docs.viam.com/program/extend/modular-resources/#configure-a-component-instance-for-a-modular-resource) for more details. You can also add an `Arm` component that uses the `MyArm` model and a `Summation` service that uses the `MySum` model in a similar manner.

An example configuration for an Arm component, a Gizmo component, and a Summation service could look like this:

```json
{
  "components": [
    {
      "name": "arm1",
      "type": "arm",
      "model": "acme:demo:myarm",
      "attributes": {},
      "depends_on": []
    },
    {
      "name": "gizmo1",
      "type": "gizmo",
      "namespace": "acme",
      "model": "acme:demo:mygizmo",
      "attributes": {
        "arg1": "arg1",
        "motor": "motor1"
      },
      "depends_on": []
    },
    {
      "name": "motor1",
      "type": "motor",
      "model": "fake",
      "attributes": {
        "pins": {
          "dir": "",
          "pwm": ""
        },
        "board": ""
      },
      "depends_on": []
    },
    {
      "name": "motor2",
      "type": "motor",
      "model": "fake",
      "attributes": {
        "pins": {
          "dir": "",
          "pwm": ""
        },
        "board": ""
      },
      "depends_on": []
    },
    {
      "name": "base1",
      "type": "base",
      "attributes": {
        "left": "motor1",
        "right": "motor2"
      },
      "model": "acme:demo:mybase",
      "depends_on": []
    }
  ],
  "services": [
    {
      "name": "mysum1",
      "type": "summation",
      "namespace": "acme",
      "model": "acme:demo:mysum",
      "attributes": {
        "subtract": false
      }
    }
  ],
  "modules": [
    {
      "name": "my-module",
      "executable_path": "/home/viam-python-sdk/examples/complex_module/run.sh"
    }
  ]
}
```

After the robot has started and connected to the module, you can use the provided `client.py` to connect to your robot and make calls to your custom, modular resources.
