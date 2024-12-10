import numpy as np
  
def get_sieve(mod: int, num: int) -> np.ndarray:
    siave = np.zeros((3, mod), dtype=np.int32)
    siave[0] = np.array([pow_modular(x, 2, mod) for x in range(len(siave[0]))])
    siave[1] = np.array(
        [(pow_modular(x, 2, mod) - num) % mod for x in range(len(siave[0]))]
    )
    siave[2] = np.array([1 if x in siave[0] else 0 for x in siave[1]])
    return siave


def move_sieve(sieve_s: np.ndarray, num: int, m: int) -> np.ndarray:
    index = (sqrt(num) + 1) % m
    return np.concatenate([sieve_s[index:], sieve_s[:index]])


def sqrt(m: int):
    if m <= 0:
        return None
    x = m
    while True:
        y = int(int(x + int(m / x)) >> 1)
        if y < x:
            x = y
        else:
            return x


def get_interval(m) -> np.ndarray:
    return np.array([int(sqrt(m) + 1), int((m + 1) / 2)])


def yield_sieve(sieves, max_len, max_len_sieves):
    k = 0
    while True:
        sieves = [
            (
                np.concatenate([np.array(sieve), np.array(sieve)])
                if len(sieve) < max_len_sieves * (k + 1)
                else sieve
            )
            for sieve in sieves
        ]
        if len(min(sieves, key=len)) >= max_len_sieves:
            if max_len_sieves * (k + 1) >= max_len:
                return [
                    sieve[max_len_sieves * k : max_len_sieves * (k + 1)]
                    for sieve in sieves
                ]
            yield [
                sieve[max_len_sieves * k : max_len_sieves * (k + 1)] for sieve in sieves
            ]
            k += 1


def factorize_sieve(num: int, a: int, b: int, c: int):
    sieve_a = move_sieve(get_sieve(a, num)[2], num, a)
    sieve_b = move_sieve(get_sieve(b, num)[2], num, b)
    sieve_c = move_sieve(get_sieve(c, num)[2], num, c)
    sieves = [sieve_a, sieve_b, sieve_c]
    max_len_sieves = len(max(sieves, key=len))
    interval = get_interval(num)
    iterator_sieves = yield_sieve(sieves, interval[1] - interval[0] + 1, max_len_sieves)
    k = interval[0]
    for sieves in iterator_sieves:
        sum_sieves = sum(sieves)
        indexes = [key for key, value in enumerate(sum_sieves) if value == 3]
        for index in indexes:
            n = int(k + index)
            x = n
            z = pow(x, 2) - num
            if z == 0:
                continue
            y = sqrt(z)
            if pow(y, 2) == z:
                p = x + y
                q = x - y
                return p, q
        k += max_len_sieves


def f(x, m):
    return (pow_modular(x, 2, m) + 1) % m


def xn_1(n, x0, m):
    if n == 0:
        return x0
    else:
        return f(xn_1(n - 1, x0, m), m)


def xn_2(n, x0, m):
    if n == 0:
        return x0
    else:
        return f(f(xn_2(n - 1, x0, m), m), m)


def factorize_ro(m, x0_1, x0_2):
    n = 0
    while True:
        xk_1 = xn_1(n, x0_1, m)
        xk_2 = xn_2(n, x0_2, m)
        ak = abs(xk_1 - xk_2)
        dk = gcd_ext(ak, m)[0]
        print(f"Шаг №{n}: xn_1={xk_1}, xn_2={xk_2}, an={ak}, bn={dk}.")
        if dk > 1 and dk < m:
            return (dk, m // dk), n
        n += 1

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


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


def pow_modular(a, n, m):
    res = 1
    mult = a
    while n != 0:
        if n % 2 == 1:
            res = (res * mult) % m
        mult = (mult * mult) % m
        n //= 2
    return res


def pow(a, n):
    res = 1
    mult = a
    while n != 0:
        if n % 2 == 1:
            res = res * mult
        mult = mult * mult
        n //= 2
    return res


if __name__ == "__main__":
    # print(xn_2(3, 2, 667))
    factorize_ro(667, 2, 2)
    # pow_modular(101, 2, 667)
    # pow_modular(125, 2, 667)
    # print(pow(101,2)%667)
    # print(pow_modular(101,2,667))
