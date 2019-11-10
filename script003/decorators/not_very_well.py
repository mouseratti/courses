def cacher(fn):
    cache = tuple()
    def wrapper(x):
        if x not in cache: cache[x] = fn(x)
        return cache[x]
    return wrapper



if __name__ == '__main__':
    from time import sleep

    @cacher
    def timed(x):
        sleep(7)
        return x**x

    print(timed(5), timed(5))
