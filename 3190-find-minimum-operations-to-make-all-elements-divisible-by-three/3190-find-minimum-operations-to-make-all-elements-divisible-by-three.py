class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        notdivby3 = 0
        for num in nums:
            if num%3 != 0:
                notdivby3 += 1
        return notdivby3