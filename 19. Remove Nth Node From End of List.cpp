Problem: '''19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''
  
  Code:  
    
    
    class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* cur = head;
        ListNode* pre = &dummy;
        
        while (n > 0)
        {
            cur = cur->next;
            --n;
        }
        

        while (cur != nullptr && pre != nullptr)
        {
            cur = cur->next;
            pre = pre->next;
        }
        
        pre->next = pre->next->next;
        
        return dummy.next;
    }
};
