# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        nxt, arr = head, []

        while nxt:
            arr.append(nxt)
            nxt = nxt.next

        dummy = curr = ListNode()
        
        for i in range(len(arr) // 2):
            curr.next = arr[i]
            curr = curr.next
            curr.next = arr[0 - (i + 1)]
            curr = curr.next
          
        if len(arr) % 2 == 1:
            curr.next = arr[len(arr) // 2]
            curr = curr.next
    
        curr.next = None
        return dummy.next

ex = ListNode(val=2, next = ListNode(val = 4, next= ListNode(val = 6, next=
                                                             ListNode(val= 8,
                                                                      next=ListNode(val=10)))))
sol = Solution()

nxt = sol.reorderList(ex)
while nxt:
    print(nxt.val)
    nxt = nxt.next
