/*
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

https://leetcode.com/problems/detect-capital/
*/


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if len(word) <= 0:
            return True
        
        elif word.upper() == word:
            return True
        
        elif word.lower() == word:
            return True
        
        elif word[0].upper() == word[0] and word.lower()[1:] == word[1:]:
            return True
        
