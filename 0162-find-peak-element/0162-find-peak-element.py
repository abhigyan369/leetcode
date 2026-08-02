class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        temp = max(nums)
        for i in range(len(nums)):
            if nums[i] == temp:
                return i
        