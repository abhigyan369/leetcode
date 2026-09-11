class Solution:
    def common(self, s1: str, s2: str) -> str:
        s = ""
        n = min(len(s1), len(s2))
        for i in range(n):
            if s1[i] == s2[i]:
                s += s1[i]
            else:
                break
        return s

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        s = strs[0]
        for i in range(1, len(strs)):
            s = self.common(s, strs[i])
            if not s:
                break
        return s