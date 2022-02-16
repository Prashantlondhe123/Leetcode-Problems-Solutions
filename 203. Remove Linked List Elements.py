Problem : 203. Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []



class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            if curr.val == val:  # cases 1-3
                if prev:  # cases 1-2
                    prev.next = curr.next
                else:  # case 3
                    head = curr.next
                curr = curr.next  # for all cases
            else:  # case 4
                prev, curr = curr, curr.next
        return head
