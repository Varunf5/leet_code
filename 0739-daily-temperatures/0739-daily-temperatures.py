class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        r=[0]*len(temperatures)
        for p in range(len(temperatures)):
            while(st and temperatures[p]>temperatures[st[-1]]):
                d=st.pop()
                r[d]=p-d
            st.append(p)
        return r
        

        