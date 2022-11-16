<h1 align="center">Branching</h1>

A Framework That Provides Easy To Use Plugin Integration.

✅ Any Issue or PR or Suggestions are highly welcomed !

### Features

- Add Plugin Architecture by simply decorate it with `@Plugin`.
- Full Support for `@foo.before` and `@foo.after` hook of any function.
- Using with little changes to your code.
- Very easy to use. Only three apis (And they are stable!).
    - `@Plugin` defines the target hook function / method.
    - `@foo.before` define a hook that run before the method.
    - `@foo.after` define a hook that run after the method.

### Cons

- `before` and `after`, `remove` and `mount` will have NO auto completion support.

### Installation

```
pip install branching
```

### demo

```python
from Branching import Plugin


@Plugin
def target(number: int):
    return number


@target.before
def before(number: int):
    return {"number": number + 1}


assert target(1) == 2

before.remove()

assert target(1) == 1

before.mount()

assert target(1) == 2
```
