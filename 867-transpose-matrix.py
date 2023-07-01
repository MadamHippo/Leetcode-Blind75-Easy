# https://leetcode.com/problems/transpose-matrix/description/

# Understanding? Uhhh...1/5?

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # filling in matrix elements
        
        '''
        Goal: switch the matrix's row and column indices...like rows become columns and columns becomes rows.
        
        
        runtime O(n*m)
        
        1. find length of row+columns
        2. create a new variable call new that copies a reference to the same object, n times. It is equivalent to this: [0, 0, 0]
        3. for loop to go through range(row) and another nested for loop for columns...
            in python you can just set matrix row and column to new matrix's swapped.
        4. just return new_matrix
        '''

        # find length of rows and columns:
        
        rows = len(matrix) # left right
        columns = len(matrix[0]) # top down
        
        new_matrix = [[0]*rows for _ in range(columns)] 
        # Is copying a reference to the same object, n times. It is equivalent to this: [0, 0, 0]


        
        for r in range(rows):
            for c in range(columns):
                new_matrix[c][r] = matrix[r][c]
                
        return new_matrix
