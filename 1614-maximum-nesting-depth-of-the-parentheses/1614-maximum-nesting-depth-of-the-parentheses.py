class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        openbracket = 0
        res = 0

        for i in range(n):
            if s[i] == '(':
                openbracket += 1
                res = max(res,openbracket)
            elif s[i] == ')':
                openbracket -= 1
        return res
