class Solution:
    def merge_array(self, left, right):
        result = []
        i,j=0,0
        n = len(left)
        m = len(right)
        ## loop until one array exahausts
        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        if i < n:
            while i < n:
                result.append(left[i])
                i += 1
        if j < m:
            while j < m:
                result.append(right[j])
                j += 1
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        left = self.sortArray(left_arr)
        right = self.sortArray(right_arr)
        return self.merge_array(left,right)
