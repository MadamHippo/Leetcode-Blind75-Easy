## https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1  # Set the left and right pointers
        
        while left < right:
            mid = (left + right) // 2  # Calculate the middle index
            if nums[mid] > nums[right]:  # If the middle element is greater than the rightmost element
                left = mid + 1  # Search the right half
            else:
                right = mid  # Search the left half (including the middle element)
        return nums[left]  # Return the minimum element found at the end of the loop
      
      
        '''

        Let's break down the code line by line:

            def findMin(nums): - This is the function definition. It takes in a list of integers nums and returns an integer, which is
            the minimum element in the list.

            left, right = 0, len(nums)-1 - This sets the left and right pointers to the first and last indices of the list nums.

            while left < right: - This starts a while loop that runs until the left pointer is equal to or greater than the right pointer.

            mid = (left + right) // 2 - This calculates the middle index between the left and right pointers.

            if nums[mid] > nums[right]: - This checks if the middle element is greater than the rightmost element.

            left = mid + 1 - If the middle element is greater than the rightmost element, then we know that the minimum element is in the
            right half of the list. Therefore, we set the left pointer to mid + 1.

            else: - If the middle element is not greater than the rightmost element, then we know that the minimum element is in the left
            half of the list.

            right = mid - Therefore, we set the right pointer to mid.

            return nums[left] - At the end of the loop, the left pointer will point to the minimum element in the list. Therefore, we
            return nums[left].

         
         '''
        
        
        
 class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Neetcode's way

        # declaring an arbitrary result
        result = nums[0]
        leftPointer, rightPointer = 0, len(nums)-1

        while leftPointer <= rightPointer:
            #if the subarray is already sorted, just take the default minimum at the farest left
            if nums[leftPointer] < nums[rightPointer]:
                result = nums[leftPointer]
                break
            
            # if array is not presorted, do binary search:
            midPointer = (leftPointer + rightPointer) // 2
            result = min(result, nums[midPointer])
            if nums[midPointer] >= nums[leftPointer]:
                leftPointer = midPointer + 1
            else:
                rightPointer = midPointer - 1
            
        return result
