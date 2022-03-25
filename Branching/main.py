import inspect
from collections import defaultdict
from functools import wraps


def Plugin(cls):
    # Get the original get attribute implementation
    orig_getattribute = cls.__getattribute__

    # Dict[str, List]
    cls.__before_hook__ = before_hook = defaultdict(list)
    cls.__after_hook__ = after_hook = defaultdict(list)

    # In Get Attribute Process
    def get_attribute(self, name):
        target = orig_getattribute(self, name)

        if not callable(target):
            return target

        @wraps(target)
        def actual_run_time(*args, **kwargs):
            # Inspect Target Function to Merge *args into **kwargs
            # TODO: merge arguments every time will lead to performance lost
            args_list, _, _, _, _, _, _ = inspect.getfullargspec(target)
            if args_list[0] == "self":
                args_list = args_list[1:]
            for i, arg in enumerate(args):
                kwargs[args_list[i]] = arg

            for b in before_hook[name]:
                if b["pipe"]:
                    kwargs = b["hook"](**kwargs)
                else:
                    b["hook"](**kwargs)

            result = target(**kwargs)

            for a in after_hook[name]:
                if a["pipe"]:
                    result = a["hook"](result, **kwargs)
                else:
                    a["hook"](result, **kwargs)

            return result

        return actual_run_time

    # Attach to the class and return
    cls.__getattribute__ = get_attribute

    return cls


def get_class_that_defined_method(meth):
    if inspect.ismethod(meth):
        for cls in inspect.getmro(meth.__self__.__class__):
            if meth.__name__ in cls.__dict__:
                return cls
    if inspect.isfunction(meth):
        return getattr(inspect.getmodule(meth),
                       meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
                       None)
    return None  # not required since None would have been implicitly returned anyway


def before(*args, pipe=False):
    def inner(hook):
        for target in args:
            cls = get_class_that_defined_method(target)
            cls.__before_hook__[target.__name__].append({
                "hook": hook,
                "pipe": pipe
            })

        return hook

    # returning inner function
    return inner


def after(*args, pipe=False):
    def inner(hook):
        for target in args:
            cls = get_class_that_defined_method(target)
            cls.__after_hook__[target.__name__].append({
                "hook": hook,
                "pipe": pipe
            })

        return hook

    # returning inner function
    return inner
