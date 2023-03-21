class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # the 2 rules we must follow is
            # open and close paratheses must be max count of n 
            # close must be smaller (<) than open count. you can add as many opening parentheses as you want (as long as count is under n)


        # doing this recursively...
            # only add paranthesis if open < n
            # only add a closing paranthesis if closed < open
            # valid IIF open == closed == n

        stack = []
        output = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                output.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return output


'''
https://leetcode.com/problems/generate-parentheses/

oh man I hated this problem...

1. Define a class called Solution, with a method called generateParenthesis that takes an integer n as input and returns a list of strings.
2. Define two rules for generating the parentheses - open and close parentheses must be the maximum count of n and close parentheses must be smaller than the open parentheses count.
3. Initialize an empty stack and an empty list called output.
4. Define a recursive function called backtrack that takes two arguments - openN and closedN.
5. Check if openN and closedN are both equal to n, if so, join the stack into a string and append it to the output list.
6. If openN is less than n, append an opening parenthesis to the stack and call the backtrack function again with openN + 1 and closedN.
7. Remove the last item from the stack (which is the opening parenthesis).
8. If closedN is less than openN, append a closing parenthesis to the stack and call the backtrack function again with openN and closedN + 1.
9. Remove the last item from the stack (which is the closing parenthesis).
10. Call the backtrack function with initial values of 0 for both openN and closedN.
11. Return the output list of valid parentheses strings.

'''
