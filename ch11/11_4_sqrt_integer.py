import math

def sqrt_integer(n):
    if n <= 1:
        return n
    if n <= 3:
        return 1
    left = 0
    right = n // 2
    while left <= right:
        mid = (left+right) // 2
        tmp = n-mid ** 2
        # print(left,mid,right,tmp)
        if (tmp) >= 0 and tmp < 2*mid+1:
            return mid
        elif tmp <0:
            right = mid -1
        else :
            left = mid +1

    return left

if __name__ == "__main__":
    for i in range (150,325):
        print(i,sqrt_integer(i))