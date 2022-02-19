Problem: '''414. Third Maximum Number
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.


'''
  class Solution:
    def thirdMax(self, n: List[int]) -> int:
        p1=list(set(n))
        if len(p1)<=2:
            return max(p1)
            
        else: 
            p=sorted(p1)
            return p[-3]
        
        
        
        
        
