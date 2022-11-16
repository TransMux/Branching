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