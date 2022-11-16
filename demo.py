def plugin(func):
    def inner(*args, **kwargs):
        print(args, kwargs)
        return func(*args, **kwargs)

    return inner


class Foo:
    @plugin
    def bar(self, a):
        print(a)


Foo().bar(a=1)
