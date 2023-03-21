# https://leetcode.com/problems/backspace-string-compare/description/

'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

'''

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # using stacks 
        #O(n) time and O(n) space
        
        stack = []
        for i in s:

            if(i!="#"):
                stack.append(i)
            elif(i=="#")and (len(stack)!=0):
                stack.pop()

        stack1 = []

        for i in t:
            if(i!="#"):
                stack1.append(i)
            elif(i=="#")and (len(stack1)!=0):
                stack1.pop()


        if(stack==stack1):
            return True
        return False
