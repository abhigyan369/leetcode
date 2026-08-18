class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        ans = []
        n = len(nums)
        for num in nums:
            mp[num] = mp.get(num,0) + 1
        
        for k,v in mp.items():
            if v > n // 3:
                ans.append(k)
        return ans