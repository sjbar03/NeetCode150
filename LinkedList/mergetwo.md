# Merge Two Lists
## Intuition
We know this problem can be solved in linear time, the main problem is keeping
track of the necessary positions and list-states.
## Approach
We save the smaller of the heads of the two lists as 'head', this will be the
value we return after we are done. We then loop as long as both lists still
exist. On each iteration, we compare the head of each list and append the
smaller one to curr.
### Making Progress
On each iteration, we must chop the head off of whichever list has the smaller
head. This is how we approach the end of the loop. We also must increment curr
to curr.next after assigning curr.next.
### Ending the Loop
Once we've exhausted either or both of the lists, we have to do one final
conditional append to ensure items are not left behind.
## Time Complexity
We loop over each item in each list once. ***O(n)***
## Space Complexity
We allocate space for a third linked list that serves as an allocator.
***O(n)***
