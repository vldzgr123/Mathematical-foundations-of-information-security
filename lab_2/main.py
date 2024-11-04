from function.encryption import *
from os import system
import sys


def clear():
    system("cls||clear")


clear()
while True:
    print("1.Найти обратное числу по модулю")
    print("2.Найти решение сравнения")
    print("3.Подобрать ключ")
    print("4.Выход")
    match (int(input())):
        case 1:
            clear()
            print("Введите число:")
            num = int(input())
            print("Введите модуль:")
            mod = int(input())
            print(inverse_modular(num, mod))
            input()
        case 2:
            clear()
            print("Введите a, b и m через пробел:")
            a, b, m = input().split(" ")
            print(comparison_solution(int(a), int(b), int(m)))
            input()
        case 3:
            clear()
            print("Введите текст:")
            text = input()
            decipherWithoutKey(text)
        case 4:
            break
        case _:
            break
    clear()

# бытьможнодельнымчеловекомидуматьокрасеногтей 27
# коуегиаэюаигдйиаюги 27
