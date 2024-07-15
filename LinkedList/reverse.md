# Reverse Linked List

## Intuition
This problem is simple to imagine, each node in the list will be modified so
that it's next pointer will point to the node that originally preceeded it. 

## Approach
We can "iterate" over the original linked list. On each node, we need to
save the next node before we overwrite it. We save it in nxt, then we modify
curr.next to be the node currrently saved as prev (if prev == None, this node is
the new tail). Before continuing on to the next node in the iteration, we change
prev to curr, then curr to nxt.

## Time Complexity
We iterate over this list once.
***O(n)***

## Space Complexity
Only three variables are created, regardless of the size of the list.
***O(1)***
