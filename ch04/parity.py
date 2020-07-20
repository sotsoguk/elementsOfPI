# Compute the parity of a word (64 bit integer)

testCases = [1,3,16,17,0b110101011]
testResults = [1,0,1,0,0]#

# parity(x) returns 1 if the number of bits set is odd, otherwise even

# brute force implementation, runtime O(n)

def parity_1(x):
    result = 0
    while x:
        result ^= (x & 1) # check if last bit is 1
        x >>= 1
    return result

# improve runtime, use trick to set lowest 1 to 0, runtime O(k), where k number of 1's
def parity_2(x):
    result = 0
    while x:
        result ^= 1
        x &= (x-1)
    return result

# improve to log n

def parity_3(x):
    x ^= (x>>32)
    x ^= (x>>16)
    x ^= (x>>8)
    x ^= (x>>4)
    x ^= (x>>2)
    x ^= (x>>1)
    return x & 0x1

def test_parity(nums,expected,func):
    for i,tc in enumerate(nums):
        if func(tc) != expected[i]:
            return False
    return True

def main():
    # print(parity_1(1),parity_1(3),parity_1(16),parity_1(17))
    # print(parity_2(1),parity_2(3),parity_2(16),parity_2(17))
    print(f'parity_1: {test_parity(testCases,testResults,parity_1)}')
    print(f'parity_2: {test_parity(testCases,testResults,parity_2)}')
    print(f'parity_3: {test_parity(testCases,testResults,parity_3)}')
if __name__ == "__main__":
    main()
