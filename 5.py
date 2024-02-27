N = int(input("N = "))
S = 0
for i in range(1 , N + 1):
    S = (i * (i + 1) * 2 * i) + S
print(S)