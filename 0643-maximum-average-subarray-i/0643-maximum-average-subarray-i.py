class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = -float('inf')
        window_sum = 0
        n = len(nums)
        for i in range(n):
            window_sum += nums[i]
            if i >= k - 1:
                maxi = max(maxi, window_sum/k)
                window_sum = window_sum - nums[i-k+1]
        return maxi