class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s=[]
        for i in range(1,n+1):
            x=bin(i)[2:]
            s.append(x)
        m="".join(s)
        return int(m,2)%(10**9+7)
