Problem :  ''' 500. Keyboard Row
              Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".



'''
  
  Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
  
  
  
#code:

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first, second, third, rlist = 'qwertyuiopQWERTYUIOP', "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM", []
        for word in words:
            one, two, three = 1, 1, 1
            for letter in word:
                #print(letter, word)
                if letter not in first:
                    one = 0
                if letter not in second:
                    two = 0
                if letter not in third:
                    three = 0
            if one or two or three:
                rlist.append(word)
        return rlist
