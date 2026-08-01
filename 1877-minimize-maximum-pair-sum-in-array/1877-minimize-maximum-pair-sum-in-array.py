class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        i = 0
        j = len(nums) - 1
        mini = float('inf')
        while i < j:
            temp = nums[i] + nums[j]
            ans.append(temp)
            temp = 0
            i += 1
            j -= 1

        return max(ans)