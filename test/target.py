from Branching import Plugin


@Plugin
def foo(number: int):
    return number


class Foo:
    @Plugin
    def foo(self, number: int):
        return number


@Plugin
def hooked(number: int):
    return number


@hooked.before
def hooked_before(number: int):
    return {"number": number + 1}
