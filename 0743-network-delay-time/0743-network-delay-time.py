import heapq as hq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for i in range(n+1)]
        for u,v,c in times:
            adj[u].append((v,c))
        dist=[1000000]*(n+1)
        dist[k]=0
        pq=[(0,k)]
        while pq:
            d,u=hq.heappop(pq)
            if d!=dist[u]:continue
            for v,c in adj[u]:
                if d+c<dist[v]:
                    dist[v]=d+c
                    hq.heappush(pq,(dist[v],v))
        mx=max(dist[1:])
        if mx==1000000:return -1
        return mx