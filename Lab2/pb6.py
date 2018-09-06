n = int(input())

f0 = 1
f1 = 1

while f1 <= n:
    aux = f1
    f1 = f1 + f0
    f0 = aux

print(f1)