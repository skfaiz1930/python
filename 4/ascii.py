#  Write a Python program to print all ASCII character with their values.

import string
for c in string.ascii_uppercase:
    print(f'ASCII for {c} is {ord(c)}')
for c in string.ascii_lowercase:
    print(f'ASCII for {c} is {ord(c)}')

