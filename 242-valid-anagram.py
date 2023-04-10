class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        https://leetcode.com/problems/valid-anagram/
        
        Anagram means all letters of a word makes up another word
        
        
        
        Solution1:
        
        Dict...good but uses extra memory.
        
        using dicts and comparing the dicts using the counts of each character...
        find the length of the string first before hash map stuff since we can just do 1 hash instead of 2.
        
        Time O(n)
        
        Space O(s+t)
        
        Basically write out your own sorting function instead of built in sort or counter.
        
        1. Check string length, and return immediately if it's not same length since they can't be Anagrams.
        
        2. Create 1 dict for s and 1 dict for t that keeps count
        
        3. iterate through length of string s
            countS
        
        
        
        '''
                
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}
        
        for i in range(len(s)): # using index i for both strings since both strings is same length
            # count occurance of each character in s...this is the key of the hashmap, and each time we see that character we increase the count by 1
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            # if dict_s' s[i] doesn't exist, you get 0
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)
            # same thing with dict_t
            
        for character in dict_s: #character is the key in dict
            if dict_s[character] != dict_t.get(character, 0):
                # you still have to use a .get() to guard no default functions
                return False
            
        return True
