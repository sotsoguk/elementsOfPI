import typing, random, heapq
from typing import List,Tuple


from math import sqrt
class Star:
    def __init__(self, x:int=0.0,y:int=0,z:int=0) -> None:
        self._x, self._y, self._z = x,y,z
    @property
    def distance(self) -> float:
        return sqrt(self._x**2 + self._y**2 + self._z**2)

    def __lt__(self, rhs) -> bool:
        return self.distance < rhs.distance


def find_closest_k_stars(stars: List[Star], k:int)->List[Star]:
   
    max_heap:List[Tuple[int,Star]]= []
    for star in stars:
        heapq.heappush(max_heap,(-star.distance,star))
        if len(max_heap) == k+1:
            heapq.heappop(max_heap)
    return [s[1] for s in heapq.nlargest(k,max_heap)]

if __name__ == "__main__":
    # generate stars
    num_stars = 10000
    max_coord = 10000
    stars:List[Star] = []
    for i in range(num_stars):
        stars.append(Star(random.randint(1,max_coord)))
    # for s in stars:
    #     print(s.distance)
    k = 5
    closest_stars = find_closest_k_stars(stars,k)
    print(f'{k}-closest stars:')
    for s in closest_stars:
        print(s.distance)