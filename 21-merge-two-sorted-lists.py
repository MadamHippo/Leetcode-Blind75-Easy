# Definition for singly-linked list.

# https://leetcode.com/problems/merge-two-sorted-lists/description/


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # must use original node, can't make copies
        
        # create dummy node to prevent edge cases of an empty list
        dummy = ListNode()
        
        #create tail that is dummy
        tail = dummy
        
        while list1 and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                #now adjust the pointer:
                list1 = list1.next
            else:
                tail.next = list2
                #now adjust the pointer:
                list2 = list2.next
            # update tail pointer (done regardless of conditional)
            
            tail = tail.next
            
            # you can't just return dummy right now bc one of the list could still have values
        if list1 is not None:
            tail.next = list1
        elif list2 is not None:
            tail.next = list2
                
        return dummy.next
