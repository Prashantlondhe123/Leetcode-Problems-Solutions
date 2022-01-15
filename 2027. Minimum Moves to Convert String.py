Problem: '''2027. Minimum Moves to Convert String

You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.


Example 1:

Input: s = "XXX"
Output: 1
Explanation: XXX -> OOO
We select all the 3 characters and convert them in one move.


Example 3:

Input: s = "OOOO"
Output: 0
Explanation: There are no 'X's in s to convert.




Code:
'''
  class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        idx = 0 
        res = 0 
        while idx < n:
            if s[idx] == 'O':
                idx += 1
            else:
                res += 1
                idx += 3
        return res 
