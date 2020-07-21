# Elements of Programming Interviews
# Chapter 04 - Primitives
# 4.8 Reverse digits

testCases = {123:321, 0:0, -8393:-3938}
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

if __name__ == "__main__":
    for k,v in testCases.items():
        print(k,v)
        assert reverse_digits(k) == v
    print(reverse_digits(123))
    