# EPI 
# Chapter 11: Searching
# 11.1 Search for first occurance in sorted array, return index

def search_first_occurance(a,k):
    # at first, whole array is searched
    left, right, result = 0, len(a)-1, -1
    while left <= right:
        mid = left + (right-left)//2
        # midpoint is k
        if a[mid] == k:
            right = mid -1
            result = mid
        elif a[mid] < k:
            left = mid+1
        else:
            right = mid -1
    return result

def find_first_greater(a,k):
    left,right,result = 0,len(a)-1,-1
    while left <= right:
        mid = left+(right-left)//2
        if a[mid] <= k:
            left = mid + 1
        else:
            right = mid-1
            result = mid
    return result

if __name__ == "__main__":
    a =  [-14,-10,2,108,108,243,285,285,285,401]
    print(search_first_occurance(a,108))
    print(find_first_greater(a,285))