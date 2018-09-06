appearances = [0] * 11

number = int(input())

while number > 0:
    appearances[number%10] = appearances[number%10] + 1
    number //=10

for i in range(1,10):
    if appearances[i] > 0:
        print(i,end="");
        appearances[i] = appearances[i] - 1
        while appearances[0] > 0:
            print(0,end="")
            appearances[0] = appearances[0] - 1
        break

for i in range(1,10):
    while appearances[i] > 0:
        print(i,end="")
        appearances[i] = appearances[i] - 1