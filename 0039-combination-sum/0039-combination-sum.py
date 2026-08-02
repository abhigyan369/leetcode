class Solution:
    def solve(self,ans,candidates,temp,idx,target):
        if target == 0:
            ans.append(temp[:])
            return
        if idx >= len(candidates) or target < 0:
            return
        ## not included
        self.solve(ans,candidates,temp,idx+1,target)
        ## included
        temp.append(candidates[idx])
        self.solve(ans,candidates,temp,idx, target - candidates[idx])
        temp.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        self.solve(ans,candidates,temp,0,target)
        return ans