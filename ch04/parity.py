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

# precompute the parity for 16 bit numbers

def precompute_parity():
    max_bits = 16
    cache = [None] * (1<<max_bits)
    for i in range(1<<max_bits):
        cache[i] = parity_2(i)
    return cache

def parity_4(x, cache):
    mask_size = 16
    bit_mask = 0xFFFF
    return  (cache[x >> (3*mask_size)] ^ cache[(x >> (2*mask_size)) & bit_mask] ^
            cache[(x >> mask_size) & bit_mask ] ^ cache[x & bit_mask])
    

def test_parity(nums,expected,func):
    for i,tc in enumerate(nums):
        if func(tc) != expected[i]:
            return False
    return True

# propagate rightmost set bit to the right (eg. 0101000 -> 0101111)
def propagate(x):
    # get rightmost set bit
    rmsb = x & -(x-1)
    return x | (rmsb-1)

def powmod(x,pow):
    return x & (pow-1)

def isPowOf2(x):
    return x == 1 or x == (x & -(x-1))



def main():
    print(parity_1(1),parity_1(3),parity_1(16),parity_1(17))
    # print(parity_2(1),parity_2(3),parity_2(16),parity_2(17))
    # print(f'parity_1: {test_parity(testCases,testResults,parity_1)}')
    # print(f'parity_2: {test_parity(testCases,testResults,parity_2)}')
    # print(f'parity_3: {test_parity(testCases,testResults,parity_3)}')
    # print(propagate(2))
    # print(powmod(77,64))
    # print(isPowOf2(16),isPowOf2(1),isPowOf2(0),isPowOf2(33),isPowOf2(4096))
    # print(po2(16),po2(80),po2(0),po2(33),po2(4096))
    cache = precompute_parity()
    print(parity_4(1,cache),parity_4(3,cache),parity_4(16,cache),parity_4(17,cache))
    print(cache[1],cache[3],cache[16],cache[17])

if __name__ == "__main__":
    main()
