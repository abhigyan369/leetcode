from typing import List

class Solution:
    def valid(self, n, s, ans):
        if n == 0:
            ans.append(s)
            return

        # Add 1
        s += '1'
        self.valid(n - 1, s, ans)

        # Remove 1
        s = s[:-1]

        # Add 0 only if previous character is 1
        if len(s) == 0 or s[-1] == '1':
            s += '0'
            self.valid(n - 1, s, ans)
            s = s[:-1]

    def validStrings(self, n: int) -> List[str]:
        ans = []
        self.valid(n, "", ans)
        return ans