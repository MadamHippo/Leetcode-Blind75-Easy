###
def checkInclusion(s1, s2):
    if len(s1) > len(s2):  # Checks if s1's length is greater than s2, return False if so
        return False

    s1_chars = [0] * 26  # Initializes an array to count occurrences of characters in s1 (assuming lowercase English letters)
    s2_chars = [0] * 26  # Initializes an array to count occurrences of characters in the sliding window of s2

    # Count occurrences of characters in the first window of s2 with the length of s1
    for i in range(len(s1)):
        s1_chars[ord(s1[i]) - ord('a')] += 1  # Increment the count of the character in s1
        s2_chars[ord(s2[i]) - ord('a')] += 1  # Increment the count of the character in s2

    # Slide a window through s2 and compare the character counts to that of s1
    for i in range(len(s1), len(s2)):
        if s1_chars == s2_chars:  # If the character counts match, return True (found a permutation)
            return True

        # Slide the window by moving the right pointer forward and updating character counts accordingly
        s2_chars[ord(s2[i]) - ord('a')] += 1  # Increment count for the new character
        s2_chars[ord(s2[i - len(s1)]) - ord('a')] -= 1  # Decrement count for the character that's no longer in the window

    return s1_chars == s2_chars  # Check if the final character counts match after the loop
###
// https://leetcode.com/problems/permutation-in-string/submissions/

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_chars = [0] * 26
    s2_chars = [0] * 26

    for i in range(len(s1)):
        s1_chars[ord(s1[i]) - ord('a')] += 1
        s2_chars[ord(s2[i]) - ord('a')] += 1

    for i in range(len(s1), len(s2)):
        if s1_chars == s2_chars:
            return True

        s2_chars[ord(s2[i]) - ord('a')] += 1
        s2_chars[ord(s2[i - len(s1)]) - ord('a')] -= 1

    return s1_chars == s2_chars
