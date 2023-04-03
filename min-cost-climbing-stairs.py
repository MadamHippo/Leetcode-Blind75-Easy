class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        '''
        another dp problem: If you're answering problems more than once, thats not good, so use space and use a answer you already calculated and save it for use later.
        
        
        Imagine a stair case step with a price tag. If you use that step, you need to pay that bill.
        Some steps have smaller bills, some larger
        We want to find what is the cheapest way we can get to get pass those stairs
        
        We can choose to start at index 0 or 1 so that means we are looking forward to the next steps and constantly comparing the 2 future steps.
        
        So create 2 variables that start both at 0.
        
        Use a for loop to iterate through the indexes in cost:
        
        calculate the cost[i] + smaller one of either 1 step ahead, or 2 ahead.
        
        "increment" by swapping variables to both next1 and next2. Next2 is now total cost.
        
        
        '''
        
        
        next1, next2 = 0, 0
        
        
        for i in range(len(cost)):                      # [10, 15, 20, 25]
            total_cost = cost[i] + min(next1, next2)
                                                        # total_cost = 10 + 0 = 10
                                                        # total_cost = 15 + 0 = 15
                                                        # total_cost = 20 + 10 = 30
                                                        # total_cost = 25 + 15 = 40
            next1 = next2 
            next2 = total_cost

                                                        # N1 and N2 are price tag sums possible of steps to get to top of stairs. 
                                                        # Return the minimum cost to reach the top of the floor.
        return min(next1, next2)
