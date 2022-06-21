#ax2+bx+c=0 (a≠0)
import math

while True:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = int(input("Введите число c: "))

    if a != 0:
        D = b ** 2 - 4 * a * c 
        print("D =", D )
    else:
        print("'a' не может быть = 0!")

    if D < 0:
        print("Нет корней!")
    elif D == 0:
        x = -b / 2 * a
        print(x)
    else:
        x1 = round((-b + math.sqrt(D)) / (2 * a))
        x2 = round((-b - math.sqrt(D)) / (2 * a))
    print("x1 округлён до ближайшего целого числа = ", x1)
    print("x2 округлён до ближайшего целого числа = ", x2)
    if input("Продолжим (Y/N) ") != "Y":
        break
