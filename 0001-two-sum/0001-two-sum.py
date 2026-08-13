class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mp = {}
        for i in range(n):
            remaining = target - nums[i]
            if remaining in mp:
                return [mp[remaining], i]

            mp[nums[i]] = i
        return []       

### nums = [2,7,11,15], target = 9
## mp = {2:0, 7:1, 11:2, 15:3}
## rem = 9-2 => 7 