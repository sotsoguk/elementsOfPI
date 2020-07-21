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
    print(findDuplicates([2,3,5,5,7,11,11,11,13,13,15]))
    

