problem: '''653. Two Sum IV - Input is a BST3
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false



'''
  
  class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.helper(root, k, set())
        
    def helper(self, root, k, seen):
        if not root:
            return None
        if (k - root.val) in seen:
            return True
        seen.add(root.val)
        left = self.helper(root.left, k, seen)
        right = self.helper(root.right, k, seen)
        
        return left or right
