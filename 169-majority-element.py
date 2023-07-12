class Solution:
    def majorityElement(self, nums: List[int]) -> int:

# HASHMAP SOLUTION
# runtime O(n) because the m is smaller (we know it is) than n so just go with n as the worst runtime
# https://leetcode.com/problems/majority-element/
        hashmap = {}
                
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
                
        for key, value in hashmap.items():
            if value > (len(nums)//2):
                return key
