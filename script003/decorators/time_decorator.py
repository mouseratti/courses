# from datetime import datetime
import time

def time_decorator(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"{fn.__name__} work time is  {end - start}")
        return result
    return wrapper

@time_decorator
def my_function(*args, **kwargs):
    pass
    print(args, kwargs)
    time.sleep(5)
    return


if __name__ == '__main__':
    my_function()