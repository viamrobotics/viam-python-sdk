# Viam Python SDK

## (In)stability Notice
This is an alpha release of the Viam Python SDK. Stability is not guaranteed. Breaking changes are likely to occur, and occur often.

## Installation - pre open sourcing
To install, you need to be invited to the repository. You will also need a [GitHub Access Token](https://github.com/settings/tokens).

Once you have access and a token, you can install the SDK with the command:

`pip install git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git`

This will install the current `main` branch to your project. If you would like a specific branch or commit, you can do so with the command

`pip install git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git@FULL_COMMIT_HASH`

It is recommended that you install using a commit hash, as that will allow you to upgrade/install over an existing installation, rather than having to uninstall and reinstall to upgrade.

## Usage
To connect to a server, you can use the `viam.rpc.dial.dial_direct` function, passing in an address and `DialOptions` (`viam.rpc.dial.DialOptions`). This will return a gRPC `Channel` which you can use to instantiate gRPC Services from the `proto` package, e.g.

```python
from viam.proto.api.component import imu

# OMITTED: Obtian a channel using dial_direct

service = imu.IMUServiceStub(channel)
response = await service.ReadOrientation(...)
```

View the `examples` for more details.

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
