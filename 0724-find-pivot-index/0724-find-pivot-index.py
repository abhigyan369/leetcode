class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    ## from the observation by calculating prefix sum and suffix sum
    ## we will iterate through both prefix and suffix, the number which is same for the index-> return the index
        n = len(nums)
        ## calculating prefix
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]

        ## calculating suffix sum
        suffix = [0] * n
        suffix[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] + nums[i]
        
        for i in range(n):
            if prefix[i] == suffix[i]:
                return i
        return -1