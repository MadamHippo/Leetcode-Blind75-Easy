// 14	Longest Common Prefix	https://leetcode.com/problems/longest-common-prefix/	String 

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
    
                    
        
        1. initalize an empty string for storing result
        
        2. go through each index in the length of the first string in the array (aka strs[0]) - this is chosen arbitararily. 
                This first string may not be the shortest length of word but we handle that case later.
        3. Now loop through each string in the array inside the first for loop. 
                This line compares the first string's max index number to the length of the rest of the array of strings. When there's enough index to match the length of string, the loop will continue. If not it will return output because we have the shortest word which limits longest common prefix.
                
        4. Otherwise, just check if string's index value matches Array's first string's first index value. If not, just return output.
                
        5. Important to UPDATE the output always and consistently. for whenever the for loops are ready to return the result.
                

        Run time: O(n*m)

        """
        output = ""
        
        for index in range(len(strs[0])): # strs[0] is Flower. Index starts at F.
            
            for word in strs: #Now loop through each word in the strs inside.
                
                if index == len(word): # if index (which is 0 for the first run) is the same length as len(string) also 0...then it's empty so return empty Output.
                    # this line compares the first string's max index number to the length of the rest of the array of strings. 
                    # When there's enough index to match the length of string, the loop will continue. 
                    # If not it will return output because we have the shortest word which limits longest common prefix.
                    return output
                
                if word[index] != strs[0][index]: # elif word value..."F" in this case...doesn't equal Array string's first index value...then just return output.
                    return output
                
            output += strs[0][index] 
            #IMPORTANT! Outside the second for loop, remember to add Array's new values to the output so the output is updated for whenever it's ready to return the result.
            
            # Now the for loop will run until it's out of the length of strs...
            
        return output
    
'''

in an IDE editor -- you need to call the class, and then enter the function definition + data:
    
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))

in an IDE editor, if it's not a class but jsut a simple def:

print(longestCommonPrefix(["flower","flow","flight"]))

'''
