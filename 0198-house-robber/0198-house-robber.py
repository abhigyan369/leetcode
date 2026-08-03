class Solution:
    def solve(self,nums,index,n):
        if index >= n:
            return 0
        if self.t[index] != -1:
            return self.t[index]
        take = nums[index] + self.solve(nums,index+2,n)
        not_take = self.solve(nums,index+1,n)
        self.t[index] = max(take,not_take)
        return self.t[index]

    def rob(self, nums: List[int]) -> int:
        self.t = [-1] * 101
        n = len(nums)
        return self.solve(nums,0,n)
