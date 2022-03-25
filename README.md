<h1 align="center">Branching</h1>

A Framework That Provides Easy To Use Plugin Integration.


✅ Any Issue or PR or Suggestions are highly welcomed !


### Features

- Add Plugin Architecture by simply decorate it with `@Plugin`.
- Full Support for `@before` and `@after` hook of any function.
- Using with little changes to your code.
- Code Auto Complete is On.
- Veryyyyy easy to use. Only three apis (And they are stable!).
    - `@Plugin` defines the target hook class.
    - `@before` define a hook that run before the method.
    - `@after` define a hook that run after the method.
- ~~No SideEffect.~~ Using this library, the hooked instance can only be used once. See Warning Section for detail.

### Installation

```
pip install branching
```

### demo

```python
from Branching import Plugin, before, after


@Plugin  # Add this decorator to provide Plugin Architecture
class Foo:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        print("Order 2: Foo.x ", self.x)
        self.hello()

    def hello(self):
        print("Order 4: In Plugin Hello", self.x)


# You can hook on more than one functions at a time
@before(Foo.get_x, Foo.hello)
def hello(*args):
    print("Order 1/3: Before Hook")


@after(Foo.get_x)
def hello(*args):
    print("Order 5: After Hook")


# Done! Lets Test it
a = Foo(123)
a.get_x()
```

And the output would be:

```text
Order 1/3: Before Hook
Order 2: Foo.x  123
Order 1/3: Before Hook
Order 4: In Plugin Hello 123
Order 5: After Hook
```

💡 It works!

## Warning

You can also hook on the instance like `a.get_x` above. The effect is the same by doing so, but there are side effects:
another instance will also trigger the hooks when getting the attributes.

This is an Unsolved problem and any suggestions are welcomed!

As an example of above:
```python
a = Foo(123)
b = Foo(456)

a.get_x()
b.get_x()
```
this will give:

```text
Order 1/3: Before Hook  // <- a.get_x()
Order 2: Foo.x  123
Order 4: In Plugin Hello 123
Order 5: After Hook
Order 1/3: Before Hook // <- b.get_x()
Order 2: Foo.x  456
Order 4: In Plugin Hello 456
Order 5: After Hook
```