class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        max_streak = 0

        for num in hset:
            if num - 1 not in hset:  # num is the start of a sequence
                curr = num
                curr_streak = 1
                while curr + 1 in hset:
                    curr += 1
                    curr_streak += 1
                max_streak = max(max_streak, curr_streak)

        return max_streak