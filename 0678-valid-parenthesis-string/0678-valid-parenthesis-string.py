from functools import lru_cache

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        @lru_cache(None)
        def solve(i, open_count):
            if i == n:
                return open_count == 0
            
            isValid = False
            if s[i] == '*':
                isValid |= solve(i + 1, open_count + 1)
                isValid |= solve(i + 1, open_count)
                if open_count > 0:
                    isValid |= solve(i + 1, open_count - 1)
            elif s[i] == '(':
                isValid |= solve(i + 1, open_count + 1)
            elif open_count > 0:
                isValid |= solve(i + 1, open_count - 1)
                
            return isValid

        return solve(0, 0)