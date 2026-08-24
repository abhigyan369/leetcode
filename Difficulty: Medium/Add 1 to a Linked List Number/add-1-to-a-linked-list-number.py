class Solution:
    def reverse(self, head):
        temp = head
        prev = None
    
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
    
        return prev
    
    def addOne(self, head):
        head = self.reverse(head)
    
        temp = head
        carry = 1
    
        while temp is not None:
            temp.data += carry
    
            if temp.data < 10:
                carry = 0
                break
            else:
                temp.data = 0
                carry = 1
    
            temp = temp.next
    
        if carry == 1:
            newNode = Node(1)
            head = self.reverse(head)
            newNode.next = head
            return newNode
    
        return self.reverse(head)