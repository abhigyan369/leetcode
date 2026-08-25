class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        count = 0
        n = len(nums)
        mp = {}

        for i in range(n):

            first = nums[i] + k
            second = nums[i] - k

            if first in mp:
                count += mp[first]

            if second in mp:
                count += mp[second]

            mp[nums[i]] = mp.get(nums[i], 0) + 1

        return count