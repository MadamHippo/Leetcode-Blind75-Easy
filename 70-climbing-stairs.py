        # https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Top down w/o memorization is O(2^n) which is not good bc we're repeating too much resolving subproblems. Top down is going from n down to 0.        
    
        
        # Bottom Up solution (starting at 0 and going to n) w/ memo-ization
        
        # O(n) solution
        
        if n == 1:
            return n
        
        if n == 2:
            return n
        
        # initalize to 1 instead of 0 because we're starting at base case of 1, 1 with 2 variables.
        # In an array 0 = 1, and 1 = 1.
        prev1, prev2 = 1, 1
        
        # Temp memorization
        temp_save = 0
        
        # we're swapping variables
        for i in range(1, n):
            temp_save = prev1 + prev2
            prev1 = prev2
            prev2 = temp_save
            
        return temp_save
    
    '''
  
    Try to solve things bottom up, start by thinking about the base case
    
    We're dealing with stairs, so how much work is there to climb 0 stairs? None! 1 stair? 1! 2 stairs? 2! 
    
    3 stairs? It's your prev 2 answers added. 4? It's your prev answers added.
    
    '''
