Problem:'''2176. Count Equal and Divisible Pairs in an Array
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
 

Example 1:

Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

'''
  class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if k==1 :
            mp=Counter(nums)
            return sum((mp[k]*(mp[k]-1))//2 for k in mp.keys())
        ans=nums.count(nums[0])-1
        n=len(nums)
        for i in range(k,n**2,k):
            x=1
            while x*x <= i :
                ans+=(i%x==0 and i//x < n  and x<n and x*x!=i and nums[x]==nums[i//x])
                x+=1
        return ans
