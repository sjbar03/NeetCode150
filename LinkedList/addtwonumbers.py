# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode()
        carry = 0
        while l1 or l2:
            l1_val = l2_val = 0

            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            
            s = l1_val + l2_val + carry
            digit = s % 10
            carry = (s - digit) // 10

            curr.next = ListNode(val=digit)
            curr = curr.next
        
        if carry > 0:
            curr.next = ListNode(val = carry)
        
        return dummy.next
