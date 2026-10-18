class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        posi = set(nums)
        target = 1
        while target in posi:
            target += 1
        return target