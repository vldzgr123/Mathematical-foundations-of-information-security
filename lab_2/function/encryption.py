from function.gets import getLet, getNum, checkLet

m = 32


# Расширенный алгоритм евклида, возращает кортеж из трех значений (НОД, коэф Безу)
def gcd_ext(a: int, b=m) -> tuple:
    # Свойство НОД(a, 0) = a  a * 1 + 0 * 0 = a
    if b == 0:
        return a, 1, 0
    # Свойство НОД(a, b) = НОД(a%b, b), при a >= b > 0
    # Проверка для условия не нужно, так как если b > a,
    # то после первой итерации числа сами поменяются местами
    d, x1, y1 = gcd_ext(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y


# Вычисление обратный элемент в кольце вычетов по заданному модулю.
def inverse_modular(a: int, m=m) -> int:
    d, x, y = gcd_ext(a, m)
    # Если НОД != 1, числа не взаимнопростые => число a не обратимо
    if d != 1:
        return None
    else:
        return x % m


# Решение сравнения вида axmodm = b
def comparison_solution(a: int, b: int, m=m) -> list:
    d = gcd_ext(a, m)[0]
    if b % d != 0:
        # Решений нет
        return None

    # По модулю m имеет d решений
    a1 = (a % m) / d
    b1 = (b % m) / d
    m1 = m / d
    a1_inv = inverse_modular(a1, m1)
    x0 = (a1_inv * b1) % m
    result = [x0]
    # Находим d решений
    for i in range(d - 1):
        result.append((result[i] + m // d) % m)
    return result


# Решение системы сравнений
def comparison_solution_system(a: int, b: int, c: int, d: int, m=m) -> str:
    A = a - c
    B = b - d
    result = comparison_solution(a=A, b=B, m=m)
    if result == None:
        return None
    return [(x, (b - (x * a)) % m) for x in result]


# Частотный анализ
def frequency_analysis(text) -> tuple:
    let_count = {}
    for let in text:
        if checkLet(let) or let == " ":
            if let in let_count:
                let_count[let] += 1
            else:
                let_count[let] = 1
    for i in let_count.keys():
        let_count[i] /= len(text)
    let_count_sorted = sorted(let_count.items(), key=lambda item: item[1], reverse=True)
    return (
        let_count_sorted[:2],
        sorted(let_count.items(), key=lambda item: item[0]),
        let_count_sorted,
    )


# Выдвижение предположений
def hypothesis(text):
    alphabet_most_frequency = "оеаитнсрмлвкдпуяызбгчйхжюшщэфцъь"
    most_pop_fir, most_pop_sec = frequency_analysis(text)[0]
    k = 1
    for i in range(0, m):
        for j in range(i + 1, m):
            res_one = comparison_solution_system(
                a=getNum(alphabet_most_frequency[i]),
                b=getNum(most_pop_fir[0]),
                c=getNum(alphabet_most_frequency[j]),
                d=getNum(most_pop_sec[0]),
                m=m,
            )
            res_two = comparison_solution_system(
                a=getNum(alphabet_most_frequency[i]),
                b=getNum(most_pop_sec[0]),
                c=getNum(alphabet_most_frequency[j]),
                d=getNum(most_pop_fir[0]),
                m=m,
            )
            if res_one == None or res_two == None:
                print(
                    f'Предположение {k}:\nЕсли буквы "{most_pop_fir[0]}" и "{most_pop_sec[0]}" шифр-текста соответствуют буквам "{alphabet_most_frequency[i]}" и "{alphabet_most_frequency[j]}" открытого текста,\nто система не разрешима, следует выдвинуть другое предположение'
                )
            else:
                print(
                    f'Предположение {k}:\nЕсли буквы "{most_pop_fir[0]}" и "{most_pop_sec[0]}" шифр-текста соответствуют буквам "{alphabet_most_frequency[i]}" и "{alphabet_most_frequency[j]}" открытого текста,\nто ключ шифрования равен либо {res_one}, либо {res_two}'
                )
                yield res_one, res_two
            k += 1


# Дешифровка симваола
def decipher_let(symb: str, key):
    new_symb = symb
    if checkLet(symb):
        a_inv = inverse_modular(key[0])
        if a_inv == None:
            return None
        new_symb = getLet((a_inv * (getNum(symb) - key[1])) % m)
    return new_symb


# Дешифровка текста с ключом
def decipher(text, key) -> str:
    text = text.lower().replace("ё", "е")
    decipher_text = ""
    for let in text:
        let = decipher_let(let, key)
        if let == None:
            return None
        decipher_text += let
    return decipher_text


# Дешифровка текста без ключа
def decipher_without_key(text):
    hyps = hypothesis(text)
    file = open("lab_2/searchKey.txt", "w", encoding="utf-8-sig")
    for hyp in hyps:
        decipher_text_fir = decipher(text, hyp[0][0])
        decipher_text_sec = decipher(text, hyp[1][0])
        if decipher_text_fir == None or decipher_text_sec == None:
            print("Расшифровать текст нельзя")
            continue
        print(
            "------------------------------------------------------------------------------"
        )
        print(f"Первый ключ: {decipher_text_fir}")
        print(f"Второй ключ: {decipher_text_sec}")
        file.write(f"{decipher_text_fir} {hyp[0]}")
        file.write(f"{decipher_text_sec} {hyp[1]}")
        print("Чтобы остановить перебор введите 1")
        print(
            "------------------------------------------------------------------------------"
        )
        inp = input()
        if inp == "1":
            break
    file.close()


if __name__ == "__main__":
    # most_pop_fir, most_pop_sec = frequency_analysis("фывфыфывфыв фыв фывф")[0]
    # print(most_pop_fir[0])
    # print(most_pop_sec)
    # print(
    #     decipher_without_key(
    #         "цжсзьбоъяьсфзкьсхфьчфжфыфясзьсицхутлрчевэлэзузстфеьсфхуяфьчфэлэкфьуиоуресиэылрсевхесзтфьчцдкыъреуафюьляфйьсихеыфхсклдгъзьсиръфевюхъолтзьфясткскстсрьфйьвиурьутурчзутвфофыев"
    #     )
    # )
    print(
        decipher_without_key(
            "ртжпещкофпакоеэкблфпэяртжфутвелвкхпяэзрафпэяэтйвечлещгтэябклзщрфбкрвкомтрцакрыуеблвешвтщэяхгвеофбкуафоаяхфоырыщэяхкщэкжкоыоцшткхжфвщшфб"
        )
    )
