class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for c in s:
            if c.isalnum():
                a.append(c.lower())
        l=0
        r=len(a)-1
        while l<r:
            if a[l] != a[r]:
                return False
            l+=1
            r-=1
        return True
            