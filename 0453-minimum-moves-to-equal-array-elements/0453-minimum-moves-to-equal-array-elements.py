class Solution:
    def minMoves(self, nums: list[int]) -> int:
        s=0
        m=nums.sort()
        n=nums[0]
        for i in range(len(nums)):
            if nums[0]<=nums[i]:
                s+=(nums[i]-n)
        return s

        