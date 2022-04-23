Problem:'''
1037. Valid Boomerang
  Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

 

Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false
  
  
  '''
  
  class Solution:
    def isBoomerang(self, P: List[List[int]]) -> bool:
        return (P[2][1]-P[1][1])*(P[0][0]-P[1][0])!=(P[2][0]-P[1][0])*(P[0][1]-P[1][1])
