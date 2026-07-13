class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        nums=sorted(d.items(),key=lambda x:x[1],reverse=True)
        a=[]
        for p in range(k):
            d=nums[p][0]
            a.append(d)
        return a

        

        