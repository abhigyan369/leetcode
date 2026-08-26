class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_sum = 0
        count = 0
        mp = {0 : 1}
        for num in nums:
            cur_sum += num
            if cur_sum - k in mp:
                count += mp[cur_sum-k]
            mp[cur_sum] = mp.get(cur_sum,0) + 1
        return count
        