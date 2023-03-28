class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # run time is logm + logn because we're using logm to find which row to look for and then logn to see which exact value in the row is the target.

        # it's a double binary search basically

        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            which_row = (top + bottom) // 2
            if target < matrix[which_row][0]:
                bottom = which_row - 1
            elif target > matrix[which_row][-1]:
                top = which_row + 1
            else:
                break

        if not (top <= bottom):
            return False
        which_row = (top + bottom) // 2
        left = 0
        right = COLS-1
        while left <= right:
            mid_index = (left + right) // 2
            if target > matrix[which_row][mid_index]:
                left = mid_index + 1
            elif target < matrix[which_row][mid_index]:
                right = mid_index - 1
            else:
                return True
        return False
