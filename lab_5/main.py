from os import system
from function.encryption import *
import tempfile


def clear():
    system("cls||clear")


path_key = "lab_4/keys.txt"
p = None
q = None
keys = None
while True:
    print(f"p = {p}, q = {q}\nТекущие открытый и закрытый ключи соответственно: {keys}")
    print(
        "------------------------------------------------------------------------------------"
    )
    print("1.Факторизовать число")
    print("2.Определение закрытого ключа")
    print("3.Расшифровать текст")
    print("4.Выход")
    match (input()):
        case "1":
            clear()
            num = int(input("Введите число: "))
            if is_prime(num):
                print("Это число простое")
            else:
                facts = factorize(num)
                print(facts)
            input()
            clear()
        case "2":
            clear()
            inp = input("Введите 1, чтобы прочитать (e, n) из файла: ")
            if inp == "1":
                file = open("lab_5/key.txt", mode="r")
                e, n = [int(x) for x in file.readline().split(" ")]
                facts = factorize(n)
                p, q = facts.keys()
                file.close()
            else:
                while True:
                    clear()
                    n = int(input("Введите n: "))
                    facts = factorize(n)
                    if len(facts) != 2 and all(value==1 for value in facts.values()):
                        print("Некорректное n.")
                        continue
                    p, q = facts.keys()
                    break
                while True:
                    e = int(input("Введите e: "))
                    if gcd_ext(e, (p-1)*(q-1))[0] != 1:
                        print("Некорректное e.")
                        continue
                    break
            keys = get_keys(e, p, q)
            input()
            clear()
        case "3":
            clear()
            if keys == None:
                print("Отсутствует ключ")
                input()
                continue
            inp = input("Введите, 1 чтобы прочитать блоки записанные в файл: ")
            file = open("lab_5/block.txt", "r")
            if inp == '1':
                text = file.readline()
            else:
                text = input("Введите блоки через пробел: ")
            text = text.split(" ")
            try:
                print("Расшифрованный текст:")
                print(
                    decipher_text(
                        blocks=[int(x) for x in text], d=keys[1][0], n=p * q
                    ).upper()
                )
            except:
                print("Данный блок не удается интерпретировать")
            input()
            file.close()
            clear()
        case "4":
            break
        case _:
            break
    clear()
# with open(path_key, "w"):
#     pass
# 103 239
