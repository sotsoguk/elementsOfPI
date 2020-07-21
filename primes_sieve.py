# Elements of Programming Interviews
# Chapter 05 - Arrays
# 5.9 Enumerate all primes up to n
#  
# O(n/2 + n/3 + n/5 + n/7 +...) = O(nlog logn)

def generate_primes(n):
    if n < 2:
        return []
    primes = []
    is_prime = [False,False]+[True]*(n-1)
    for p in range(2,n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p,n+1,p):
                is_prime[i] = False
    return primes

def generate_primes2(n):
    if n<2:
        return []
    primes = [2]
    # check only odd numbers 3,5,7, .. n (or n-1)
    # index with i ==> p = 2*i+3 => size = (n-3)//2 +1
    size = (n-3)//2 +1
    is_prime = [True] *size
    for i in range(size):
        if is_prime[i]:
            p = 2*i + 3
            primes.append(p)
            for j in range(2*i**2+6*i+3,size,p):
                is_prime[j] = False
    return primes

if __name__ == "__main__":
    print(generate_primes(100))
    print(generate_primes2(100))

