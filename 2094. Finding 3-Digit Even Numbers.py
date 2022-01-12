#Problem:  2094. Finding 3-Digit Even Numbers
          '''You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.'''
  
  
  
Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.



#code:

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output = set()
        for n in itertools.permutations(digits, 3):
            if n[0] != 0 and n[2] % 2 == 0:
                output.add(n[0] * 100 + n[1] * 10 + n[2])
        output = list(output)        
        output.sort()
        return output
