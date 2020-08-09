from collections import Counter
import typing

def constructable(l:str, m:str) -> bool:
    chars_letter = Counter(l)

    for c in m:
        if c in chars_letter:
            chars_letter[c] -= 1
            if chars_letter[c] == 0:
                del chars_letter[c]
                # check if all letters are used
                if not chars_letter:
                    return True
    return not chars_letter

def pythonic_constructable(l:str, m:str) -> bool:
    return (not Counter(l) - Counter(m))
if __name__ == "__main__":
    letter = "bert"
    magazine = "hirbart"
    print(constructable(letter,magazine))
    print(pythonic_constructable(letter,magazine))