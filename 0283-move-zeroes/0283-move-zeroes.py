class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[l] == 0 and nums[r] != 0:
                # swap
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
            if nums[l] != 0 and nums[r] != 0:
                l += 1


        

# 0     1   0   3   12
# l,r
# l     r
# 1     0   0   3   12 ->swap
#       l   r
#       l       r
# 1     3   0   0   12 ->swap
#           l       r
# 1     3   12  0   0-> swap
            

        