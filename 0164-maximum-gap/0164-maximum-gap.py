class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        i,j = 0,1
        while j < len(nums):
            diff = nums[j] - nums[i]
            maxi = max(maxi,diff)
            i += 1
            j += 1
        return maxi