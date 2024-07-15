# Duplicate Integer
# Given an integer array nums, return true if any value appears more than
# once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         s = set(nums)
         return len(s) == len(nums)

# SOLUTION:
# By casting nums to a set, all duplicates will be removed. If the set is
# shorter than nums, an element must appear more than once.