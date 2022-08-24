'''

You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record. The test cases are generated so that the answer fits in a 32-bit integer.


Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.

'''



#### PYTHON


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
       
        
        """
        
        # Using stack = O(n) space
        # Time = O(n) time
        
        #### PYTHON ####
        stack = []
        
        for op in ops:
            if op == "+":
                stack.append(stack[-1]+stack[-2])
            
            elif op == "D":
                stack.append(stack[-1]*2)
                
            elif op == "C":
                stack.pop()
                
            else:
                stack.append(int(op))
                
        return sum(stack)
