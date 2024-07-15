# Reorder Linked List
## Intuition
It will be helpful to keep a reference to each node, so that we can access it
later in **O(1)** time. Therefore we transform the linked list into an array,
then iterate over the references in the arry. By doing this, we can easily jump
around the singly linked list instead of having to loop from the beginning each
time we want a new reference.
## Approach
First, place each node into an array at its corresponding index in the linked
list. Then, iterate over the first half of this array, and append each node,
and the node at its negative index in the arry to a dummy linked list. Finally,
if the linked list is an odd length, append the middle element to the end of the
list. Return the dummy list.
## Time complexity
We iterate over the list a maximum of two times, so it is ***O(n)***
## Space complexity
We allocate an array of the same size as the linked list, so it is ***O(n)***
