def add(a):
    a[-1] += 1
    for i in reversed(range(1,len(a))):
        if a[i] == 10:
            a[i] = 0
            a[i-1] += 1
    if a[0] == 10:
        a[0] = 1
        a.append(0)
    return a

if __name__ == "__main__":
    print(add([9,9,9]))
