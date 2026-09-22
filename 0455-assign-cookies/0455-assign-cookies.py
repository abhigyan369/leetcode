class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i,j =0,0
        n,m = len(g), len(s)
        
        g.sort()
        s.sort()

        while i < n and j < m:
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i

'''
7 8 9 10

5 6 7 8


'''