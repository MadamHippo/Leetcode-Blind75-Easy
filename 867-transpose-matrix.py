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


'''

Problem Description: You're given a 2D matrix, and your goal is to transpose it, which means switching the matrix's row and column indices (rows become columns, columns become rows).

Step 1: Finding the Dimensions of the Matrix

python
Copy code
rows = len(matrix) # Finding the number of rows
columns = len(matrix[0]) # Finding the number of columns
Here, you're correctly finding the number of rows and columns in the input matrix.

Step 2: Creating a New Matrix

python
Copy code
new_matrix = [[0]*rows for _ in range(columns)]
You're creating a new matrix (new_matrix) with swapped dimensions (rows become columns and vice versa) filled with zeros. This is where you'll store the transposed matrix.

Step 3: Transposing the Matrix

python
Copy code
for r in range(rows):
    for c in range(columns):
        new_matrix[c][r] = matrix[r][c]
You're using nested loops to iterate through the original matrix. For each element at matrix[r][c], you're assigning it to new_matrix[c][r], effectively transposing the matrix.

Step 4: Returning the Transposed Matrix

python
Copy code
return new_matrix
Finally, you're returning the new_matrix, which now contains the transposed version of the input matrix.
'''
