# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateHeight(self, root):
        if root is None:
            return 0
        left = self.calculateHeight(root.left)
        right = self.calculateHeight(root.right)
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        check = abs(self.calculateHeight(root.left) - self.calculateHeight(root.right))
        if check > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)