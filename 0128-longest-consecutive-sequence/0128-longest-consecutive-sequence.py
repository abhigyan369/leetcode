class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        streak = 1
        maxi = 1
        if len(nums) == 0: return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1

            maxi = max(maxi, streak)

        return maxi