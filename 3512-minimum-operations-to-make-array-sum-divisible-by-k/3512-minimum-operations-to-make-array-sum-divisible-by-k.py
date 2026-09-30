class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        remainder = sum(nums) % k
        return remainder
        