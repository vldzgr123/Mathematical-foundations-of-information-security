from os import system
from function.factorize import *


def clear():
    system("cls||clear")


params = [1, 1]
x0_1, x0_2 = None, None

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
            while True:
                if params == [1, 1]:
                    print("Текущая функция: f(x) = (x^2 + 1) mod m.")
                elif params[0] == 1:
                    if params[1] > 0:
                        print(f"Текущая функция: f(x) = (x^2 + {params[1]}) mod m.")
                    if params[1] < 0:
                        print(f"Текущая функция: f(x) = (x^2 - {-params[1]}) mod m.")
                    else:
                        print(f"Текущая функция: f(x) = (x^2) mod m.")
                else:
                    if params[1] > 0:
                        print(
                            f"Текущая функция: f(x) = ({params[0]} * x^2 + {params[1]}) mod m."
                        )
                    if params[1] < 0:
                        print(
                            f"Текущая функция: f(x) = ({params[0]} * x^2 - {-params[1]}) mod m."
                        )
                    else:
                        print(f"Текущая функция: f(x) = ({params[0]} * x^2) mod m.")
                print(f"Текущие начальные значения: x0_1, x0_2 = {x0_1}, {x0_2}.")
                print(f"m = {m}.")
                print("Выберите дальнейшее действие:")
                print(
                    f"1. Начать поиск.\n2. Указать другие начальные значения.\n3. Указать параметры для функции ((Ax^2 + B) mod m) и выбрать новые начальные значения.\n4. Выйти в меню."
                )
                match (input()):
                    case "1":
                        clear()
                        mults = factorize_ro(m, x0_1, x0_2, params)
                        if mults != None:
                            print(
                                f"На {mults[1]} шаге алгоритма получено значение d_{mults[1]} = {mults[0][0]}\nОтвет: {m} = {mults[0][0]} * {mults[0][1]}"
                            )
                        else:
                            print(
                                "Данное m простое или не подходит функции и начальные значения."
                            )
                        input()
                        clear()
                    case "2":
                        clear()
                        x0_1, x0_2 = [
                            int(x)
                            for x in input("Введите x0_1 и x0_2 через пробел: ").split(
                                " "
                            )
                        ]
                        clear()
                    case "3":
                        clear()
                        params = [
                            int(x)
                            for x in input(
                                "Укажите A и B через пробел ((Ax^2 + B) mod m): "
                            ).split(" ")
                        ]
                        x0_1, x0_2 = [
                            int(x)
                            for x in input("Введите x0_1 и x0_2 через пробел: ").split(
                                " "
                            )
                        ]
                        clear()
                    case "4":
                        clear()
                        break
                    case _:
                        break
        case "3":
            clear()
            break
        case _:
            break
    clear()
# 445051
