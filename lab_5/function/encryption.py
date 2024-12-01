from function.gets import getLet, getNum, checkLet
from math import sqrt


file = open("lab_5/function/primes.txt", mode="r")
primes_file = file.readline()
file.close()


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


def prime_iterator():
    for prime in primes_file.split(" "):
        yield int(prime)


def q_iterator(n):
    q = [1, []]
    n_sqrt = sqrt(n)
    for p in prime_iterator():
        q[0] *= p
        q[1].append(p)
        if p * q[0] >= n_sqrt or len(q[1]) == 3:
            yield q
            q = [1, []]


def fill_dict_primes(mults: dict, primes):
    for prime in primes:
        if prime not in mults.keys():
            mults[prime] = 0
    return mults


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


def factorize(n: int) -> dict:
    mults = {}
    for q in q_iterator(n):
        mults = fill_dict_primes(mults, q[1])
        while gcd_ext(q[0], n)[0] != 1:
            d = gcd_ext(q[0], n)[0]
            n /= d
            if is_prime(d):
                mults[d] += 1
            else:
                mults_simple = factorize(d)
                primes = mults_simple.keys()
                mults = fill_dict_primes(mults, primes)
                for prime in primes:
                    mults[prime] += mults_simple[prime]
        if is_prime(n):
            mults[int(n)] = 1
            break
    return {key: value for key, value in mults.items() if value != 0}


def inverse_modular(a: int, m: int) -> int:
    d, x, y = gcd_ext(a, m)
    # Если НОД != 1, числа не взаимнопростые => число a не обратимо
    if d != 1:
        return None
    else:
        return x % m


def pow(a, n, m):
    res = 1
    mult = a
    while n != 0:
        if n % 2 == 1:
            res = (res * mult) % m
        mult = (mult * mult) % m
        n //= 2
    return res


def get_keys(e, p, q):
    m = (p - 1) * (q - 1)
    if gcd_ext(e, m)[0] != 1:
        return None
    n = p * q
    d = inverse_modular(e, m)
    print(f"Открытый ключ: ({e}, {n})\nЗакрытый ключ: ({d}, {n})")
    return (e, n), (d, n)


def decipher_text(blocks, d, n):
    decipher_blocks = "".join([str(pow(block, d, n)) for block in blocks])
    print(decipher_blocks)
    decipher_text = ""
    for i in range(0, len(decipher_blocks), 2):
        try:
            decipher_text += getLet(int(decipher_blocks[i : i + 2]))
        except:
            return None
    return decipher_text


if __name__ == "__main__":
    # from sympy import primerange
    # file = open("lab_5/function/primes.txt", mode="w")
    # for prime in primerange(0, 1000):
    #     file.write(f"{prime} ")
    print(factorize(113803))
    facts = {1 : 2, 2 : 1}
    print(all(value==1 for value in facts.values()))
