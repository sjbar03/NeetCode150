# Copy Linked List with Random Pointer
## Intuition
To make a deep copy, we must ensure we are not reusing any of the pointers from
the original linked list. Every element must be explicitly created. Further, the
next and random pointers need to point to brand new nodes as well.  
Two main problems we need to solve are: there can only be n nodes in the new
list, and each pointer has to point to the correct node. We cannot simply create
all new nodes.
## Approach
We tackle this problem in two loops over the nodes.  
1. On the first loop, we create a copy of the nodes and place them into an array. We leave the the random pointer as none for now.
2. The second loop finds the index of the random pointer for each node in the
original array, then links the corresponding node in the new array to the new
node. This ensures no duplicate nodes are created and the deep copy has the same
wiring as the original.
## Time Complexity
We loop over the linked list three times, ***O(n)***
## Space Complexity
We allocate two new arrays with n elements, ***O(n)***
