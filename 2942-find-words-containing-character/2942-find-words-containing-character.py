class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        res = []
        for i in range(n):
            for j in range(len(words[i])):
                if words[i][j] == x:
                    res.append(i)
                    break

        return res