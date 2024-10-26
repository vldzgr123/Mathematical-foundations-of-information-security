from function.gets import getLet, getNum, checkLet

m = 32


def encrypt(text: str, key: int) -> str:
    encryptText = ""
    for let in text:
        if checkLet(let):
            encryptText += getLet((getNum(let) + key) % m)

    return encryptText


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


if __name__ == "__main__":
    print(encrypt("асудьикто", 24))
    print(decipher("шйльфавкж", 24))
