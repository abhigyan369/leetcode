class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        maxi = 0
        i = 0
        for j in range(len(s)):
            if s[j] in mp:
                i = max(i,mp[s[j]] + 1)
            mp[s[j]] = j
            maxi = max(maxi, j-i+1)

        return maxi