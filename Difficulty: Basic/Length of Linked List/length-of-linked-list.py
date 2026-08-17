''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        temp = head
        cnt = 1
        if head == None: return 0
        while temp.next is not None:
            cnt += 1
            temp = temp.next
        return cnt