

def square(a):
    return a**2

def summary(a): return a + a


def function_acceptor(fn, arg):
    return fn(arg)


if __name__ == '__main__':
    decision = ""
    while decision not in ("square", "summary"):
        decision = input("input square or summary: ")

    argument = int(input("input argument: "))
    if decision == "square":
        func = square
        print(function_acceptor(func, argument))
    else:
        func = summary
        # func = lambda x: x + x
        print(function_acceptor(func, argument))
        # print(function_acceptor(lambda x: x + x, argument))

