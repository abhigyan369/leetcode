class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos = []
        for num in nums:
            if num > 0:
                pos.append(num)
        pos.sort()
        target = 1
        for n in pos:
            if n == target:
                target += 1
            elif n > target:
                return target
        
        return target