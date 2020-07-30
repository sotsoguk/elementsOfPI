from typing import List,Union
import random
class Heap():
    def __init__(self,capacity:int = 4) -> None:
        self.capacity = max(capacity,4)
        self.data:List[Union[int,None]] = [None] * (self.capacity+1)
        self.lastpos = 0
    
    def __double_capacity(self) -> None:
        self.data += [None]*(self.capacity)
        self.capacity += self.capacity

    def __repr__(self) -> str:
        output = ""
        for i in range(1,self.lastpos+1):
            output += f'{self.data[i]},'
        
        return output
    
    def insert(self,v) -> None:
        self.lastpos += 1
        # print(self.lastpos)
       
        if self.lastpos > self.capacity:
            self.__double_capacity()
        self.data[self.lastpos] = v
        # print("HERE:",self.data)
        # heapify to max heap
        currPos = self.lastpos
        while currPos >= 1:
            # get parent node
            parent = currPos // 2
            if parent > 0 and self.data[currPos] > self.data[parent]:
                self.data[currPos], self.data[parent] = self.data[parent], self.data[currPos]
                currPos = parent
            else:
                break
    def max_child(self,i:int) -> int:
            if i*2 + 1 > self.lastpos:
                return 2*i
            if self.data[2*i] > self.data[2*i+1]:
                return 2*i
            else:
                return 2*i +1

    def pop(self) -> Union[int,None]:
       
        if self.lastpos == 0:
            return None
        maxValue = self.data[1]
        # print("Beofre Swapped:",self.data)
        self.data[1] = self.data[self.lastpos]
        # print("Swapped:",self.data)
        self.lastpos -= 1
        # heapify again, bubble down
        currPos = 1
        while (2* currPos <= self.lastpos):
            # compare with left child
            maxc = self.max_child(currPos)
            if self.data[currPos] < self.data[maxc]:
                self.data[currPos], self.data[maxc] = self.data[maxc], self.data[currPos]
            currPos = maxc
        return maxValue
    def get_size(self) -> int:
        return self.lastpos

if __name__ == "__main__":
    # print("HELLO")
    h = Heap()
    # 
    random.seed(42)
    for _ in range(20):
        h.insert(random.randrange(0,100))
    print(h)
    while h.get_size():
        print(f'Popped = {h.pop()}')
        print(h)
        print("-------\n")