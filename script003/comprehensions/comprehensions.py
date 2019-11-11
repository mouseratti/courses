
squired = []

for x in range(1,11):
    squired.append(x**2)


print(squired)

squired == [x**2 for x in range(1,11)]

squired_even = [x**2 for x in range(1,11) if not x % 2]

squired_even_ternary = [x**2 if not x % 2 else 0 for x in range(1,11) ]

dict_compr = {x: x**2 for x in range(1,9)}


generator_expression = (x**x for x in range(5)) # not a tuple will be generated!!!