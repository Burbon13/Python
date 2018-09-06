appearances = [0] * 11

number1 = int(input())
number2 = int(input())

while number1 > 0:
    appearances[number1%10] = appearances[number1%10] + 1
    number1 //= 10

truth = True

while number2 > 0 and truth == True:
    if appearances[number2%10] == 0 :
        truth = False
    number2 //=10

print(truth)

