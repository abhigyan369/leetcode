# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, ans):
        if root == None: return []
        q = deque()
        q.append(root)
        left_to_right = True
        while len(q) != 0:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if left_to_right == False:
                level.reverse()
            ans.append(level)
            left_to_right = not left_to_right

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.helper(root,ans)
        return ans
        