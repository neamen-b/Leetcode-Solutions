'''
Initial thoughts
    I can think of two ways to do this:

    1. IF IT IS A SQAURE MATRIX, you can do an in place transpose

        for each element in the upper triangle of matrix, 
            swap across the diagonal

    2. For both square and non square matrices

        create a new array with reverse dimentsions. 

        then do the same thing as step one
    
    This is a nice way which I wanted to try. Saw a solutoin
        it used zip

    typical go through each row and convert it in to a column

'''
from typing import List
class Solution:
    
    # In place transpose
    def squareTranspose(mat: List[List[int]]) -> None: 

        if len(mat) != len(mat[0]):
            print("Not a Sqaure Matrix!")
            return None

        for i in range(len(mat)):
            for j in range(i + 1, len(mat[0])):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Clever trasnpose using zip. 
    def transposeZip(mat):
        new_mat = []
        # * unpacks the mat list into iterables for zip
        # Zips throws an error if the iterables are not equal length
        for item in zip (*mat):
            # print(list(item))
            new_mat.append(list(item))
        return new_mat

    
mat = [[1,2,3],[4,5,6]]
print(mat)
print(Solution.transposeZip(mat))

        
