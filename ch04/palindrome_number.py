# Elements of Programming Interviews
# Chapter 04 - Primitives
# 4.9 Check if number palindrome
import math
def reverse_digits(x):
    sign = -1 if x<0 else 1
    x = abs(x)
    result = 0
    while x:
        digit = x % 10
        result *= 10
        result += digit
        x //= 10
    return sign * result

# simple way, check if x is the same as reverse(x)

def palindrome(x):
    if x<0:
        return False
    return x == reverse_digits(x)


# compare indivual digits
def palindrome_2(x):
    # first find number of digits
    num_digits = 
if __name__ == "__main__":
    print(palindrome(1232))