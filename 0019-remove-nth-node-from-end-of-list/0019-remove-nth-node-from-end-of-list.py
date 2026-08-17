# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: return None
        cnt = 0
        temp = head
        while temp is not None:
            cnt += 1
            temp = temp.next
        
        iteration = cnt - n
        if iteration == 0:
            return head.next
        curr = head
        prev = None
        for _ in range(iteration):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head