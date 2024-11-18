from function.encryption import *
from os import system
import sys
import pprint


def clear():
    system("cls||clear")


clear()
while True:
    print("1.Найти обратное числу по модулю")
    print("2.Найти решение сравнения")
    print("3.Найти решение системы сравнений")
    print("4.Получить частоту появления букв")
    print("5.Получить предположения")
    print("6.Расшифровать текст без ключа")
    print("7.Выход")
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
            print("Введите a, b и m через пробел (из выражения (ax)mode m ≡ b)):")
            a, b, m = input().split(" ")
            print(comparison_solution(int(a), int(b), int(m)))
            input()
        case 3:
            clear()
            print("Введите модуль:")
            m = input()
            print("Введите a и b через пробел (из выражения (ax + y)mod m ≡ b):")
            a, b = input().split(" ")
            print("Введите c и d через пробел (из выражения (cx + y)mod m ≡ d):")
            c, d = input().split(" ")
            print(comparison_solution_system(int(a), int(b), int(c), int(d), int(m)))
            input()
        case 4:
            clear()
            print("Введите текст:")
            text = input()
            most_pop_let, let_count, _ = frequency_analysis(text)
            print(f"Самые часто встречающихся буквы {most_pop_let}")
            print("Таблица частот")
            pprint.pprint(let_count, width=40)
            input()
        case 5:
            clear()
            print("Введите текст:")
            text = input()
            for i in range(m * (m-1)):
                hypothesis(text)
            input()
        case 6:
            clear()
            print("Введите текст:")
            text = input()
            decipher_without_key(text)
            input()
        case 7:
            break
        case _:
            break
    clear()

#ртжпещкофпакоеэкблфпэяртжфутвелвкхпяэзрафпэяэтйвечлещгтэябклзщрфбкрвкомтрцакрыуеблвешвтщэяхгвеофбкуафоаяхфоырыщэяхкщэкжкоыоцшткхжфвщшфб
#тамлесидолвиденийполнытамозареприхлынутволнынабрегпесчаныйипустойитридцатьвитязейпрекрасныхчредойизводвыходятясныхиснимидядькаихморской [(23.0, 18.0), (7.0, 18.0)]