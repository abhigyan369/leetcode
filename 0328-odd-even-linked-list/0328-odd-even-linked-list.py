# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head

        odd = head
        even = head.next
        evenhead = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = odd.next
        odd.next = evenhead
        return head

        
            
