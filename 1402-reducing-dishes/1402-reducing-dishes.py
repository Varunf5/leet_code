class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        arr = satisfaction
        arr.sort()
        summ = 0
        idx = 0
        for i in range(len(arr) - 1, -1, -1):
            summ += arr[i]
            if summ < 0:
                idx = i + 1
                break
        time = 1
        summ = 0
        for i in range(idx, len(arr)):
            summ += arr[i] * time
            time += 1
        return summ