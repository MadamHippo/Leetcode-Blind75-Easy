# Definition for singly-linked list.


# https://leetcode.com/problems/reverse-linked-list/


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        
        """
        :type head: ListNode
        :rtype: ListNode
        
        helpful tutorial video for recursive solution: https://www.youtube.com/watch?v=MRe3UsRadKw
        
        """
        # Recursive solution

        if not head:
            return None

        # Make variable to maintain new head...initially set to head

        newHead = head

        # If head.next is not Null (still exists a subproblem) then we reverse List
        if head and head.next:
            # call reverseList with head.next so you can find the end of the linkedlist and make that the new head!!! This is how we recursively traverse the list until we found the last node.
            newHead = self.reverseList(head.next)
            
            # confusing but explanation is, we are at end of the linked list so head.next.next is now Null which means the pointer pointing to Null can be manipuated and turned to point at curr instead -- effectively reversing the linked list.
            head.next.next = head
        
        # now set head.next to Null 
        # go back to the start of the callstack if head and head.next:
        # If head happens to be the first node in the list, we need to reverse the next pointer to Null indicating this is the new end of LinkedList that points to null.
        head.next = None
    
        return newHead


        # -> 1 -> 2 -> 3
        
        
        
    ''' 
        # Iterative Solution
        
        if not head:
            return None
        
        prev = None
        cur = head
        
        while cur:
            # saving next node so we don't lose it when we move cur's pointer...
            saveNext = cur.next
            
            # switching the cur.next's pointer to the one before it (not afraid to lose cur.next bc we already saved it)
            cur.next = prev
            
            # incrementing prev to cur (moving forward by 1)
            prev = cur
            
            # incrementing cur also forward by 1
            cur = saveNext
        return prev
    
    # gif animation for clarity: https://media.geeksforgeeks.org/wp-content/cdn-uploads/RGIF2.gif
    
    '''
