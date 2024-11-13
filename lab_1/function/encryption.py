from function.gets import getLet, getNum, checkLet


m = 32

# Метод для шифрования текста
def encrypt(text: str, key: int) -> str:
    encryptText = ""
    for let in text:
        if checkLet(let):
            encryptText += getLet((getNum(let) + key) % m)
        else:
            encryptText += let

    return encryptText

# Метод для дешифрования текста 
def decipher(text: str, key: int) -> str:
    decipherText = ""
    for let in text:
        if checkLet(let):
            decipherText += getLet((getNum(let) - key) % m)
        else:
            decipherText += let

    return decipherText

# Метод для дешифрования кейса без ключа (перебором)
def decipherWithoutKey(text: str):
    file = open("lab_1/searchKey.txt", "w", encoding="utf-8-sig")
    for key in range(32):
        decipherText = ""
        for let in text:
            if checkLet(let):
                decipherText += getLet((getNum(let) - key) % m)
            else:
                decipherText += let
        file.write(str(decipherText) + " " + str(key) + "\n")

    file.close()
