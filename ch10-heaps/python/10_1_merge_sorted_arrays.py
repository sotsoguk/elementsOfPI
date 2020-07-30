
# Elements of Programming Interviews
# Chapter 10 - Heaps
# 10.1 Merge already sorted arrays

from typing import List,Union
import heapq

def merge_sorted_arrays(sorted_arrays:List[int]) -> List[int]:
    min_heap:List[Union[int,None]] = []
    result:List[Union[int,None]] = []
    # Build a list of all iterators of the arrays
    iterators = [iter(x) for x in sorted_arrays]

    # Put the first element of each array into the heap
    for i, it in enumerate(iterators):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element,i)) # store the index of the array which the elemnt is from
        
    while min_heap:
        smallest_value, smallest_index = heapq.heappop(min_heap)
        smallest_array_it = iterators[smallest_index]
        result.append(smallest_value)
        next_element = next(smallest_array_it,None)
        if next_element is not None:
            heapq.heappush(min_heap,(next_element, smallest_index))
    return result

## pythonic soltion
def pythonic_merge(sorted_arrays:List[int]) ->List[int]:
    return list(heapq.merge(*sorted_arrays))

if __name__ == "__main__":
    a = [3,5,7]
    b = [0,2,6,9]
    c= [1,3,4,10]
    print(merge_sorted_arrays([a,b,c]))    
    print(pythonic_merge([a,b,c]))