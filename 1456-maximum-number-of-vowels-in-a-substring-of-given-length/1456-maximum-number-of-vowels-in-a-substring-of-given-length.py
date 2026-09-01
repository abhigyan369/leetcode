class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        st = set('aeiou')
        n = len(s)
        count = 0
        maxi = 0
        # first window
        for i in range(k):
            if s[i] in st:
                count += 1
        maxi = count

    
        # slide
        for i in range(k,n):
            if s[i] in st:
                count += 1
            if s[i-k] in st:
                count -= 1
            maxi = max(maxi, count)

        return maxi