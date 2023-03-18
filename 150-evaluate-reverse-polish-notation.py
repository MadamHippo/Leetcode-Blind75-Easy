# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # space O(n)  time O(n)

        stack = []

        for character in tokens:
            if character == "+":
                stack.append(stack.pop() + stack.pop())
            elif character == "-":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 - val1)
            elif character == "*":
                stack.append(stack.pop() * stack.pop())
            elif character == "/":
                val1, val2 = stack.pop(), stack.pop()
                # decimal division:
                # stack.append(val2/val1)
                # but we want to round it to zero like problem statement says so we use the int function to round it to zero 
                stack.append(int(val2/val1))              
            else:
                stack.append(int(character))
        
        # return top of stack
        return stack[-1]
