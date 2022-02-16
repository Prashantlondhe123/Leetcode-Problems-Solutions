Problem: '''83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 
 
 
 '''
  
  
  class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head
        if head == None:
            return head
        while cursor.next is not None:
            if cursor.next.val == cursor.val:
                # delete duplicate node
                new_next = cursor.next.next
                del cursor.next
                cursor.next = new_next
            else:
                cursor = cursor.next
        return head
