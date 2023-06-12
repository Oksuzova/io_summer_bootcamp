import math
while True:
    try:
        A, B = map(int, input().split())
        numm = int(input())
        break
    except ValueError:
        print("Введіть числа")
        continue
chara = str(input())


def task_8(n1, n2):
    print(n1 * 75 + n2 * 112)


def task_14(fo, fe):
    print((fo * 12 + fe) * 2.54)


def task_18(h, r):
    print(round(h * math.pi * r * r, 1))


def task_32(ch):
    l = [int(el) for el in str(ch)]
    summ = 0
    for i in l: summ += i
    print(summ)


def task_37(bukva):
    list1 = ["o", "u", "a", "e", "i"]
    if bukva in list1:
        print("Golosna")
    elif bukva == "y":
        print("Golosna i Prigolosna")
    else:
        print("Prigolosna")


def fizzbuzz():
    for i in range(1, 100):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# task_8(A, B)
# task_14(A, B)
# task_18(A, B)
# task_32(numm)
# task_37(chara)
# FizzBuzz()

# hello
# new changessss
