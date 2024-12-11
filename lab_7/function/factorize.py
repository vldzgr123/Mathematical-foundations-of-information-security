import numpy as np


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

def y_n(n, k, a, p):
    return pow_modular(a, n * k, p)


def z_n(n, a, b, p):
    return (b * pow_modular(a, n, p)) % p


def discrete_logarithm(a, b, p):
    k = sqrt(p) + 1
    for ind in yield_indexes(a, b, p, k):
        i = ind[0][0]
        j = ind[0][1]
        x = i * k - j
        if pow_modular(a, x, p) == b:
            yield x, i, j, ind[1]


def yield_indexes(a, b, p, k):
    checked = []
    n = 1
    y_n_arr = []
    z_n_arr = []
    while True:
        y = y_n(n, k, a, p)
        z = z_n(n, a, b, p)
        if y == z:
            yield (n, n), n
            checked.append((n, n))
        y_ident = [(n, ind) for ind, val in z_n_arr if y==val]
        z_ident = [(ind, n) for ind, val in y_n_arr if z==val]
        if len(y_ident) > 0:
            for indexes in y_ident:
                if indexes not in checked:
                    yield indexes, n
                    checked.append(indexes)
        if len(z_ident) > 0:
            for indexes in z_ident:
                if indexes not in checked:
                    yield indexes, n
                    checked.append(indexes)
        y_n_arr.append((n, y))
        z_n_arr.append((n, z))
        n +=1


def pow_modular(a, n, m):
    res = 1
    mult = a
    while n != 0:
        if n % 2 == 1:
            res = (res * mult) % m
        mult = (mult * mult) % m
        n //= 2
    return res


if __name__ == "__main__":
    # print(xn_2(3, 2, 667))
    print(discrete_logarithm(2, 18441, 30203))
    # print(discrete_logarithm(6, 15, 109))
