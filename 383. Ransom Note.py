Problem :'''383. Ransom Note
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
'''
  class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		for i in ransomNote:
			if i in magazine:
				magazine = magazine.replace(i, "", 1)
			else:
				return False
		return True
