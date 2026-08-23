class Solution:
    def binary(self, n):
        result = ""

        while n > 0:
            result = str(n % 2) + result
            n //= 2

        return "0" * (8 - len(result)) + result

    def isPalindromic(self, s: str) -> bool:
        check = ""

        for char in s:
            check += self.binary(ord(char))

        return check == check[::-1]