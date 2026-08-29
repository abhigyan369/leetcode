class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = -float('inf')
        window_sum = 0
        n = len(nums)
        for i in range(n):
            window_sum += nums[i]
            window_avg = 0
            if i >= k:
                window_sum -= nums[i-k]
                
            if i >= k - 1:
                window_avg = window_sum / k
                maxi = max(maxi, window_avg)
        return maxi