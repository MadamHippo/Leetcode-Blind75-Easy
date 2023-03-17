class Solution(object):
    def isValid(self, string):
        """
        :type s: str
        :rtype: bool
        
        Runtime O(n) 
        n is number of characters in our string...
        
        Space O(n)
        
        """
        # using Stack is key
        
        # using Hashmap to keep track of all types of parathesis
        
        # Adding a dummy 0 means we don't need to check if stack is empty or not!
        
        # empty stack with a dummy 0 
        stack = [0]
        
        # create a dict/hash with all parathesis paired as corresponding open & close as key/value
        mapping = {0: None, '(':')', '[':']', '{':'}'}
        
        # go through each character in string
        for char in string:
            
            # if character is found in Hash's KEY.
            # fast key lookup if you don't write dict.values() because they're linear scans with comparison
            if char in mapping:
                # if char exists in mapping, add it to stack
                stack.append(char)
            elif mapping[stack.pop()] != char:
                return False
                # if char not in stack...
                
                # last item on stack does NOT map to character in hash then..return false
            
        return stack == [0]
