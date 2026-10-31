class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n=len(nums)
        a=[]
        for i in range(n):
            if target==nums[i]:
                a.append(i)
        return a


        