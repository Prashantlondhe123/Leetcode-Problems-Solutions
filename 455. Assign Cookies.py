Problem:    '''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and 
the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
'''
  
  
Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.




#Code:

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        i = len(g) -1
        j = len(s) - 1
        while i >= 0 and j >= 0:
            if s[j] >= g[i]: #satisfy this child
                res += 1
                i -= 1
                j -= 1
            else: # cannot satisfy this child, so pass this cookie to another child who have less content
                i -= 1
        
        return res
        
