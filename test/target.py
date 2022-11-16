from Branching import Plugin


@Plugin
def foo(number: int):
    return number


class Foo:
    @Plugin
    def foo(self, number: int):
        return number
