Problem:'''Day of the Week
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"

'''
  
  
  Solution:
    from datetime import date
class Solution:
    d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return Solution.d[date(year, month, day).weekday()]
