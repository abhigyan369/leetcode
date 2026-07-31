class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = [0] * 26
        for char in sentence:
            alpha[ord(char)-ord('a')] += 1
        for num in alpha:
            if num == 0:
                return False
        return True