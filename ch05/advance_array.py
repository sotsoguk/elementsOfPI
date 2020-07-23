# EPI 
# Chapter 5: Arrays
# 5.3 Advance Arrays

def advance_array(a):
    i,reachable = 0,0
    
    while i<len(a) and i<= reachable:
        print(i,reachable,a[i])
        reachable = max(reachable,i+a[i])
        i +=1
    return True if reachable >= len(a)-1 else False

def min_steps(a):
   jumps = 1
   reachable = a[0]
   for i in range(len(a)):
      print(i, reachable,a[i],jumps)
      if reachable <i:
         return -1
      if a[i] + i > reachable:
         reachable = a[i]+i
         jumps += 1
      if reachable >= len(a)-1:
         return jumps
   return jumps
if __name__ == '__main__':
    a = [3,3,1,0,3,0,0]
    print(advance_array(a))
    print(min_steps(a))
