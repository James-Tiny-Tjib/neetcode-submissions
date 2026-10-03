# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        # Set the head:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            if list1.val > list2.val:
                head = list2
                list2 = list2.next
            else:
                head = list1
                list1 = list1.next
            cur = head


        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next    
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next 

        cur.next = list1 if list1 else list2                       
        

        return head
                