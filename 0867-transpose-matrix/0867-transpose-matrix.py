class Solution:
    def transpose(self, mat: list[list[int]]) -> list[list[int]]:
        n = len(mat)
        m = len(mat[0])
        res = [[0]*n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                res[j][i] = mat[i][j]

        return res