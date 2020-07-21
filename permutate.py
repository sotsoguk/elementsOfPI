# Elements of Programming Interviews
# Chapter 05 - Arrays
# 5.10 Permutate Arrays
#  
# 

def permutate(a,p):
    if len(a) != len(p):
        raise ValueError()
    
    for i in range(len(a)):
        next = i
        while p[next] >= 0:
            a[i], a[p[next]] = a[p[next]], a[i] # swap
            tmp = p[next]
            p[next] -= len(p)
            next = tmp
            print(a,p,i,next)
    return a, p


if __name__ == "__main__":
    a = ['a','b','c','d']
    p = [1,2,0,3]
    print(permutate(a,p))
