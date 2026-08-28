class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ## solve using duth national flag algo
        low = 0 
        mid = 0 # current element
        high = n -1 
        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high],nums[mid] = nums[mid], nums[high]
                high -= 1

## algorithm
# low, mid ko 0 index par and high ko last index par
# mid is the current element jo helper hai swap karne ke liye
# agar nums[mid] = 0 hai, then swap with low
# agar nums[mid] = 1 hai, then no swapping required
# agar nums[mid] = 2 hai, then swap with high
            