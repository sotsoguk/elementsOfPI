import typing
from typing import List


def n_queens(n:int) -> List[int]:
    def solve_n(row:int) -> None:
        if row == n:
            result.append(list(placement))
            return
        # test all cols
        for col in range(n):
            # if a queen conflicts with an other one it is either in the same col ( col - oldcol == 0 )
            # or it is diagonally (if i rows above abs(col -oldcol) == 2
            if all (
                    abs(c-col) not in (0,row-i) 
                    for i,c in enumerate(placement[:row])):
                placement[row] = col
                if row == n-1:
                    result.append(list(placement))
                    return
                else:
                    solve_n(row+1)            

    result = []
    placement = [0] * n 
    solve_n(0)
    return result

if __name__ == "__main__":
    print(n_queens(5))