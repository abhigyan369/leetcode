class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if i < j and nums[i] == nums[j]:
                    cnt += 1
        return cnt