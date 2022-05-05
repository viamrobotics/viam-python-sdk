# Viam Python SDK
[![documentation](https://img.shields.io/static/v1?label=docs&message=python.viam.dev&color=informational)](https://python.viam.dev)
![build status](https://github.com/viamrobotics/python-sdk/actions/workflows/test.yml/badge.svg)

## (In)stability Notice
This is an alpha release of the Viam Python SDK. Stability is not guaranteed. Breaking changes are likely to occur, and occur often.

## Installation - pre open sourcing
To install, you need to be invited to the repository. You will also need a [GitHub Access Token](https://github.com/settings/tokens).

Once you have access and a token, you can install the SDK with the command:

`pip install git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git`

This will install the current `main` branch to your project. If you would like a specific branch or commit, you can do so with the command

`pip install git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git@FULL_COMMIT_HASH`

### Upgrading
Because the SDK is under active development, we suggest that you upgrade the package frequently. To do so, simply run the `pip install` command with the `-U` option:

`pip install -U git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git`

## Usage
To connect to a server, you can use the `viam.rpc.dial.dial_direct` function, passing in an address and `DialOptions` (`viam.rpc.dial.DialOptions`). This will return a gRPC `Channel` which you can use to instantiate component clients, e.g.

```python
from viam.proto.api.component import motor

# OMITTED: Obtian a channel using dial_direct

my_motor = motor.MotorClient(name='my_motor', channel=channel)
await my_motor.set_power(0.9)
await asyncio.sleep(3)
await my_motor.set_power(0)
position = await my_motor.get_position()
```

View the [`examples`](https://github.com/viamrobotics/python-sdk/tree/main/examples) for more details.

## Easy Setup via app.viam.com
The easiest way to get started writing a client application (that is, one which is not directly responsible for interacting hardware,
but rather calls into the viam-server to actuate hardware or read from sensors), is to navigate to the robot page on app.viam.com,
select the `CONNECT` tab, and copy the boilerplate code from the section labeled `Python SDK`.

It is recommended that you save and run this simple program. Doing so will ensure that the python-sdk is properly installed,
that the viam-server instance on your robot is alive, and that the computer running the program is able to connect to that instance.

### Accessing a component:
First you'll need to access the RobotClient. This should look:
```python
from viam.robot.client import RobotClient
```

Then to instantiate the robot, you'll call one of two class methods, `RobotClient.at_address`, `RobotClient.with_channel`, which will
return a `RobotClient` that can be used to access the components of the robot.
```python
robot = await RobotClient.with_channel(channel=channel, options=RobotClient.Options(refresh_interval=10))
```

You can then use this Robot to access components by name. Take a look at the component documentation to
see a full list of methods for the object and their arguments. For Example:
```python
motor = Motor.from_robot(robot, 'my_motor')
await motor.go_for(rpm=60, revolutions=100)
```

## Implementing a component and using the python-sdk as server:
Find the Component type you wish to implement in the docs and create a new class which sub-classes that Component’s BaseComponent class.

You’ll need to create an implementation of each method that class has. If however you do not need or wish to implement every method,
a simple no-op method whose body consists of `pass` is sufficient to get the server up and running.
For a simple Server program, your `main()` method can look like:
```python
async def main():
    srv = Server(components=[MyCoolMotor("left_motor")])
    await srv.serve()
```

With this program running, you can connect directly via the python-sdk. Currently the python-sdk does not support authentication,
so you’ll want to connect insecurely. To connect your python client application to a server running on the same machine you can use:
```python
opts = DialOptions(insecure=True)
channel = await dial_direct("localhost:9090", opts)
```

To use this custom server as part of a larger robot, you’ll want to add it as a `remote` in the config for your main part.
```json
"remotes": [
    {
      "name": "my-cool-python-server",
      "insecure": true,
      "address": "localhost:9090"
    }
  ]
```

And to ensure that the python server starts up with the rest of the robot, you can add it as a process. **NOTE**: The `viam-server`
starts as a root process, so you may need to switch users to run the python SDK server.
```json
[
  {
    "id": 0,
    "log": true,
    "name": "sudo",
    "args": [
      "-u",
      "pi",
      "python",
      "/home/pi/python-server.py"
    ]
  }
]
```

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
To develop the python SDK, it is strongly encouraged that you use a python environment ([Miniconda](https://docs.conda.io/en/latest/miniconda.html), [venv](https://docs.python.org/3/library/venv.html), [pyenv](https://github.com/pyenv/pyenv), etc.)

Install the requirements: `pip install -r etc/requirements.txt`

[`flake8`](https://www.flake8rules.com) is our styleguide, and [`autopep8`](https://pypi.org/project/autopep8/) is used for automatic linting and formatting.

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
