import random
def minmax(a):
    # find the min and max simultanously
    if not a:
        return (-1,-1)
    if len(a) == 1:
        return a[0],a[0]
    a_min = min(a[0],a[1])
    a_max = max(a[0],a[1])
    if len(a) == 2:
        return a_min,a_max
    upper_range_bound = len(a)-1
    # if len(a) %2 :
    #     upper_range_bound = upper_range_bound//2 * 2
    for i in range(2,upper_range_bound,2):
        local_min, local_max = 0,0
        if a[i] < a[i+1]:
            local_min = a[i]
            local_max = a[i+1]
        else:
            local_min = a[i+1]
            local_max = a[i]
        a_min = min(a_min,local_min)
        a_max = max(a_max,local_max)
        #     a_min = min(a[i],a_min)
        #     a_max = max(a[i+1],a_max)
        # elif a[i] > a[i+1]:
        #     a_min = min(a[i+1],a_min)
        #     a_max = max(a[i],a_max)
        # else:
        #     a_min = min(a_min,a[i])
        #     a_max = min(a_max,a[i])
    if len(a) % 2:
        a_min = min(a_min,a[len(a)-1])
        a_max = max(a_max,a[len(a)-1])
    return a_min, a_max

if __name__ == "__main__":
    num_ints = 10
    range_ints = [0,20]
    a = [0] * num_ints
    for i in range(num_ints):
        a[i] = random.randint(range_ints[0],range_ints[1])
    a = [1,2,3,4]
    print(a)
    print(minmax(a))
    