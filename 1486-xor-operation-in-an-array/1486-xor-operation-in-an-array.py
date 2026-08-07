class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [-1] * n
        for i in range(n):
            nums[i] = start + (2 * i)
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor