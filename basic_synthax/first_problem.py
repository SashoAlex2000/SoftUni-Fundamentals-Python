a = int(input())
b = int(input())
c = int(input())

import sys

max_number = -sys.maxsize

if a > max_number:
    max_number = a
if b > max_number:
    max_number = b
if c > max_number:
    max_number = c


print(max_number)
