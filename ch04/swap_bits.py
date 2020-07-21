# Elements of Programming Interviews
# Chapter 04 - Primitives
# 4.2 Swap bits

# swap_bits at i & j position
def swap_bits(x,i,j):
    # check if bits at i and jth position differ
    if (x>>i) & 1 != (x>>j) & 1:
        # create mask with 1 at i and j
        mask = (1<<i) | (1<<j)
        #flip bits with xor
        x ^= mask
    return x

if __name__ == "__main__":
    print(swap_bits(26,2,3))
    
    