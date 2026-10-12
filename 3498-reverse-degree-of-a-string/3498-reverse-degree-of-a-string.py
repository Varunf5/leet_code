class Solution:
    def reverseDegree(self, s: str) -> int:
        a=0
        for i,ch in enumerate(s,start=1):
            a+=(122 - ord(ch) + 1)*i
        return a
