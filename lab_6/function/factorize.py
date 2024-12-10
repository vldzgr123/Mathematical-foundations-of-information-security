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


def factorize(num: int, a: int, b: int, c: int):
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
        indexes = [key for key, value in enumerate(sum_sieves) if value==3]
        for index in indexes:
            n = int(k + index)
            x = n
            z = pow(x, 2) - num
            if z==0:
                continue
            y = sqrt(z)
            if pow(y, 2) == z:
                p = x + y
                q = x - y
                return p, q
        k += max_len_sieves


# def gcd_ext(a: int, b: int) -> tuple:
#     # Свойство НОД(a, 0) = a  a * 1 + 0 * 0 = a
#     if b == 0:
#         return a, 1, 0
#     # Свойство НОД(a, b) = НОД(a%b, b), при a >= b > 0
#     # Проверка для условия не нужно, так как если b > a,
#     # то после первой итерации числа сами поменяются местами
#     d, x1, y1 = gcd_ext(b, a % b)
#     x = y1
#     y = x1 - (a // b) * y1
#     return d, x, y


# def prime_iterator():
#     for prime in primes_file.split(" "):
#         yield int(prime)


# def q_iterator(n):
#     q = [1, []]
#     n_sqrt = sqrt(n)
#     for p in prime_iterator():
#         q[0] *= p
#         q[1].append(p)
#         if p * q[0] >= n_sqrt or len(q[1]) == 3:
#             yield q
#             q = [1, []]


# def fill_dict_primes(mults: dict, primes):
#     for prime in primes:
#         if prime not in mults.keys():
#             mults[prime] = 0
#     return mults


# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True


# def factorize(n: int) -> dict:
#     mults = {}
#     for q in q_iterator(n):
#         mults = fill_dict_primes(mults, q[1])
#         while gcd_ext(q[0], n)[0] != 1:
#             d = gcd_ext(q[0], n)[0]
#             n /= d
#             if is_prime(d):
#                 mults[d] += 1
#             else:
#                 mults_simple = factorize(d)
#                 primes = mults_simple.keys()
#                 mults = fill_dict_primes(mults, primes)
#                 for prime in primes:
#                     mults[prime] += mults_simple[prime]
#         if is_prime(n):
#             mults[int(n)] = 1
#             break
#     return {key: value for key, value in mults.items() if value != 0}


# def inverse_modular(a: int, m: int) -> int:
#     d, x, y = gcd_ext(a, m)
#     # Если НОД != 1, числа не взаимнопростые => число a не обратимо
#     if d != 1:
#         return None
#     else:
#         return x % m


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


# def get_keys(e, p, q):
#     m = (p - 1) * (q - 1)
#     if gcd_ext(e, m)[0] != 1:
#         return None
#     n = p * q
#     d = inverse_modular(e, m)
#     print(f"Открытый ключ: ({e}, {n})\nЗакрытый ключ: ({d}, {n})")
#     return (e, n), (d, n)


# def decipher_text(blocks, d, n):
#     decipher_blocks = "".join([str(pow(block, d, n)) for block in blocks])
#     print(decipher_blocks)
#     decipher_text = ""
#     for i in range(0, len(decipher_blocks), 2):
#         try:
#             decipher_text += getLet(int(decipher_blocks[i : i + 2]))
#         except:
#             return None
#     return decipher_text


if __name__ == "__main__":
    # from sympy import primerange
    # file = open("lab_5/function/primes.txt", mode="w")
    # for prime in primerange(0, 1000):
    #     file.write(f"{prime} ")
    print(factorize(num=667, a=3, b=5, c=7))
