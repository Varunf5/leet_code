class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dis=[10**6]*n 
        dis[src]=0
        for i in range(k+1):
            temp=dis[:]
            for u,v,c in flights:
                if dis[u]!=10**6 and temp[v]>dis[u]+c:
                    temp[v]=dis[u]+c
            dis=temp[:]
        if dis[dst]==10**6:return -1
        return dis[dst]       