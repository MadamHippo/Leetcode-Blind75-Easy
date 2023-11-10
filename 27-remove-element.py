# Problem https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        '''     
        # nums = [0,1,2,2,3,0,4,2]
        # val = 2
        # desire output = 5, nums = [0,1,4,0,3,_,_,_]
        
        
        while val in nums:
            if val in nums:
                nums.remove(val)
        return len(nums)
        
        '''
        
        i = 0

        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
    
    
    
        '''        
        # the more official way:
        
        if len(nums) == 0:
            return None
        
        # j is count
        j = 0
        
        for num in nums:
            if num != val:
                # put valid elements to the front and modifies the values to make sure all the allowed elements are in the right place all upfront.
                nums[j] = nums[num]
                j+=1
                # or if it DOES equal val, we want to just skip it with the j pointer by +1
        return j
        
        '''
