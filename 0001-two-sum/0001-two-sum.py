class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if nums[i] in mp:
                return [mp[nums[i]], i]
            mp[rem] = i    
        return [-1,-1]