string_a = 'string'
string_b = "string with spaces"
multiline = '''
string 
with 
multiple
lines
'''


# most of strings are interned and won't be cleaned by GC
string_the_same_as_a = 'string'
print(string_a is string_the_same_as_a)


a = '5'
a + a, a * a

space = ' '
space.join("space")
space.upper()
space.startswith('s')
space.split()
space.count()
space.find('1')

' ' in space
########## String formatting
## .format
placeholdered_without_any_order = "{} is {} but not {}"
placeholdered_without_any_order.format(1, 'number', None)

placeholdered_indexed = "{1} is not {0} but {1}"
placeholdered_indexed.format(type(5), "sun", 'word')

placeholdered_named = "{TAG2} equals to {TAG1}"
placeholdered_named.format(TAG1=5, TAG2=5.0)

with_brackets = "{{}}"
with_brackets.format()


## f-strings
#my_integer = 1.0
a = f'{my_integer}'
print(a)



