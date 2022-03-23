import inspect
from collections import defaultdict
from functools import wraps


def Plugin(cls):
    # Get the original get attribute implementation
    orig_getattribute = cls.__getattribute__

    # Dict[str, List]
    cls.__before_hook__ = before_hook = defaultdict(list)
    cls.__after_hook__ = after_hook = defaultdict(list)

    # Make a new definition
    def run_with_hook(self, name):
        print(name)

        for b in before_hook[name]:
            b(self)

        result = orig_getattribute(self, name)

        for a in after_hook[name]:
            a(self, result)

        return result

    # Attach to the class and return
    cls.__getattribute__ = run_with_hook

    return cls
