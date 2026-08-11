class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == 1: return False
        for i in range(len(nums)):
            if nums[i-1] == nums[i]: return True
        return False