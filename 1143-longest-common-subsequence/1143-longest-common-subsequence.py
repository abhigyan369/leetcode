class Solution:
    def solve(self, s1, s2, i, j,t):
        ## base case - last tak reach kar gye
        if i >= len(s1) or j >= len(s2):
            return 0
        if t[i][j] != -1:
            return t[i][j]
        if s1[i] == s2[j]:
            return 1 + self.solve(s1,s2,i+1,j+1,t)
        else:
            t[i][j] = max(self.solve(s1,s2,i,j+1,t), self.solve(s1,s2, i+1, j,t))
        return t[i][j]

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        ## classic question of dp on strings (why dp??)
        ## 1. options - lena hai(equal hai , toh +1 ) ya nhi lena hai(not equal hai)
        ## 2. problem repeat ho rhe hai
        ## 3. question me optimal puch rha hai - like maximum, minimum aisa kuch
        m = len(s1)
        n = len(s2)
        t = [[-1] * (1001) for _ in range(1001)]
        return self.solve(s1,s2,0,0,t)