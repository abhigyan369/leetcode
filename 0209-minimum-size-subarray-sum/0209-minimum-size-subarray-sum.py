class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # variable size sliding window

        left = 0
        summ = 0
        ans = float('inf')
        n = len(nums)

        for right in range(n):
            # expand the window
            summ += nums[right]
            ## condition met toh -> shrink
            while summ >= target:
                ans = min(ans, right-left+1)
                summ -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans