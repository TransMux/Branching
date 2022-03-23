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


def get_class_that_defined_method(meth):
    if inspect.ismethod(meth):
        print('this is a method')
        for cls in inspect.getmro(meth.__self__.__class__):
            if meth.__name__ in cls.__dict__:
                return cls
    if inspect.isfunction(meth):
        print('this is a function')
        return getattr(inspect.getmodule(meth),
                       meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
                       None)
    print('this is neither a function nor a method')
    return None  # not required since None would have been implicitly returned anyway
