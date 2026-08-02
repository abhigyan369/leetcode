
class Solution:
    
    t = [[-1]*1001 for _ in range(200)]
    def solve(self,idx,nums,target):
        n = len(nums)
        if target == 0:
            return 1
        if idx >= n or target < 0:
            return 0
        if Solution.t[idx][target] != -1:
            return Solution.t[idx][target]
        result = 0
        for i in range(len(nums)):
            take_idx = self.solve(0,nums,target-nums[i])
            result += take_idx

        Solution.t[idx][target] = result
        return Solution.t[idx][target]
        




    def combinationSum4(self, nums: List[int], target: int) -> int:
        Solution.t = [[-1]*1001 for _ in range(200)]
        return self.solve(0,nums,target)