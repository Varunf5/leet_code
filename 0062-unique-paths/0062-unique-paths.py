def dfs(r,c,m,n,cache):
    if r==m or c==n:
        return 1
    if r>m or c>n :
        return 0
    if (r,c) in cache:
        return cache[(r,c)]
    right=dfs(r+1,c,m,n,cache)
    left=dfs(r,c+1,m,n,cache)
    ans =right+left
    cache[(r,c)]=ans
    return ans




class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache={} 
        return dfs(0,0,m-1,n-1,cache)   




        
        