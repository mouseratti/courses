
def my_function(arg1):
    result = arg1 * arg1
    return


def my_function2(arg1, arg2):
    """:returns float"""
    if arg1 == 0 : return
    # if arg1 == 0 : return None
    return arg1 / arg2


def with_optional_param(required, nnn=0):
    return required ** nnn