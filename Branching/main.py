from functools import partial


class Wrapper:
    def __init__(self, function):
        self.function = function
        self._before = []
        self._after = []

    def __call__(self, *args, **kwargs):
        kwargs.update(zip(self.function.__code__.co_varnames, args))

        for before_function in self._before:
            updates = before_function(**kwargs)
            kwargs.update(updates)

        result = self.function(**kwargs)

        for after_function in self._after:
            result = after_function(result, **kwargs)

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

    wrapper = Wrapper(function)

    return wrapper


if __name__ == '__main__':
    @Plugin
    def target(number: int):
        return number


    @target.before
    def before(number: int):
        return {"number": number + 1}


    assert target(1) == 2
