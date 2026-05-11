class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            maxi = max(maxi, summ)
            if summ < 0:
                summ = 0
        return maxi