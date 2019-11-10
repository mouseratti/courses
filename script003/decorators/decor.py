# https://www.datacamp.com/community/tutorials/decorators-python
# from functools import wraps


def not_decorated_function(*args, **kwargs):
    pass
    print(f"args are {args}, {type(args)}")
    print(f"kwargs are {kwargs}, {type(kwargs)}")
    return



def decorator(fn):
    # @wraps(fn)
    def wrapper(*args, **kwargs):
        """docstring for wrapper"""
        print("wrapper is starting!")
        result = fn(*args, **kwargs)
        print("wrapper is finished")
        return result
    return wrapper

def not_decorated(example_arg1=0):
    """docstring for this function"""
    print("this is example arg1")
    return 1


another_name_for_not_decorated = not_decorated

decorated = decorator(not_decorated)

# not_decorated = decorator(not_decorated)

@decorator
def decorated2(example_arg1=''):
    """docstring for this function"""
    print("this is example arg1")
    return(1)


if __name__ == '__main__':
    a, b = decorated(), decorated2()
    print(f"results are {a}, {b}")