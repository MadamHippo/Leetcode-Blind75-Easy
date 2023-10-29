# Problem: https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # Run time: Big O(26*n)
        # Sliding window

        # to count each character we are using hashmap
        count_hashmap = {}
        result = 0

        leftPointer = 0
        for rightPointer in range(len(s)):
            # adding 1 to count if it exists (otherwise, count.get returns 0)
            count_hashmap[s[rightPointer]] = 1 + count_hashmap.get(s[rightPointer], 0)

            # take length of window subtracted by count of most frequent character (going thru hash map and getting the max value from the hash map)
            while (rightPointer-leftPointer + 1) - max(count_hashmap.values()) > k:

                # take the count of the character at the left position and decrease it by 1 (so we can get the updated correct max for result)
                count_hashmap[s[leftPointer]] -= 1

                # close the sliding window from the left if number of replacement is greater than k
                leftPointer += 1

            result = max(result, rightPointer-leftPointer + 1)

        return result


