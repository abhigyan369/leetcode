class Solution:
    def prodOfDigits(self, num):
        prod = 1
        while num:
            prod *= num % 10
            num //= 10
        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        while self.prodOfDigits(n) % t != 0:
            n += 1
        return n