

def buggy_range(finish, start=0, step=1):
    if start != 0: finish,start = start,finish
    while start != finish:
        return start
        start += step

def simple_range(finish, start=0, step=1):
    if start != 0: finish,start = start,finish
    result = []
    while start != finish:
        result.append(start)
        start += step
    return result

# def generated_range(finish, start=0, step=1):
#     if start != 0: finish,start = start,finish
#     while start != finish:
#         yield start
#         start += step


def simple_gen():
    yield 1
    yield 2
    yield 3
    yield 4


def fibonacci_gen(n):
    counter = 1
    current, next_pos = 1, 1
    while counter <= n:
        yield current
        current, next_pos = next_pos, next_pos + current
        counter += 1


def square_gen():
    for x in range(6):
        yield x**2

g1 = square_gen()
g2 = (x**2 for x in range(6))