class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=[]
        c,n,m=0,len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:c+=1
                if grid[i][j]==2:q.append((i,j))
        level=0
        if c==0: return 0
        while q:
            s=len(q)
            for i in range(s):
                i,j=q.pop(0)
                for x,y in [(0,-1),(-1,0),(1,0),(0,1)]:
                    ni,nj=i+x,j+y
                    if 0<=ni<n and 0<=nj<m and grid[ni][nj]==1:
                        c-=1;grid[ni][nj]=2
                        q.append((ni,nj))
            level+=1
        if c==0:return  level-1
        return -1