# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None or l2 == None:
            return l1 or l2
        
        if l1.val <= l2.val:
            head = tail = l1
            l1 = l1.next
        else:
            head = tail = l2
            l2 = l2.next
            
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        
        tail.next = l1 or l2
        
        return head