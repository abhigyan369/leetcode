class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        arr = []

        while top <= bottom and left <= right:

            # left -> right
            for j in range(left, right + 1):
                arr.append(matrix[top][j])
            top += 1

            # top -> bottom
            for i in range(top, bottom + 1):
                arr.append(matrix[i][right])
            right -= 1

            # right -> left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    arr.append(matrix[bottom][j])
                bottom -= 1

            # bottom -> top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    arr.append(matrix[i][left])
                left += 1

        return arr