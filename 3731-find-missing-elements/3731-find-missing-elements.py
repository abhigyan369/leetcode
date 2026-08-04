class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing = []
        tracker = [0]*101
        nums.sort()
        n = len(nums)
        start = nums[0]
        end = nums[-1]
        for i in range(n):
            tracker[nums[i]] = 1
        for i in range(start,end+1):
            if tracker[i] == 0:
                missing.append(i)
        return missing