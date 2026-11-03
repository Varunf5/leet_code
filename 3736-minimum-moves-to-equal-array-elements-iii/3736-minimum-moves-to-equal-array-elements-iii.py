class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s=0
        m=nums.sort()
        n=nums[-1]
        for i in range(len(nums)):
            if nums[0]<=nums[i]:
                s+=(n-nums[i])
        return s
                
        
        