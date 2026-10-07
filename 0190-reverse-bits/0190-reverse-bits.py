class Solution:
    def reverseBits(self, n: int) -> int:
        a=bin(n)[2:]
        
        a=a.zfill(32)
        rev=a[::-1]
        return int(rev,2)