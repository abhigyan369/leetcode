class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        result = []
        for s in strs:
            key = "".join(sorted(s))
            if key not in mp:
                mp[key] = []

            mp[key].append(s)

        return list(mp.values())