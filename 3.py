from math import *
import random



a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b ** 2 - 4 * a * c
X1 = ((-b) - sqrt(D)) / 2 * a
X2 = ((-b) + sqrt(D)) / 2 * a
if a == 0:
    print("yechimga ega emas")
elif D == 0:
    print("bitta yechimga ega" , X1)
elif D < 0:
    print("bo'w to'plam")
elif D > 0:
    print("ikkita yechimga ega" ,X1 , X2)