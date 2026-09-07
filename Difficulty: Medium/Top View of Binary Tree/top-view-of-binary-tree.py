'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        if root == None: return None
        ans = []
        q = deque()
        result = {}
        q.append((root,0))
        while len(q) != 0:
            node, line = q.popleft()
            if line not in result:
                result[line] = node.data
            if node.left is not None:
                q.append((node.left, line-1))
            if node.right is not None:
                q.append((node.right, line+1))
        for val in sorted(result.items()):
            ans.append(val[1])
        return ans
        
        