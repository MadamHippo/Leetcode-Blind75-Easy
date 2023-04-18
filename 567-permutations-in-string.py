// notes needed
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
