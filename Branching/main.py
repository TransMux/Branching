from functools import partial, wraps
from typing import Callable


def call_function(target: Callable, arguments: dict, result=None):
    # only pass the needed arguments to the function
    arguments = {key: value for key, value in arguments.items() if key in target.__code__.co_varnames}
    if result is not None and "_result" in target.__code__.co_varnames:
        arguments["_result"] = result
    return target(**arguments)


class Wrapper:
    def __init__(self, function, in_class=False):
        self.function = function
        self._before = []
        self._after = []
        self.in_class = in_class

    def __call__(self, *args, **kwargs):
        var_names = self.function.__code__.co_varnames

        kwargs.update(zip(var_names, args))

        for before_function in self._before:
            updates = call_function(before_function, kwargs)
            kwargs.update(updates)

        result = self.function(**kwargs)

        for after_function in self._after:
            result = call_function(after_function, kwargs, result=result)

        return result

    def before(self, function):
        self._before.append(function)
        return self

    def after(self, function):
        self._after.append(function)
        return self


def Plugin(function=None):
    if function is None:
        return partial(Plugin, function)

    # whether function is defined inside class
    if function.__name__ != function.__qualname__:
        wrapper = Wrapper(function, in_class=True)
    else:
        wrapper = Wrapper(function)

    @wraps(function)
    def inner(*args, **kwargs):
        return wrapper(*args, **kwargs)

    inner.before = wrapper.before
    inner.after = wrapper.after

    return inner


if __name__ == '__main__':
    @Plugin
    def target(number: int):
        return number


    @target.before
    def before(number: int):
        return {"number": number + 1}


    assert target(1) == 2
