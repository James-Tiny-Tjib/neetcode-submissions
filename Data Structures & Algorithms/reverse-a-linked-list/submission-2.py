# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        
        cur = head.next
        head.next = None

        while (cur is not None):
            temp = cur.next
            cur.next = head
            head = cur
            cur = temp

        
        return head
            
            


        