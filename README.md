# Viam Python SDK

## (In)stability Notice
This is an alpha release of the Viam Python SDK. Stability is not guaranteed. Breaking changes are likely to occur, and occur often.

## Installation
To install, you need to be invited to the repository. You will also need a [GitHub Access Token](https://github.com/settings/tokens).

Once you have access and a token, you can install the SDK with the command:

`pip install git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git`

This will install the current `main` branch to your project. If you would like a specific branch or commit, you can do so with the command

`pip install git+https://YOUR_ACCESS_TOKEN@github.com/viamrobotics/python-sdk.git@FULL_COMMIT_HASH`

## Usage
To connect to a server, you can use the `viam.rpc.dial.dial_direct` function, passing in an address and `DialOptions` (`viam.rpc.dial.DialOptions`). This will return a gRPC `Channel` which you can use to instantiate gRPC Services from the `proto` package, e.g.

```python
from proto.api.component.v1 import imu_grpc

# OMITTED: Obtian a channel using dial_direct

service = imu_grpc.IMUServiceStub(channel)
response = await service.ReadOrientation(...)
```

View the `examples` for more details.
