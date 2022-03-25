Full explanation of `three` apis provided by `Branching`

## `@Plugin`

This decorator can only be used on Class Definition.

```python
@Plugin
class Foo:
    pass
```

This decorator will patch `__getattribute__` function.

## `@before`

`before` hook support 2 mode:

- inform mode(default) : it will not change the input to the target function, just run the hook to inform.All returns
  will not be saved.
- `pipe=True` pipe mode: It will change the input to the target function. The hook must return `kwargs`.

Furthermore, all arguments on the function call will be merged in `kwargs`, simply change the value you can change the
arguments.

**Change arguments in inform mode is not recommended!**

```python
@before(target_function)  # inform
def bar(**kwargs):
    return something  # will be ignored


@before(target_function, pipe=True)  # pipe
def bar(**kwargs):
    kwargs["arg_name"] = some_value  # Change the argument as you want
    return kwargs
```

## `@after`

`after` also support the above 2 modes. In pipe mode, it will change the `result` of the target function.

different from `@before`,`result` argument must be included.

```python
@after(target_function)  # inform
def bar(result, **kwargs):
    return something  # will be ignored


@after(target_function, pipe=True)  # pipe
def bar(result, **kwargs):
    return result  # Only return the result
```