class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mp = Counter(nums)
        ans = []
        for key in list(mp.keys()):
            if mp[key] == 2:
                ans.append(key)
        return ans