from os import system
from function.encryption import *
import tempfile


def clear():
    system("cls||clear")


path_key = "lab_4/keys.txt"
p = None
q = None
keys = None
clear()
p, q = input_p_q()
clear()
while True:
    print(f"p = {p}, q = {q}\nТекущие открытый и закрытый ключи соответственно: {keys}")
    print(
        "------------------------------------------------------------------------------------"
    )
    print("1.Заменить p и q")
    print("2.Генерация ключей")
    print("3.Выбрать ключ из сохраненных")
    print("4.Зашифровать текст")
    print("5.Расшифровать текст")
    print("6.Выход")
    match (input()):
        case "1":
            clear()
            p, q = input_p_q()
            clear()
        case "2":
            clear()
            file = open(path_key, mode="a")
            e = input(
                "Введите e (если хотите, чтобы е сгенерировалось - оставьте строку пустой): "
            )
            if e != "":
                new_keys = get_keys(int(e), p, q)
                if new_keys == None:
                    print("Это e не удовлетворяет условию")
                    input()
                    continue
                keys = new_keys
                file.write(str(keys))
                file.write("\n")
            else:
                inp = int()
                gens = generate_keys(p, q)
                for gen in gens:
                    inp = input(
                        "Выберите номер ключа (если хотите продолжить оставьте строку пустой): "
                    )
                    if inp != "":
                        keys = gen[int(inp) - 1]
                        file.write(str(keys) + "\n")
                        break
            file.close()
            clear()
        case "3":
            clear()
            file = open(path_key, mode="r")
            file.seek(0)
            lines = file.readlines()
            for i in range(len(lines)):
                print(f"{i+1}. {lines[i]}")
            num = input("Выберите ключей: ")
            if num == "" or len(lines) - 1 < int(num) - 1:
                continue
            keys = lines[int(num) - 1]
            clear()
        case "4":
            clear()
            if keys == None:
                print("Отсутствуют ключ")
                input()
                continue
            text = input("Введите текст: ")
            print("Зашифрованный текст:")
            print(encrypt_text(text=text, e=keys[0][0], n=keys[0][1]))
            input()
            clear()
        case "5":
            clear()
            if keys == None:
                print("Отсутствуют ключ")
                input()
                continue
            text = input("Введите текст: ")
            print("Расшифрованный текст:")
            print(decipher_text(text=text, d=keys[1][0], n=keys[1][1]).upper())
            input()
            clear()
        case "6":
            break
        case _:
            break
    clear()
with open(path_key, "w"):
    pass
