class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=[]
        m=n
        while n!=0:
            a=n%10
            n=n//10
            s.append(a)
        p=1
        t=0
        for i in range(len(s)):
            p*=s[i]
            t+=s[i]
        return m%(p+t)==0
        
