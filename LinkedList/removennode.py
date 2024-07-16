# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        leading = trailing = dummy
        i = 0
        while leading.next != None:
            if i >= n:
                trailing = trailing.next
            leading = leading.next
            i += 1
        trailing.next = trailing.next.next
        return dummy.next
