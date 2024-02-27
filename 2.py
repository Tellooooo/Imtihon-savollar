from math import *
import random


X = int(input("X = "))
Y = int(input("Y = "))
Z = int(input("Z = "))

a = X + Y + Z / 2
b = X * Y * Z

S = min(a,b)
print(S ** 2 + 1)