Problem:'''1175. Prime Arrangements
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 
 '''
  Solution:
    class Solution:
    def numPrimeArrangements(self, n: int) -> int:
	
        count, fact1, fact2, g = 1, 1, 1, 1000000007
        
    #calculate number of prime and non-prime numbers
        
        for i in range(3,n+1):
            count += 1
            for j in range(2,i-1):
                if i % j == 0:
                    count -= 1
                    break
        m = n - count
        if m > count:
            m, count = count, m
    
    #calculate the factorials
    
        for i in range(1,count+1):
            fact1 *= i
            if i == m:
                fact2 = fact1
                
    #mod operation
    
        return ((fact2 * fact1) % g)
