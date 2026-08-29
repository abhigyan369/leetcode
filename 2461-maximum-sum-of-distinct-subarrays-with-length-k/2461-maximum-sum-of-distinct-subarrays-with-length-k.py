class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = set()
        curr_sum = 0
        max_sum = 0
        i = 0
        for j in range(n):
            while nums[j] in seen or (j-i+1) >k:
                seen.remove(nums[i])
                curr_sum -= nums[i]
                i += 1
            seen.add(nums[j])
            curr_sum += nums[j]

            if j-i+1 == k:
                max_sum = max(max_sum,curr_sum)
        return max_sum

        

        