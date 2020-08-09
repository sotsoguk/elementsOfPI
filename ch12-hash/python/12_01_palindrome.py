from collections import Counter
import typing

def palindromic(s:str) -> bool:
    return sum(v % 2 for v in Counter(s).values()) <= 1

if __name__ == "__main__":
    test = "edified"
    print(palindromic(test))
