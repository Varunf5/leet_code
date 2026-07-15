class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        r=[]
        rows,cols,posd,negd=set(),set(),set(),set()
        l=[["."]*(n) for p in range(n)]
        def bt(i):
            if(i==n):
                d=["".join(p) for p in l]
                r.append(d)
            for j in range(n):
                if i in rows or j in cols or i+j in posd or i-j in negd or l[i][j] =="Q":
                    continue
                l[i][j]="Q"
                rows.add(i)
                cols.add(j)
                posd.add(i+j)
                negd.add(i-j)
                bt(i+1)
                l[i][j]="."
                rows.discard(i)
                cols.discard(j)
                posd.discard(i+j)
                negd.discard(i-j)
        bt(0)
        return r

