class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        if total_ones <= 1:
            return 0

        n = len(nums)
        nums = nums + nums

        i = 0
        curOnes = 0
        maxOnes = 0

        for j in range(len(nums)):
            if nums[j] == 1:
                curOnes += 1

            if j - i + 1 > total_ones:
                if nums[i] == 1:
                    curOnes -= 1
                i += 1

            # Only consider windows whose starting index is in the original array
            if j - i + 1 == total_ones and i < n:
                maxOnes = max(maxOnes, curOnes)

        return total_ones - maxOnes