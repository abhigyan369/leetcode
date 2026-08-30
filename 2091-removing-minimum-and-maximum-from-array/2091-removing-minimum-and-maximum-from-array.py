class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi = float('-inf')
        maxIndex = 0
        mini =  float('inf')
        minIndex = 0
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                maxIndex = i
            if nums[i] < mini:
                mini = nums[i]
                minIndex = i
        leftIndex = min(maxIndex, minIndex)
        rightIndex = max(maxIndex, minIndex)

        #all 3 options- 
        #1. LeftIdx se left deletion
        # RightIdx se right deletion

        #2. both from left delete

        #3. both from right delete

        return min((leftIndex+1)+(n-rightIndex),
        rightIndex+1, 
        n-leftIndex)

