class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # choose a hashset because looking up the number takes O(1) time.
        # Array and List takes O(n) time.

        # HELPER FUNCTION:
        def get_next_digit(n):
            digit_sum = 0

            # if n isn't 0...separate each digit and add it up, and that will become your new number
            while n != 0:
                next_digit = n % 10
                n = n / 10
                digit_sum += next_digit * next_digit
            return digit_sum

        # create a set storing uniquely seen numbers...
        hashset = set()

        # as long as n isn't 1 and is NOT in the set...add it to the set and move onto the next number using Helper Function
        while n != 1 and n not in hashset:
            hashset.add(n)
            n = get_next_digit(n)

        # otherwise return True since n is a happy number
        else: 
            return n == 1

