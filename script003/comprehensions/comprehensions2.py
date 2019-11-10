from string import ascii_letters
import random

STRING_LENGTH = 15

random_strings = [''.join(random.choice(ascii_letters)for x in range(STRING_LENGTH)) for y in range(4)]