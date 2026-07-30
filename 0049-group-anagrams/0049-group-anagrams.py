class Solution:
    def generate(self, word: str):
        arr = [0] * 26
        for ch in word:
            arr[ord(ch) - ord('a')] += 1
        return tuple(arr)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for word in strs:
            key = self.generate(word)
            if key not in mp:
                mp[key] = []
            mp[key].append(word)

        return list(mp.values())