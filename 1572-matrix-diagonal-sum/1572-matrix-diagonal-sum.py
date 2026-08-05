class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary_sum = 0
        secondary_sum = 0
        n = len(mat)

        for i in range(n):
            for j in range(n):
                if i == j:
                    primary_sum += mat[i][j]

                if i + j == n - 1:
                    secondary_sum += mat[i][j]

        total = primary_sum + secondary_sum

        if n % 2 == 1:  ## odd matrix hua to delete karna madega
            total -= mat[n // 2][n // 2]

        return total