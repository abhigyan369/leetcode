class Solution:
    def help(self,nums,i,t):
        if i >= len(nums): return 0
        
        if t[i] != -1:
            return t[i]

        steal = nums[i] + self.help(nums,i+2,t)
        skip = self.help(nums,i+1,t)
        t[i] = max(steal, skip)
        return t[i]

    def rob(self, nums: list[int]) -> int:
        t = [-1] *(len(nums) + 1)
        return self.help(nums,0,t)