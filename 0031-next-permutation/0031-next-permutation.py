class Solution:
    def reverse_from(self,nums, start):
        left = start
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## good question- facebook
        ## approach- right side se traverse karo
        ## condition arr[i-1] < arr[i]
        ## gola arr[i-1] wala element h and find the next greater in the right side and swap with them
        # gola wala element apne right position par aa gya, now reverse all the elements in the right side of goala
        n = len(nums)
        # find first the blue gola
        gola_index = -1
        for i in range(n-1,-1,-1):
            if nums[i] > nums[i - 1]:
                gola_index = i - 1
                break
        if gola_index != -1:
            swap_index = gola_index
            for j in range(n-1,gola_index,-1):
                if nums[j] > nums[gola_index]:
                    swap_index = j
                    break
            ## swap
            nums[gola_index], nums[swap_index] = nums[swap_index], nums[gola_index]

        self.reverse_from(nums, gola_index + 1)
