''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = head
        fast = head
        cnt = 1
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # cycle detected
                
                temp = slow
                while temp.next != slow:
                    temp = temp.next
                    cnt += 1
                return cnt
        return 0