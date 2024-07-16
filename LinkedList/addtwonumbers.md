# Add Two Numbers - Linked List
## Intuition
The linear-time solution to this problem is easy to understand if you understand
long-addition. The algorithm is exactly the process we all learned in first
grade. The linked lists being 'reversed' may seem intimidating at first, but it
makes it simpler as we normally add from right to left regardless.
## Approach
We initialize a dummy node to chain the solution onto as we generate it. As we
iterate over each node, we add the two values together and calculate the
remainder, and the carry digit. We create a ListNode with the remainder as its
value, and chain it to the dummy node. This is our one's digit. The carry is
added to the sum of the nodes in the next iteration. This continues until both
lists are exhausted. If carry is not zero after the loop ends, this is called a
*carry-out*. We just add another node to the end of the list as our most
significant digit.
## Time complexity

We iterate over the list one time, and do a constant amount of work in each
iteration -> ***O(n)***

## Space complexity

We generate a new linked list to build our resultant number -> ***O(n)***
