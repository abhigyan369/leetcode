class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = -float('inf')
        window_sum = 0
        n = len(nums)
        ## first window
        for i in range(k):
            window_sum += nums[i]
        maxi = window_sum/k

        # slide
        for i in range(k,n):
            window_sum -= nums[i-k]
            window_sum += nums[i]
            maxi = max(maxi, window_sum/k)
        return maxi