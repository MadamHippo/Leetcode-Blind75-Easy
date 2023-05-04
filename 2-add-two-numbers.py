# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, list1, list2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        
        Approach:
        
        O(N) time & space
        
        Traverse these lists at the same time. If 1 list is less digits, then use 0.
        
        
        """
        
        dummy = ListNode(0)
        list3_output = dummy
        
        carry = 0
        
        while list1 or list2 or carry:
            # teriraray condition, if no list1/list2 anymore, just use 0
            value1 = list1.val if list1 else 0
            value2 = list2.val if list2 else 0
            
            # new digit
            current_sum = value1 + value2 + carry
            
            carry = current_sum // 10
            
            # if value greater than 10 and we want only the last digit...we need to mod it by 10. ie 44 % 10 = 4
            last_digit = current_sum % 10 
            
            list3_output.next = ListNode(last_digit)
            
            # update pointers
            list3_output = list3_output.next
            
            # 
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
            
        # reference to our dummy head of new list
        return dummy.next
