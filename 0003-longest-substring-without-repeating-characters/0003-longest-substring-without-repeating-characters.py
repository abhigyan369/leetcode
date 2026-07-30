class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        n = len(s)
        maxi = 0
        i = 0
        j = 0
        while i < n and j < n:
            if s[j] not in st:
                st.add(s[j])
                maxi = max(maxi, len(st))
                j += 1
            else:
                st.clear()
                i += 1
                j = i
        return maxi