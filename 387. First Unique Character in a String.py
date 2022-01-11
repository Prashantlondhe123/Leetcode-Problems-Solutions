#Problem :    387. First Unique Character in a String
#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
    Input: s = "leetcode"
    Output: 0
      
Example 2:
    Input: s = "loveleetcode"
    Output: 2


#code:
1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1    
    
    
    
    
 2)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=list(s)
        for i in l:
            if l.count(i)==1:
                return l.index(i)
                break
            
        return -1    
        


