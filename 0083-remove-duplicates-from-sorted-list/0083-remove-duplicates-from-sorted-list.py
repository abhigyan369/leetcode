# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## using 2 pointer, i will stay at uniq value and j will iterate and find uniq for i
        if head is None:
            return head
        i = head
        j = head.next

        while j is not None:
            if j.val != i.val:
                i.next = j
                i = j
            j = j.next
        i.next = None
        return head

            