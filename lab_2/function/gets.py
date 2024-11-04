from function.vocab import russian_codes_to_letters, russian_letter_codes

def getNum(letter: str) -> int:
        return russian_letter_codes[letter]

def getLet(num: int) -> str:
        return russian_codes_to_letters[num]

def checkLet(letter: str) -> bool:
        return letter in russian_letter_codes.keys()
