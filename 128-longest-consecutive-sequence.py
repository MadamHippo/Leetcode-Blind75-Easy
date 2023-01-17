# Problem link: https://leetcode.com/problems/longest-consecutive-sequence/description/
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Linear time, linear space -- O(n)
        numSet = set(nums)

        longestSoFar = 0

        for n in nums:
            # check if its the start of a sequence by checking the left neighbor
            if (n-1) not in numSet:
                # if it doesn't have a left neighbor then it is the start...
                length = 0
                while ( n + length) in numSet:
                    length += 1
                longestSoFar = max(length, longestSoFar)
        return longestSoFar
