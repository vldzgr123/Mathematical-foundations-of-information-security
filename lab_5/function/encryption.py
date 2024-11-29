from function.gets import getLet, getNum, checkLet
from math import ceil, sqrt
from random import randint
from collections import deque

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


def prime_num():
    nm = 2
    while True:
        sq = ceil(nm ** 1 / 2)
        for i in range(2, sq + 1):
            if (nm % i) == 0:
                break
        else:
            yield nm
        nm += 1
        
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
        
def factorize(num: int) -> list[int]:
    
    



# fi(n)-1
# def input_p_q():
#     while True:
#         p = int(input("Введите p: "))
#         q = int(input("Введите q: "))
#         if is_prime(p) and is_prime(q):
#             return p, q
#         else:
#             print("p или q не являются простыми")

# def inverse_modular(a: int, m: int) -> int:
#     d, x, y = gcd_ext(a, m)
#     # Если НОД != 1, числа не взаимнопростые => число a не обратимо
#     if d != 1:
#         return None
#     else:
#         return x % m

# def pow(a, n, m):
#     res = 1
#     mult = a
#     while n != 0:
#         if n % 2 == 1:
#             res = (res * mult) % m
#         mult = (mult * mult) % m
#         n //= 2
#     return res


# def get_keys(e, p, q):
#     m = (p - 1) * (q - 1)
#     if gcd_ext(e, m)[0] != 1:
#         return None
#     n = p * q
#     d = inverse_modular(e, m)
#     print(f"Открытый ключ: ({e}, {n})\nЗакрытый ключ: ({d}, {n})")
#     return (e, n), (d, n)


# def generate_e(p, q):
#     phi = (p - 1) * (q - 1)
#     while True:
#         e = randint(2, phi - 1)
#         if gcd_ext(e, phi)[0] == 1:
#             yield e


# def generate_keys(p, q):
#     res = []
#     es = generate_e(p, q)
#     for e in es:
#         print(f"Ключ №{len(res)+1}")
#         keys = get_keys(e, p, q)
#         res.append(keys)
#         if len(res) == 3:
#             yield res
#             res = []
#     print("Ключей больше нет.")


# def preprocces_text(text: str) -> str:
#     return text.upper()


# def coding_text(text: str):
#     code_text = ""
#     for let in text:
#         if checkLet(let):
#             code_text += str(getNum(let))
#     return code_text


# def split_blocks(text, n):
#     code_text = deque(text)
#     blocks = []
#     next_code = ""
#     code = ""
#     block = []
#     while True:
#         try:
#             block = code_text.popleft()
#             while True:
#                 code = code_text.popleft()
#                 block += code
#                 if int(block) > n:
#                     block = block[:-1]
#                     code_text.appendleft(code)
#                     break
#             next_code = code_text.popleft()
#             if next_code == "0":
#                 block = block[:-1]
#                 code_text.appendleft(next_code)
#                 code_text.appendleft(code)
#             else:
#                 code_text.appendleft(next_code)
#             blocks.append(int(block))
#         except:
#             if len(block) != 0:
#                 blocks.append(int(block))
#             break
#     print(f"Блоки: {blocks}")
#     return blocks


# def encrypt_text(text, e, n):
#     coded_text = coding_text(text=text)
#     preproccesed_text = preprocces_text(coded_text)
#     blocks = split_blocks(preproccesed_text, n)
#     encrypt_blocks = [pow(block, e, n) for block in blocks]
#     return encrypt_blocks


# def decipher_text(blocks, d, n):
#     decipher_blocks = "".join([str(pow(block, d, n)) for block in blocks])
#     decipher_text = ""
#     for i in range(0, len(decipher_blocks), 2):
#         try:
#             decipher_text += getLet(int(decipher_blocks[i : i + 2]))
#         except:
#             return None
#     return decipher_text


# if __name__ == "__main__":
#     # a = "Вася молодец"
#     # a = preprocces_text(a)
#     # split_blocks(a, 22213)
#     key = generate_e(103, 239)
#     print(key)
