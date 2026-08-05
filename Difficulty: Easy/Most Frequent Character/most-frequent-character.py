class Solution:
    def getMaxOccuringChar(self, s):
        mp = {}

        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1

        ans = None
        max_freq = 0

        for ch, freq in mp.items():
            if freq > max_freq:
                max_freq = freq
                ans = ch
            elif freq == max_freq and ch < ans:
                ans = ch

        return ans