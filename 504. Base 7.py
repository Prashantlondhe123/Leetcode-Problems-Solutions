Problem: '''504. Base 7
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 '''
  class Solution:
	def convertToBase7(self, num: int) -> str:
		n, result = num, ""

		if num == 0: return "0"

		if num<0: 
			num = -num

		while num:
			result += str(num%7)
			num = num // 7

		return result[::-1] if n >= 0 else "-" + result[::-1]
