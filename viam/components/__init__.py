"""
## Accessing a component
First you'll need to import the component's client. Generically this should look:
```python
from viam.components.component import ComponentClient
```
Example:
```python
from viam.components.motor import MotorClient
```

Then to instantiate a client, you'll call its constructor, which typically takes `name` and `channel` as arguements,
where `channel` is our connection to the robot, and `name` is the name of the component in that robot's JSON config. Example:
```python
left_motor = MotorClient(name='left', channel=channel)
```

You can then use this Component object's methods to issue viam's gRPC API calls. Take a look at the component documentation to
see a full list of methods for the object and their arguments. For Example:
```python
await left_motor.go_for(rpm=60, revolutions=100)
```

## Implementing a component and using the python-sdk as server
Find the Component type you wish to implement in the docs and create a new class which sub-classes that Component's BaseComponent class.

You'll need to create an implementation of each method that class has. If however you do not need or wish to implement every method,
a simple no-op method whose body consists of `pass` is sufficient to get the server up and running.
For a simple Server program, your `main()` method can look like:
```python
async def main():
    srv = Server(components=[MyCoolMotor('left_motor')])
    await srv.serve()
```

With this program running, you can connect directly via the python-sdk. Currently the python-sdk does not support authentication,
so you'll want to connect insecurely. To connect your python client application to a server running on the same machine you can use:
```python
opts = DialOptions(insecure=True)
channel = await dial_direct('localhost:9090', opts)
```

To use this custom server as part of a larger robot, you'll want to add it as a `remote` in the config for your main part.
```json
"remotes": [
    {
      "name": "my-cool-python-server",
      "insecure": true,
      "address": "localhost:9090"
    }
  ]
```
"""
