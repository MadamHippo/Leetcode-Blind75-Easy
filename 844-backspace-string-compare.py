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
        # Using stacks to handle backspaces efficiently
        # This algorithm has a time complexity of O(n) and a space complexity of O(n).

        # Initialize two empty stacks, one for each input string
        stack = []
        stack1 = []

        # Iterate through the characters in the first input string 's'
        for i in s:
            if i != "#":
                # If the character is not a backspace ('#'), push it onto the stack
                stack.append(i)
            elif i == "#" and len(stack) != 0:
                # If the character is a backspace and the stack is not empty,
                # pop the top element from the stack, effectively simulating the backspace behavior
                stack.pop()

        # Repeat the same process for the second input string 't'
        for i in t:
            if i != "#":
                stack1.append(i)
            elif i == "#" and len(stack1) != 0:
                stack1.pop()

        # Finally, compare the two stacks. If they are equal, the strings are considered equal
        if stack == stack1:
            return True
        return False
