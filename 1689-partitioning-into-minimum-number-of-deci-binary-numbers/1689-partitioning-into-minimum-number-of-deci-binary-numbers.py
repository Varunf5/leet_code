class Solution:
    def minPartitions(self, n: str) -> int:
        l=0
        for ch in n:
            digit=int(ch)
            if digit>l:
                l=digit
        return l