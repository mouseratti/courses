# https://www.w3schools.com/python/python_operators.asp
a_int = 5
a_float = 5.0
b_float = 5 / 2
b_int = 5 // 2
with_remainder = 5 % 2
5 * 2, 5 ** 2


# https://dzone.com/articles/never-use-float-and-double-for-monetary-calculatio
y = 0
for x in range(100): y+= 0.1


y = 0
import decimal
for x in range(100): y+= decimal.Decimal("0.10")

y.bit_length()
y.bit_length == y.bit_length()

y = 5.0
y.is_integer()

