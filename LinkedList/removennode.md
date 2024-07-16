# Remove Node From End Of Linked List
## Intuition
Immediately, we know we need to find a way to locate the nth node from the end
of the list. Because this is not a doubly linked list, we cannot navigate
backwards, and since it is not an array, we cannot use indexes. Ideally, we
should find a way to locate this node after a single iteration through the list.
  We can keep two references, one to a 'leading node' and the other to a
  'trailing node'. While iterating over the list, once trailing is n nodes
  behind leading, we start incrementing trailing as well. When leading reaches
  the last node, trailing will be on the nth node from the end.
## Approach
We keep four references total, one to a dummy node prepended to the linked list,
one for a leading node, one for a trailing node, and the last for the index. We
initialize leading and trailing to the dummy node (doing this solves the issue
of removing the first node in the list). We initialize the index var to 0, and
then begin our iteration. On each iteration, we check if index is greater than
or equal to n yet. If it is, we increment both leading and trailing. Otherwise,
we only increment leading and the index var. Once leading reaches the end,
trailing holds a reference to the node immediately before the nth node from the
end. We can do a simple linked list node removal:
    trailing.next = trailing.next.next
## Time Complexity
We iterate over the linked list once ***O(n)***
# Space Complexity
We create 4 new references regardless of the size of the list ***O(1)***
