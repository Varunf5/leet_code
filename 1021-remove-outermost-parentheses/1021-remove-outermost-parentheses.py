class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        d=0
        for i in s:
            if i=="(":
                if d>0:
                    res+=i
                d+=1
            else:
                d-=1
                if d>0:
                    res+=i
        return res


        