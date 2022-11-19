'''

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

HINT1: In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.

HINT2: A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.


'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        right = 0
        
        while left<len(nums) and right<len(nums):
            # when both are zero:
            if nums[left] == 0 and nums[right] == 0: 
                right+=1
            # when one is not zero, swap them:
            elif nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right+=1
            # when both are not zero 
            else:
                left+=1
                right+=1
            print(nums[left])
        
        
        # [1, 3, 3, 12, 0]
        #            L  R      
        
        
        
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = i + 1
        
        while j < len(nums):
            if nums[i] == 0 and nums[j] == 0:
                j += 1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] == 0:
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] != 0:
                i += 1
                j += 1

'''
