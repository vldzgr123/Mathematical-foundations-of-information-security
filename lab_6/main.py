from os import system
from function.factorize import *


def clear():
    system("cls||clear")


clear()
while True:
    print("1.Факторизовать число методом квадратичного решета.")
    print("2.Факторизовать число ро-методом.")
    print("3.Выход")
    match (input()):
        case "1":
            clear()
            m = int(input("Введите m: "))
            while True:
                a, b, c = [
                    int(x) for x in input("Введите a, b, c через пробел: ").split(" ")
                ]
                if (
                    gcd_ext(a, b)[0] != 1
                    or gcd_ext(a, c)[0] != 1
                    or gcd_ext(b, c)[0] != 1
                ):
                    print("Введены некорректные значения")
                    continue
                break
            mults = factorize_sieve(m, a, b, c)
            if mults == None:
                print("Данное m простое")
            else:
                print(f"Ответ: {m} = {mults[0]} * {mults[1]}")
            input()
            clear()
        case "2":
            clear()
            m = int(input("Введите m: "))
            x0_1, x0_2 = [
                int(x) for x in input("Введите x0_1 и x0_2 через пробел: ").split(" ")
            ]
            mults = factorize_ro(m, x0_1, x0_2)
            if mults != None:
                print(
                    f"На {mults[1]} шаге алгоритма получено значение d{mults[1]}={mults[0][0]}\nОтвет: {m} = {mults[0][0]} * {mults[0][1]}"
                )
            else:
                print("Данное m простое")
            input()
            clear()
        case "3":
            clear()
            break
        case _:
            break
    clear()
# with open(path_key, "w"):
#     pass
# 103 239
