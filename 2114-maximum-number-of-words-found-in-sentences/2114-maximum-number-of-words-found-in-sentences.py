class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        cnt = 0
        maxi = 0
        for sentence in sentences:
            for char in sentence:
                if char == ' ':
                    cnt += 1
                    maxi = max(maxi,cnt)
            cnt = 0
        return maxi + 1