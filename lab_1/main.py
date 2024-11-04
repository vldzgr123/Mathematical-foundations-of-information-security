from function.encryption import *
from os import system
import sys


def clear():
    system("cls||clear")


clear()
while True:
    print("1.Шифровать")
    print("2.Расшифровать")
    print("3.Подобрать ключ")
    print("4.Выход")
    match (int(input())):
        case 1:
            clear()
            print("Введите ключ:")
            key = int(input()) % 32
            print("Введите текст:")
            text = input()
            file = open("lab_1/encrypt.txt", "w", encoding="utf-8-sig")
            file.write(str(encrypt(text, key)) + " " + str(key))
            file.close()
        case 2:
            clear()
            print("Введите ключ:")
            key = int(input()) % 32
            print("Введите текст:")
            text = input()
            file = open("lab_1/decipher.txt", "w", encoding="utf-8-sig")
            file.write(str(decipher(text, key)) + " " + str(key))
            file.close()
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