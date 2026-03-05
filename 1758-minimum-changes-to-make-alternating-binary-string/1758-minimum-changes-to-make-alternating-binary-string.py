class Solution:
    def minOperations(self, s: str) -> int:
        ch1=0
        ch2=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]!='0':
                    ch1+=1
                else:
                    ch2+=1
            else:
                if s[i]!='1':
                    ch1+=1
                else:
                    ch2+=1
        return min(ch1,ch2)


            
        
        