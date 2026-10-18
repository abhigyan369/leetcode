from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = Counter(nums)
        for key,val in mp.items():
            if val > len(nums) / 2:
                return key