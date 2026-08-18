class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        result = [0] * n
        nums.sort()
        j = n - 1
        i = 1
        while i < n:
            result[i] = nums[j]
            i += 2
            j -= 1
        i = 0
        while i < n:
            result[i] = nums[j]
            i += 2
            j -= 1
        nums[:] = result
        
        