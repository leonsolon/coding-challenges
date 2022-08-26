# Week 2
# Matrix
# Spiral Matrix
# Runtime: 27 ms, faster than 49.90% of Python online submissions for Spiral Matrix.
# Memory Usage: 13.4 MB, less than 45.12% of Python online submissions for Spiral Matrix.


def spiralOrder(matrix):
  
  row = len(matrix)
  col =  len(matrix[0])
  n_elem = row * col
  output = []
  start_row = 0 # start row 
  start_col = 0 # start column
  end_row = row # end row
  end_col = col # end col

  while len(output) < n_elem:
    
    # first row 
    for i in range(start_col, end_col):
      output.append(matrix[start_row][i])
    
    start_row += 1

    # last column 
    for i in range(start_row, end_row):
      output.append(matrix[i][end_col - 1])
    
    end_col -= 1

    # last row 
    if start_row < end_row:
      for i in range(end_col - 1, start_col - 1, -1):
        output.append(matrix[end_row - 1][i])
      
      end_row -= 1
    
    # first column 
    if start_col < end_col:
      for i in range(end_row - 1, start_row - 1, -1):
        output.append(matrix[i][start_col])
      
      start_col += 1
  
  return output

assert spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
