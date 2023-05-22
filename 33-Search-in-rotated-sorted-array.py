class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # binary search techique to do it in O(logo n) time
        # this one is hard and confusing. Must be drawn out before you code!!!
        # the coding isn't hard but you need to understand what's going on. Draw it out!!

        left = 0
        right = len(nums)-1

        
        while left <= right:
            mid = (left + right) // 2
            # if luckily target happens to be mid
            if target == nums[mid]:
                return mid
            
            # if the value at the left pointer is smaller than midpoint:
            if nums[left] <= nums[mid]:
                # and if target is larger than midpoint, then igore all the values on left and update left pointer to mid+1
                if target > nums[mid]:
                    left = mid+1
                elif target < nums[left]:
                    left = mid+1
                else:
                # if target is smaller than midpoint...we ignore all values on the right and update right pointer to mid-1
                    right = mid-1
            else:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[right]:
                    right = mid - 1
                else:
                    # target is greater than middle value and target is greater than right value:
                    left = mid + 1
        return -1
