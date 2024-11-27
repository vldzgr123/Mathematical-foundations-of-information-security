from function.gets import getLet, getNum, checkLet

def gcd_ext(a: int, b: int) -> tuple:
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

def inverse_modular(a: int, m: int) -> int:
    d, x, y = gcd_ext(a, m)
    # Если НОД != 1, числа не взаимнопростые => число a не обратимо
    if d != 1:
        return None
    else:
        return x % m

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
        return True 

def generate_keys(p: int, q: int):
    if not (is_prime(p) or is_prime(q)): return None
    n = p * q
    fin = (p - 1) * (q - 1)
    e = 1
    keys = []
    while len(keys) < 3:
        d = inverse_modular(e, fin)
        if d != None:
            keys.append((e, n))
            keys.append((d, n))
        e += 1
            
    

