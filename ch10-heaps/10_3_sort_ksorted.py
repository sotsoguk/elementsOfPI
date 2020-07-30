
# Elements of Programming Interviews
# Chapter 10 - Heaps
# 10.3 Sort a k-sorted array (each value is only max k away from right position)

from typing import List,Union
import heapq,itertools


def sort_k_sorted(array:List[int],k:int) ->List[int]:
    min_heap:List[int] = array[:k+1]
    heapq.heapify(min_heap)
    result:List[int] =[]
    for i in range(k+1,len(array)):
        result.append(heapq.heappushpop(min_heap,array[i]))
    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result
if __name__ == "__main__":
    pass
    a= [3,-1,2,6,4,5,8]
    print(sort_k_sorted(a,3))
    
