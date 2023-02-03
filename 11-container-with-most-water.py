# https://leetcode.com/problems/container-with-most-water/description/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int


        # brute force (will get time limit exceeded) 
        # O(n)^2
        result = 0

        for leftPointer in range(len(height)):
            for rightPointer in range(leftPointer+1, len(height)):
                # area is (width is rightPointer - leftPointer) * height 
                area = (rightPointer - leftPointer)*min(height[leftPointer], height[rightPointer])
                result max(result, area)
        return result

        """

        # LINEAR efficient solution, O(n) using two pointers


        result = 0

        leftPointer = 0
        rightPointer = len(height)-1

        while leftPointer < rightPointer:
            area = (rightPointer - leftPointer) * min(height[leftPointer], height[rightPointer])
            result = max(result, area)

            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            elif height[leftPointer] > height[rightPointer]:
                rightPointer -= 1
            else:
                rightPointer -= 1
        return result
