import random



N = int(input("N = "))
A = []
for i in range (1 , N + 1):
    Z = random.randint(1 , N + 1)
    A.append(Z)
print(A)