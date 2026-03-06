class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        p=[-1]*(n+1)
        def union(x,y):
            p[x]=y
        def find(x):
            while(p[x]!=-1):x=p[x]
            return x
        for u,v in edges:
            ru,rv=find(u),find(v)
            if ru==rv: return[u,v]
            union(ru,rv)
