class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB
        cnt1, cnt2 = 0, 0

        # Count nodes in headA
        while temp1 is not None:
            cnt1 += 1
            temp1 = temp1.next

        # Count nodes in headB
        while temp2 is not None:
            cnt2 += 1
            temp2 = temp2.next

        # Start pointers at the heads
        c1 = headA
        c2 = headB

        # Move the pointer of the longer list ahead
        if cnt1 > cnt2:
            for _ in range(cnt1 - cnt2):
                c1 = c1.next
        else:
            for _ in range(cnt2 - cnt1):
                c2 = c2.next

        # Move both pointers together
        while c1 is not None and c2 is not None:
            if c1 == c2:
                return c1

            c1 = c1.next
            c2 = c2.next

        return None