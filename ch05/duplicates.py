
# Elements of Programming Interviews
# Chapter 05 - Arrays
# 5.5 Delete duplicates online
#  O(n), O(1)
# 
 
# Variant: remove given key element

def remove(a,key):
    if not a:
        return [],0
    offset = 0
    for i in range(len(a)):
        # not the key value, skip
        if a[i] == key:
            offset += 1
            # continue
        elif offset == 0:
            continue
        else:
            a[i-offset] = a[i]
    for i in range(0,offset):
        a[-(1+i)] = 0
    return a,len(a)-offset

def findDuplicates(a):
    if len(a) < 2:
        return a
    curr_value = a[0]
    offset = 0
    for i in range(1,len(a)):
        prev_value = curr_value
        curr_value = a[i]
        if curr_value == prev_value:
            offset += 1
        else:
            a[i-offset-1] = prev_value
        print(i,a)
    a[len(a)-offset-1] = curr_value
    for i in range(0,offset):
        a[-(1+i)] = 0
    return a,len(a)-offset

if __name__ == "__main__":
    # print(findDuplicates([2,3,5,5,7,11,11,11,13,13,15]))
    print(remove([1,2,3,3,7,3,3,4,5,6],3))
    print(remove([3,3,3],3))

