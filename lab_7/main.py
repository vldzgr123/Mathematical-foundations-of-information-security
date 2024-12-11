from os import system
from function.factorize import *


def clear():
    system("cls||clear")


clear()
while True:
    print("1.Выполнить дискретное логарифмирование.")
    print("2.Выход")
    match (input()):
        case "1":
            clear()
            inp = input("Введите 1, чтобы прочитать a, b, p из файла: ")
            if inp == "1":
                file = open("lab_7/input.txt", mode='r')
                a, b, p = [int(x) for x in file.read().split(" ")]
                file.close()
            else:
                a, b, p = [
                    int(x) for x in input("Введите a, b, p через пробел: ").split(" ")
                ]
            for x in discrete_logarithm(a, b, p):
                print(f"x = {x[0]}, при i, j = {x[1]}, {x[2]}, n = {x[3]}")
                inp = input("Введите 1, чтобы закончить поиск решений: ")
                if inp == "1":
                    break
            input()
            clear()
        case "2":
            clear()
            break
        case _:
            break
    clear()
