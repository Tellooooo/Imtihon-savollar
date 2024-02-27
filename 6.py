N = int(input("N = "))
a0 = 1
for i in range(1 , N + 1):
    S = i * a0 + 1 / i
    a0 = S
print(S)


