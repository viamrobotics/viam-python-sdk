# Viam Python SDK
[![documentation](https://img.shields.io/static/v1?label=docs&message=python.viam.dev&color=informational)](https://python.viam.dev)
![build status](https://github.com/viamrobotics/python-sdk/actions/workflows/test.yml/badge.svg)
[![license](https://img.shields.io/badge/license-Apache_2.0-blue)](https://github.com/viamrobotics/viam-python-sdk/blob/main/LICENSE)

## (In)stability Notice

> **Warning**
> This is an alpha release of the Viam Python SDK. Stability is not guaranteed. Breaking changes are likely to occur, and occur often.

## Installation
Currently, we have pre-built binaries for macOS (both Intel and Apple Silicon), along with Linux (x86 and aarch64) that you can install via pip

`pip install viam-sdk`

If your system is not supported, read further on how to install from source.

### Upgrading

> **Note**
> Because the SDK is under active development, we suggest that you upgrade the package frequently.

To upgrade, simply run the `pip install` command with the `-U` option:
`pip install -U viam-sdk`

### Installing from Source
The Viam Python SDK uses native libraries to support communication over WebRTC, which will allow you to connect to robots that are not on the same network. In order to facilitate that communication, there is a [Rust SDK](https://github.com/viamrobotics/viam-rust-sdk) that contains the necessary protocols. Therefore, to build from source, you will need both the Rust SDK and the Rust compiler.

1. Download/clone this repository
1. Download/clone the [Rust SDK](https://github.com/viamrobotics/viam-rust-sdk)
1. [Install Rust](https://www.rust-lang.org/tools/install) if not already available
1. From the `viam-rust-sdk` directory, run `cargo build`
    * You can optionally provide the `--release` flag: `cargo build --release`
1. Find the compiled library in `viam-rust-sdk/target/debug/libviam.*`
    * If you provided the `--release` flag, the enclosing directory will be `release`: `viam-rust-sdk/target/release/libviam.*`
    * The extension of the executable will depend on your operating system. For example, on macOS it will be `libviam.dylib`, whereas on Linux it will be `libviam.so`
1. Copy the compiled library to the directory `viam-python-sdk/src/viam/rpc/`
1. From the `viam-python-sdk` directory, run `poetry build` to create an installable package
1. Find the newly created installable package located in `viam-python-sdk/dist/` and pip install it directly, e.g.: `pip install viam-python-sdk/dist/viam_sdk-0.1.0-py3-none-any.whl`


If you do **NOT** need communication over WebRTC (and thus, do not need the native library), the steps are:

1. Download/clone this repository
1. Run `poetry build` from the `viam-python-sdk` directory
1. Find the newly created installable package located in `viam-python-sdk/dist/` and pip install it directly, e.g.: `pip install viam-python-sdk/dist/viam_sdk-0.1.0-py3-none-any.whl`
1. Ensure that every connection has the option `disable_webrtc` set to `True`: `viam.rpc.dial.DialOptions(disable_webrtc=True)`
    * For more information about connecting to a robot, see the [documentation](https://python.viam.dev) and [example usage](https://python.viam.dev/examples/example.html)

## Configure a client application at [app.viam.com](https://app.viam.com)

Your client application does not directly interact with your hardware. Instead, your client application makes calls to the viam-server which can then issues commands to your hardware or read from sensors.

To create a client application, to navigate to [app.viam.com](https://app.viam.com). After you log in, perform these steps:

1. Create a location (for example `home`)
2. Create a robot (for example `arduino`)
3. Follow the steps on the setup tab:
   1. Setup Viam App Config on Single Board Computer (SBC)
   2. Download and Install Viam Server
   3. Wait until the robot shows as connected. If this doesn't happen try restarting the viam-server:
      ```
      sudo systemctl restart viam-server
      ```

Next, select the `CONNECT` tab in the Viam Web UI, and copy the boilerplate code from the section labeled `Python SDK`.

To ensure the installation succeeded and the systems are functional, save and run this simple program. If the program runs successfully, the python-sdk is properly installed, the `viam-server` instance on your robot is alive, and the computer running the program is able to connect to that instance.

## Examples
Read the [Example Usage](https://python.viam.dev/examples/example.html) page, to learn how to access a component, build a custom component, and expose
custom components as a remote to existing robots.

More examples can be found in the [`examples`](/examples) directory.

## The `do` method
Every component provided by the SDK includes a generic `do` method which is useful to execute commands that are not already defined on the component.
```python
async def do(self, command: Dict[str, Any]) -> Dict[str, Any]
```

If this is not generic enough, you can also create your own custom component by subclassing the [`viam.components.generic.Generic`](https://python.viam.dev/autoapi/viam/components/generic/index.html) component
class. For more details, you can view the documentation for the [`Generic`](https://python.viam.dev/autoapi/viam/components/generic/index.html) component.

## Documentation
Documentation, like this entire project, is under active development, and can be found at [python.viam.dev](https://python.viam.dev).

---
## Development
To contribute to the python SDK, please see the [contribution guidelines](https://python.viam.dev/contributing.html).

### Adding new component types
The SDK provides a number of abstract base components. To add more abstract base components, follow these steps:

1. Create a new directory in `viam.components` with the name of the new component
2. Create 3 new files in the newly created directory:
    1. Add all imports for the package in `__init__.py`
    2. Define all requirements of the component in `{COMPONENT}.py`
    3. Implement the gRPC service for the new component in `service.py`
3. Add the new service to [`viam.rpc.server`](https://python.viam.dev/autoapi/viam/rpc/server/index.html) to expose the gRPC service
4. If the component needs to be included in the robot/status service, add it in [`viam.robot.service`](https://python.viam.dev/autoapi/viam/robot/service/index.html)
5. Write tests for the new component and add the component to `tests.mocks.components`
6. Add the component to `examples.server.v1.components` and its corresponding concrete type in `examples.server.v1.server`

## License
Copyright 2021-2022 Viam Inc.

Apache 2.0 - See [LICENSE](https://github.com/viamrobotics/viam-python-sdk/blob/main/LICENSE) file
