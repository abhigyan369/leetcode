class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        for arr in matrix:
            summ = sum(arr)
            ans.append(summ)
        return ans