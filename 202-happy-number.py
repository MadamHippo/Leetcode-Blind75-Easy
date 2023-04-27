# Literally still do not understand this... https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:

        # keep track of number we visited in hashmap in constant speed
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        return False

    # helper function
    
    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            # mod for the last place number
            digit = n % 10
            # squaring in py
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
