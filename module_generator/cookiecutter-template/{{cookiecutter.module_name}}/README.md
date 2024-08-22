# [{{cookiecutter.module_name}} Module](https://app.viam.com/module/viam/{{cookiecutter.module_name}})

This [module](https://docs.viam.com/registry/#modular-resources) implements the [{{cookiecutter.__api}} API](https://python.viam.dev/autoapi/viam/{{cookiecutter.__resource_type}}s/{{cookiecutter.__resource}}/#api) in a `{{cookiecutter.model_name}}` model.

## Configure your {{cookiecutter.module_name}} {{cookiecutter.__resource.replace('_', ' ')}}

Navigate to the [**CONFIGURE** tab](https://docs.viam.com/configure/) of your [machine](https://docs.viam.com/fleet/machines/) in [the Viam app](https://app.viam.com/).
[Add {{cookiecutter.__resource.replace('_', ' ')}} / {{cookiecutter.module_name}} to your machine](https://docs.viam.com/configure/#{{cookiecutter.__resource_type}}s).

On the new component panel, copy and paste the following attribute template into your {{cookiecutter.__resource.replace('_', ' ')}}’s attributes field:

```json
{
  <INSERT SAMPLE ATTRIBUTES>
}
```

> [!NOTE]
> For more information, see [Configure a Machine](https://docs.viam.com/configure/).

### Attributes

The following attributes are available for `{{cookiecutter.__model}}` {{cookiecutter.__resource.replace('_', ' ')}}s:

| Name    | Type   | Required?    | Description |
| ------- | ------ | ------------ | ----------- |
| `todo1` | string | **Required** | TODO        |
| `todo2` | string | Optional     | TODO        |

### Example configuration

```json
{
  <INSERT SAMPLE CONFIGURATION(S)>
}
```

### Next steps

- To test your {{cookiecutter.__resource.replace('_', ' ')}}, go to the [**CONTROL** tab](https://docs.viam.com/fleet/control/).
- To write code against your {{cookiecutter.__resource.replace('_', ' ')}}, use one of the [available SDKs](https://docs.viam.com/sdks/).
- To view examples using a {{cookiecutter.__resource.replace('_', ' ')}} {{cookiecutter.__resource_type}}, explore [these tutorials](https://docs.viam.com/tutorials/).
