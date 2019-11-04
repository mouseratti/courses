def my_function(arg1):
    return arg1 * arg1


def my_function2(arg1, arg2):
    """:returns float"""
    if arg1 == 0 : return
    # if arg1 == 0 : return None
    return arg1 / arg2



def with_optional_param(required, optional=None):
    if optional is None:
        return required ** 0
    return required ** optional