Problem:'''912. Sort an Array.py


Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

'''
  
  class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        p=sorted(nums)
        return p
        
