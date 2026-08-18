''' Structure of Linked List Node
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val
'''

class Solution:
    def removeLoop(self, head):
        # code here
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # cycle detected
                # find starting point of the cycle
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                # last point of the cycle
                temp = slow
                while temp.next != slow:
                    temp = temp.next
                
                temp.next = None # cycle removed
                return head
        return head