from function.encryption import *
from os import system


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
            en = encrypt(text, key)
            print("-------------------------------------------------------")
            print(en)
            print("-------------------------------------------------------")
            file.write(str(en) + " " + str(key))
            file.close()
        case 2:
            clear()
            print("Введите ключ:")
            key = int(input()) % 32
            print("Введите текст:")
            text = input()
            file = open("lab_1/decipher.txt", "w", encoding="utf-8-sig")
            dec = decipher(text, key)
            file.write(str(dec) + " " + str(key))
            print("-------------------------------------------------------")
            print(dec)
            print("-------------------------------------------------------")
            file.close()
        case 3:
            clear()
            print("Введите текст:")
            text = input()
            decipherWithoutKey(text)
            print("-------------------------------------------------------")
            print("Перебор ключа выведен в файл searchKey.txt")
            print("-------------------------------------------------------")
        case 4:
            break
        case _:
            break

# бытьможнодельнымчеловекомидуматьокрасеногтей 27
# пушкиневгенийонегин
# коуегиаэюаигдйиаюги 27