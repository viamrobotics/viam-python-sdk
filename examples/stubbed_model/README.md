# stub_model

This is an example using the `stub_model` class decorator, a helper for creating Viam modules.

`stub_model` adds stub functions for unimplemented abstract methods so that your class can be instantiated. This is a helper for development, so you can gradually fill in a new model implementation rather than doing it all at once before you can test. Avoid using this in modules that are published to the registry unless you really understand the maintainability tradeoffs.

Take an example Motor class:

```python
@stub_model
class MyMotor(Motor, EasyResource):
    MODEL = "org:examples:stubbed-motor"
```

Without the stub_model decorator, this would fail on instantiation with an error like:

```
TypeError: Can't instantiate abstract class MyMotor with abstract methods get_position, get_properties, go_for, go_to, is_moving, is_powered, reset_zero_position, set_power, set_rpm, stop
```

## Instructions

Follow the instructions in the [easy_resource example](../easy_resource).
