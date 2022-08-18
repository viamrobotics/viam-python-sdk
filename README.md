# Viam Python SDK
[![documentation](https://img.shields.io/static/v1?label=docs&message=python.viam.dev&color=informational)](https://python.viam.dev)
![build status](https://github.com/viamrobotics/python-sdk/actions/workflows/test.yml/badge.svg)
[![license](https://img.shields.io/badge/license-Apache_2.0-blue)](https://github.com/viamrobotics/viam-python-sdk/blob/main/LICENSE)

## (In)stability Notice
This is an alpha release of the Viam Python SDK. Stability is not guaranteed. Breaking changes are likely to occur, and occur often.

## Installation - pre open sourcing
To install, you need to be invited to the repository. You will also need a [GitHub Access Token](https://github.com/settings/tokens) with *repo* access.

Once you have access and a token, you can install the SDK with the command:

`pip install git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git`

This will install the current `main` branch to your project. If you would like a specific branch or commit, you can do so with the command

`pip install git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git@FULL_COMMIT_HASH`

### Upgrading
Because the SDK is under active development, we suggest that you upgrade the package frequently. To do so, simply run the `pip install` command with the `-U` option:

`pip install -U git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git`

## Easy Setup via [app.viam.com](app.viam.com)
The easiest way to get started writing a client application (that is, one which is not directly responsible for interacting with hardware,
but rather calls into the viam-server to actuate hardware or read from sensors), is to navigate to the robot page on [app.viam.com](app.viam.com),
select the `CONNECT` tab, and copy the boilerplate code from the section labeled `Python SDK`.

It is recommended that you save and run this simple program. Doing so will ensure that the python-sdk is properly installed,
that the `viam-server` instance on your robot is alive, and that the computer running the program is able to connect to that instance.

## Examples
The [Example Usage](https://python.viam.dev/examples/example.html) has the info required to access a component, build a custom component, and expose
custom components as a remote to existing robots.

Further examples can be found in the `examples` directory.

## The `do` method
Every component provided by the SDK includes a generic `do` method which is useful to execute commands that are not already defined on the component.
```python
async def do(self, command: Dict[str, Any]) -> Dict[str, Any]
```

If this is not generic enough, you can also create your own custom component by subclassing the `viam.components.generic.Generic` component
class. For more details, you can view the documentation for the `Generic` component.

## Documentation
Documentation, like this entire project, is under active development, and can be found at [python.viam.dev](https://python.viam.dev).

---
## Development
To develop the python SDK, please see the [contribution guidelines](https://python.viam.dev/contributing.html).

### Adding new component types
The SDK provides a number of abstract base components to start. To add more abstract base components, please make sure you follow these guidelines:

* Create a new directory in `viam.components` with the name of the new component
* Implement 3 new files in the newly created directory:
    * `__init__.py`, where you should include the imports for the package
    * `{COMPONENT}.py`, which should define the requirements of the component
    * `service.py`, which should implement the gRPC service for this component
* Add the new service in `viam.rpc.server` to expose the gRPC service
* If the component needs to be included to the robot/status service, add it in `viam.robot.service`
* Write tests and add the component to `tests.mocks.components`
* Add the component to `examples.server.v1.components` and its corresponding concrete type in `examples.server.v1.server`

## License
Copyright 2021-2022 Viam Inc.

Apache 2.0 - See [LICENSE](https://github.com/viamrobotics/viam-python-sdk/blob/main/LICENSE) file
