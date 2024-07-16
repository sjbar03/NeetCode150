# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head == None:
            return None

        curr = head
        orig, n = [], []
        i = 0

        while curr:
            orig.append(curr)
            n.append(Node(curr.val, next=None, random=None))
            curr = curr.next
            i += 1
        
        for i in range(len(n) - 1):
            n[i].next = n[i+1]

        for i in range(len(orig)):
            print(orig[i].random)
            if orig[i].random:
                loc = orig.index(orig[i].random)
                n[i].random = n[loc]
        
        return n[0]

