"""
You are given a String called S.

OK so the secret sauce is using a Dictionary and a Stack.

Add the opening and closing parens as keys: values to the Dictionary.

Create an empty stack to keep order.

Go thru each character in the String S.
    Does this character match a Key in the dictionary?
        Yes -> then append it to the stack.
        
        No -> then this character doesn't match a key in the dictionary...so it must be a closing paren
            so pop the top of the stack (IF a stack exists that is)
            does what popped off the stack (an open paren) correlate to the correct closing paren character?
                -> If yes, continue
                -> If No, return false
                
 Now just check at the end of it all, is your stack empty? IF it's empty it, return True it was all valid parens.
            
    

"""



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


