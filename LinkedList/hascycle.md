# Has Cycle Linked List

## Intuition

My first thought was to track which nodes I've seen, and if I find a match
return true. This is not the most memory efficient method but it is the most
straightforward.

## Approach

Iterate over the linked list, storing each node in a set. Before storing the
node, check if it is already in the set. If it is, return true (there is a
cycle). Otherwise, continue on.

## Time Complexity

We iterate over the list once. The time complexity of a set lookup is **O(1)**.
Therfore the total time is ***O(n)***

## Space Complexity

We allocate a set that might have n elements in the worst case -> ***O(n)***
