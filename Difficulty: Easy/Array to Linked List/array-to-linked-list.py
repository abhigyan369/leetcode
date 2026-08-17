'''
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def arrayToList(self, arr):
        # code here
        head = Node(arr[0])
        curr = head
        for i in range(1,len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next
        return head
            
            
        