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
        while len(q) != 0:
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                if i == level_len - 1:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(root,ans)
        return ans
    
        