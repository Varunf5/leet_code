class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        t=x
        b=t+k-1
        while t<=b:
            t_row=grid[t]
            b_row=grid[b]
            for idx in range(y, y + k):
                t_row[idx],b_row[idx]=b_row[idx],t_row[idx]
            t+=1
            b-=1
        return grid