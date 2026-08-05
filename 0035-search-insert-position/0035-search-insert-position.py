class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## using binary search
        lo = 0
        hi = len(nums) -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
            
        
