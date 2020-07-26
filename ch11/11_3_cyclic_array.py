# Chapter 11: Searching
# 11.3 Search smallest entry in cyclic sorted array 
# eg [10,11,12,15,1,2,3,4,5]

def min_cyclic(a):
    if not a:
        return -1
    left, right = 0, len(a)-1
    while left < right:
        mid = left + (right-left)//2
        print(left,mid,right,a[left],a[mid],a[right])
        # left entry exisits and is bigger, entry found
        if (mid == 0 or a[mid-1]>a[mid]):
            return (a[mid],mid)
        if a[mid] > a[right]:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    a = [10,11,12,15,16,17,18]
    print(min_cyclic(a))