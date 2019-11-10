def function(*args, **kwargs):
    """coeff - some coefficient"""
    print(args, len(args), type(args[0]))
    print(kwargs)
    return


function(1,2,3,4,5, coeff='value1', key2=5)
# function()
# function(1)
# function(1,2)
# function(1,2,3)
# function((1,2,3,4,5,), key1='value1', key2=5)

a = 1,2,3
function(a)
function(*a)


def function2(arg1, arg2=[]):
    arg2.append(arg1)
    return arg2

# function2(3, [1])
function2(1)
function2(2)
function2(3)
