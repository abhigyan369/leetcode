class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## anagram-
        ## "anagram" - a -> 3, n->1, g->1, r->1, m->1
        ## nagaram = a -> 3, n->1, g->1, r->1, m->1

        mp1 = {}
        for char in s:
            mp1[char] = mp1.get(char,0) + 1
        mp2 = {}
        for char in t:
            mp2[char] = mp2.get(char,0) + 1
        return mp1 == mp2
