from function.vocab import russian_codes_to_letters, russian_letter_codes


def getNum(letter: str) -> int:
    if letter == " ":
        return 99
    return russian_letter_codes[letter.lower()] + 10


def getLet(num: int) -> str:
    if num == 99:
        return " "
    return russian_codes_to_letters[num - 10]


def checkLet(letter: str) -> bool:
    return letter.lower() in russian_letter_codes.keys() or letter == " "
