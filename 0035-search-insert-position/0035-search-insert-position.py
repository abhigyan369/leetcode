class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## brute force solution using linear search
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
        
