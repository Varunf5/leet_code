class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col,tl,tr=[0]*n,[0]*(2*n+1),[0]*(2*n+1)
        b=[['.']*n for i in range(n)]
        res=[]
        def nqueen(i,n):
            if i==n:
                t=[]
                for i in range(n):
                    t.append(''.join(b[i]))
                res.append(t)
                return
            for j in range(n):
                if not col[j] and not tl[i-j+n-1] and not tr[i+j]:
                    col[j]=tl[i-j+n-1]=tr[i+j]=1;b[i][j]="Q"
                    nqueen(i+1,n)
                    b[i][j]='.';col[j]=tl[i-j+n-1]=tr[i+j]=0
        nqueen(0,n)
        return res        