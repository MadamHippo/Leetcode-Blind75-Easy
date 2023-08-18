# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # sliding window, runtime = O(n), space = O(n)


        # initalizing a set to make sure we have all our characters stored
        characterSet = set()

        # we need two pointers for sliding window...
        leftPointer = 0
        rightPointer = 0

        # we need to initialize a return value 
        result = 0

        # right pointer will go through every character...
        # if we get to a duplicate character, we need to update our window and also character set...so that's rightPointer's job
        for rightPointer in range(len(s)):
            while s[rightPointer] in characterSet:
                # remove the left's value in the characterSet...
                characterSet.remove(s[leftPointer])
                # close up the left's sliding window
                leftPointer += 1
            # add the right Pointer's value instead to the set...and repeat the loop
            characterSet.add(s[rightPointer])



            # calculating which has the longest window so far...so it would compare result originally at 0 to any size window between left and right pointers.
            result = max(result, rightPointer - leftPointer + 1)
        
        return result
