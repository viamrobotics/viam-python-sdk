# Viam Python SDK

![PyPI](https://img.shields.io/pypi/v/viam-sdk)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/viam-sdk)
[![documentation](https://img.shields.io/static/v1?label=docs&message=python.viam.dev&color=lightgray)](https://python.viam.dev)
![build status](https://github.com/viamrobotics/python-sdk/actions/workflows/test.yml/badge.svg)
[![license](https://img.shields.io/badge/license-Apache_2.0-blue)](https://github.com/viamrobotics/viam-python-sdk/blob/main/LICENSE)

The Viam Python SDK allows you to build robots, access existing Viam robots, and manage your fleet of Viam robots.

If you would like a blueprint on setting up a Python environment with Viam from scratch, you can follow our [Setup](https://python.viam.dev/#installing-from-source) guide.

If you would like to develop and contribute to Viam's Python SDK, take a look at the [Development](#development) portion of the README.

## Installation

Currently, we have pre-built binaries for macOS (both Intel `x86_64` and Apple Silicon) and Linux (`x86`, `aarch64`, `armv6l`) that you can install using `pip`:

`pip install viam-sdk`

If you want to install on Windows, you can install from github directly with `pip`:

`pip install git+https://github.com/viamrobotics/viam-python-sdk.git`

Note that only direct gRPC connections are supported on Windows; you will need to [disable webrtc](https://python.viam.dev/autoapi/viam/rpc/dial/index.html#viam.rpc.dial.DialOptions.disable_webrtc) or else connection will fail. Full support (including webRTC) _does_ exist on WSL.

If you intend to use the [`MLModel` service](https://python.viam.dev/autoapi/viam/services/mlmodel/mlmodel/index.html#viam.services.mlmodel.mlmodel.MLModel), use the following command instead, which installs additional required dependencies:

`pip install 'viam-sdk[mlmodel]'`

You can also run this command on an existing Python SDK install to add support for the ML model service.
See the [ML (machine learning) model service](https://docs.viam.com/data-ai/ai/deploy/) documentation for more information.

### Upgrading

To upgrade, simply run the `pip install` command with the `-U` option:
`pip install -U viam-sdk`

### Installing from Source

The Viam Python SDK uses native libraries to support communication over WebRTC, which will allow you to connect to robots that are not on the same network. In order to facilitate that communication, there is a [rust-utils repo](https://github.com/viamrobotics/rust-utils) that contains the necessary protocols. Therefore, to build from source, you will need both the Rust utils and the Rust compiler.

1. Download/clone this [repository](https://github.com/viamrobotics/viam-python-sdk)
1. Download/clone the [rust-utils](https://github.com/viamrobotics/rust-utils)
1. [Install Rust](https://www.rust-lang.org/tools/install) if not already available
1. From the `rust-utils` directory, run `cargo build`
   - You can optionally provide the `--release` flag: `cargo build --release`
1. Find the compiled library in `rust-utils/target/debug/libviam_rust_utils.*`
   - If you provided the `--release` flag, the enclosing directory will be `release`: `rust-utils/target/release/libviam_rust_utils.*`
   - The extension of the executable will depend on your operating system. For example, on macOS it will be `libviam_rust_utils.dylib`, whereas on Linux it will be `libviam_rust_utils.so`
1. Copy the compiled library to the directory `viam-python-sdk/src/viam/rpc/`
1. From the `viam-python-sdk` directory, run `uv build --wheel` to create an installable package
1. Find the newly created installable package located in `viam-python-sdk/dist/` and pip install it directly, for example: `pip install viam-python-sdk/dist/viam_sdk-0.1.0-py3-none-any.whl`

If you have a macOS or Linux based operating system and do not want to build rust-utils manually, you can also look for the executable in the [releases](https://github.com/viamrobotics/rust-utils/releases/latest) page of the rust-utils library.

If you do **NOT** need communication over WebRTC (and thus, do not need the native library), the steps are:

1. Download/clone this repository
1. Run `uv build --wheel` from the `viam-python-sdk` directory
1. Find the newly created installable package located in `viam-python-sdk/dist/` and pip install it directly, for example: `pip install viam-python-sdk/dist/viam_sdk-0.1.0-py3-none-any.whl`
1. Ensure that every connection has the option `disable_webrtc` set to `True`: `viam.rpc.dial.DialOptions(disable_webrtc=True)`
   - For more information about connecting to a robot, see the [documentation](https://python.viam.dev) and [example usage](https://python.viam.dev/examples/example.html)

## Configure a client application at [app.viam.com](https://app.viam.com)

Your client application does not directly interact with your hardware. Instead, your client application makes calls to the `viam-server` which can then issue commands to your hardware or read from sensors.

To create a client application, to navigate to [app.viam.com](https://app.viam.com). After you log in, perform these steps:

1. Create a location (for example `home`)
2. Create a robot (for example `arduino`)
3. Follow the steps on the setup tab:

   1. Setup machine cloud credentials on Single Board Computer (SBC)
   2. Download and Install Viam Server
   3. Wait until the robot shows as connected. If this doesn't happen try restarting the viam-server:

      ```
      sudo systemctl restart viam-server
      ```

Next, select the `CODE SAMPLE` tab in the Viam Web UI, and copy the boilerplate code from the section labeled `Python SDK`.

To ensure the installation succeeded and the systems are functional, save and run this simple program. If the program runs successfully, the python-sdk is properly installed, the `viam-server` instance on your robot is alive, and the computer running the program is able to connect to that instance.

## The `RobotClient` & connectivity

The main entry point for using the SDK as a client is the `RobotClient` class. This class can manage resources, operations, frames, etc., for the robot. It can also manage connectivity and behavior around sessions and reconnection through the `RobotClient.Options` nested class.

The `RobotClient` will attempt to refresh its resources at a set interval (customizable via `Options`).

In the event that connection is lost to the robot, the `RobotClient` will attempt to reconnect at a set interval. There are two options available for customizing this behavior: how often the client checks the connection status (`RobotClient.Options.check_connection_interval`), and how often the client attempts to reconnect upon detecting a loss of connection (`RobotClient.Options.attempt_reconnect_interval`).

Upon a loss of connection, outstanding requests are **NOT** terminated and can possibly error with a `GRPCError` whose status is `DEADLINE_EXCEEDED`. When connection is restored, existing built-in clients will automatically receive the new connection - no need to re-obtain the client. Tasks initiated by Viam will automatically resume, but any user-defined tasks that depend on the connection should be checked and potentially restarted.

The Viam Python SDK utilizes gRPC and, optionally WebRTC (defaults to on). gRPC is provided purely in python, but WebRTC is provided by the external [viam Rust utils](https://github.com/viamrobotics/rust-utils) library. WebRTC settings can be changed using the appropriate attributes in `viam.rpc.dial.DialOptions`. These options can be passed to the `RobotClient` through `RobotClient.Options.dial_options`.

### Sessions

Sessions are a safety feature that automatically cancel operations made by the python client if it loses connection to a robot. Sessions are enabled by default but can be disabled by setting `RobotClient.Options.disable_sessions = True`. Please see the [RDK session documentation](https://pkg.go.dev/go.viam.com/rdk/session) for more details and server-side configuration options.

## Examples

Read the [Example Usage](https://python.viam.dev/examples/example.html) page, to learn how to access a component, build a custom component, and expose
custom components as a remote to existing robots.

More examples can be found in the [`examples`](https://github.com/viamrobotics/viam-python-sdk/tree/main/examples) directory.

## Documentation

Documentation, like this entire project, is under active development, and can be found at [python.viam.dev](https://python.viam.dev).

---

## Development

To contribute to the python SDK, please see the [contribution guidelines](https://python.viam.dev/contributing.html).

### Adding new resource types

The SDK provides a number of abstract base components and services (collectively: resources). To add more abstract resources, follow these steps:

1. Create a new directory in `viam.components` or `viam.services` with the name of the new component
1. Create 4 new files in the newly created directory:
   1. Define all requirements of the resource in `{RESOURCE_NAME}.py`
   1. Implement the gRPC service for the new resource in `service.py`
   1. Create a gRPC client for the new resource in `client.py`
   1. Register the API and define package exports in `__init__.py`
1. Write tests for the new resource and add the resource to `tests.mocks.{components|services}`
1. If the resource is a component, add the component to `examples.server.v1.components` and its corresponding concrete type in `examples.server.v1.server`

## License

Copyright 2021-2024 Viam Inc.

Apache 2.0 - See [LICENSE](https://github.com/viamrobotics/viam-python-sdk/blob/main/LICENSE) file
