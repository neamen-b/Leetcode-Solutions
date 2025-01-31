'''
Initial thoughts

    check top left neightbour and see if they are equal. 
    but first you have to make sure that the top left neighbout is there,
        neightbour = mat[i-1][j-1]
        gotta check if i-1 >=0 and j-1>=0

            the heck if the values at those two pairs are equal,
                if not return false
            
        return true

'''


def isToeplitzMatrix(matrix)-> bool:

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):

            if i-1>= 0 and j-1>=0:

                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
                
    return True

matrix = [[1]]

print(isToeplitzMatrix(matrix))