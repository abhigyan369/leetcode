
# brute force solution- finding all the subarray using 2 for loop and check if it is equal to the target.
# this won't work in interview, do another approach of hashing

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    