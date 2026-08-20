class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorResult = 0
        for i in range(n+1):
            xorResult = xorResult ^ i
        for num in nums:
            xorResult = xorResult ^ num
        return xorResult