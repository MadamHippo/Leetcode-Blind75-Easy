class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # write in O(log n) time, everytime you can eliminate by half until you find target. Log(base2 of N)...how many times n can be divided by 2.
        # pre-sorted in ASCENDING order
        
        # Two pointers, L at start and R at the end.
        # Find midway point (M) and see if it's bigger or smaller than target
        # Now take L pointer and shift it to M + 1 and that will be the solution where the range is.
        # Repeat
        # Return index of M
        
        left = 0
        right = len(nums) - 1
        #print(left)
        #print(right)
        
        while left <= right:
            # since we keep adding +1 to left, left will eventually equal or increase above right which means you've ran out of nums in the array. So when left has crossed right, you will have no more values to search and target was not found.
            
            middle_index = (left + right) // 2
            # each iteration of the loop, we will see what our new mid index is.
            
            if nums[middle_index] > target: # if the value this index is at is larger than target, I want to see whats on my left side.
                
                right = middle_index-1
                # we want to see values to our Left so decrease / limit down right to mid-1
                
            elif nums[middle_index] < target: # if VALUE...nums[mid]...is smaller than target, move left to mid index + 1.
                left = middle_index+1
            else:
                return middle_index
        return -1
