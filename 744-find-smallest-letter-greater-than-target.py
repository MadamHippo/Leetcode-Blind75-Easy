class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        
        # TRICKY!!!
        
        # Log(N)
        
        # Return smallest CHARACTER (not index)
        
        
        
        """
        # to handle the wrap around, we'll set result's default to the first letter of the character array
        result = letters[0]
        
        # perform regular binary two-pointer search...
        n = len(letters)
        left_pointer = 0
        right_pointer = n - 1
        
        
        while left_pointer <= right_pointer:
            
            mid_point = (left_pointer + right_pointer) // 2
            
            # tweaked binary search to return the smallest letter greater than target
            if letters[mid_point] <= target: # if value at midpoint is smaller or equal to target....
                left_pointer = mid_point + 1 # move left_pointer to mid + 1 to shrink and close in on the target AND move left_pointer forward to get out of the While loop eventually
            
            elif letters[mid_point] > target:
                
                result = letters[mid_point]
                # reassign new mid point value to result as you calcuated above with the new Left and Right values so you can return accurately later.
                
                right_pointer = mid_point - 1
                # shrinking the right_pointer to close in, then recalcuate the result again until we find == target and just return it.
                # AND move right pointer back to get out of the While loop eventually
                
        
        return result
    
