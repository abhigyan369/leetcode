# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root,summ):

        if root == None: return 0
        summ = summ*10 + root.val

        if root.left is None and root.right is None:
            return summ

        left = self.solve(root.left,summ)
        right = self.solve(root.right,summ)

        return left + right
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = 0
        return self.solve(root,summ)