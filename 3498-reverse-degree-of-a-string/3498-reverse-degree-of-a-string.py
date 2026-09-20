class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans = ans + (i+1)* (123-ord(s[i]))
        return ans