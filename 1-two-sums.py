# Given array of nums, we also have a target.

# Return the position of two numbers in that array that will add up to the target.

# Pseudocode...we have to loop through the array of numbers first...so use a for loop to run through nums. 

# We also need a nested another loop for this to compare to see if both numbers can add up to target.

# If two numbers from two indices does, return indices. That makes it O(n2) time...too long and not great. Space complexicity is O(1).

# The more "correct way" is using a hash map, and do it in one pass. Storing the values in a hash. You will subtract the target to whatever is being currently looped through in the array and seeing if the hash map has that value added. In the beginning you will have no or little hash map values to compare to but eventually you will find your number that will add up to target. Brilliant. This solution is constant time O(n).

class Solution(object):
    def twoSum(self, nums, target):
        
        hashMap = {} # val : index
        
        for i in range(len(nums)):
            num = nums[i]
            difference = target - num
