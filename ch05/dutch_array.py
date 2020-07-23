# EPI 
# Chapter 5: Arrays
# 5.1 Dutch flag partioning

def dutch_partition(a,p):
  if p>= len(a):
      raise ValueError()
  # first run , put all smaller values to the front
  smaller = 0
  pivot = a[p]
  for i in range(len(a)):
    if a[i] < pivot:
        a[i], a[smaller] = a[smaller],a[i]
        smaller += 1
  
  # second run, bring all larger than pivot 
  larger = len(a)-1
  for i in reversed(range(len(a))):
    if a[i] < pivot:
        break
    elif a[i] > pivot:
        a[i], a[larger] = a[larger], a[i]
        larger -= 1
  return a
  
def part_true_false(a):
    f = 0
    t = len(a) - 1
    for i in range(len(a)):
        if not a[i]:
            a[i], a[f] = a[f],a[i]
            f += 1
    return a
if __name__ == '__main__':
    a = [1,3,2,1,4,1,2,5,1]
    p = 2
    print(dutch_partition(a,p))
    b = [0,1,1,1,0,1,1,0,0,1,1,0]
    print(part_true_false(b))
