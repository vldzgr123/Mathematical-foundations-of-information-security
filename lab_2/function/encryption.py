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
    # Если НОД=1 числа не взаимнопростые => число a не обратимо
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
    a1 = a / d
    b1 = b / d
    m1 = m / d
    a1_inv = inverse_modular(a1, m1)
    x0 = (a1_inv * b1) % m
    result = [x0]
    # Находим d решений
    for i in range(d - 1):
        result.append(result[i] + m / d)
    return result


# Решение системы сравнений
def comparison_solution_system(a: int, b: int, c: int, d:int) -> str:
    
   


def decipher(text: str, key: int) -> str:
    decipherText = ""
    for let in text:
        if checkLet(let):
            decipherText += getLet((getNum(let) - key) % m)

    return decipherText


def decipherWithoutKey(text: str):
    file = open("searchKey.txt", "w", encoding="utf-8-sig")
    for i in range(32):
        decipherText = ""
        for let in text:
            if checkLet(let):
                decipherText += getLet((getNum(let) - i) % m)
        file.write(str(decipherText) + " " + str(i) + "\n")
        file

    file.close()
    
    
print((0-30 )%32)
