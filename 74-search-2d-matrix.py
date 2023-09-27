class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # run time is logm + logn because we're using logm to find which row to look for and then logn to see which exact value in the row is the target.

        # https://leetcode.com/problems/search-a-2d-matrix/

        # it's a double binary search basically

        ROWS = len(matrix)
        COLS = len(matrix[0])

        top_row = 0
        bottom_row = ROWS - 1

        while top_row <= bottom_row:
            which_row = (top_row + bottom_row) // 2


            if target < matrix[which_row][0]:
                bottom_row = which_row - 1

            # looking at the right-most value to see if this target is greater than the largest value in the row:
            elif target > matrix[which_row][-1]:
                # if it is, move onto the next (larger) row
                top_row = which_row + 1

            # target value is in the current row...so break out of the loop so you can do the SECOND binary search
            else:
                break

        # none of the rows contain the target value..
        if not (top_row <= bottom_row):
            return False

        # SECOND binary search portion:
        # run binary search on a specific row...
        current_row = (top_row + bottom_row) // 2
        left = 0
        right = COLS-1
        while left <= right:
            mid_index = (left + right) // 2
            if target > matrix[current_row][mid_index]:
                left = mid_index + 1
            elif target < matrix[current_row][mid_index]:
                right = mid_index - 1
            else:
                return True
        return False
