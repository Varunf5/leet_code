class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if n==0:
            return 0
        for i in range(n-1):
            a,b=b,a+b
        return b
