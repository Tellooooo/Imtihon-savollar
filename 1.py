from math import *
import random


X = int(input("X = "))
Y = int(input("Y = "))
Z = int(input("Z = "))

a = X + Y + Z
b = X * Y * Z
if a > b:
    print("a katta")
else:
    print("b katta")