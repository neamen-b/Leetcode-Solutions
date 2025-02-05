'''
Initial thoughts

    First you gotta check if the the given parameters for the new matrix are viable

    let row = og_mat.length
    let cols = og_mat[o].length

    if row*cols != r*c:
        then the reshape is not possible because the number of elements don't add up
        return og_matrix

    
        No figure out the swapping
'''

# Does not work properly
def matrixReshape(matrix, r, c):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows*cols != r*c:
        return matrix
    
    new_mat = [[0]*c for _ in range(r)]
    # print(new_mat)
    m,n =0,0

    for i in range(rows):
        for j in range(cols):
            print(f"i-{i},j-{j},m-{m},n-{n}")
            if j >= c:
                n = 0
                m+=1
            if i >= r:
                m = 0
                n+=1
            new_mat[m][n] = matrix[i][j]


    return new_mat

mat = [[1,2,3,4]]
r,c = 2,2

# print(matrixReshape(mat,r,c))


def matrixreshape2(matrix, r, c):

    rows = len(matrix)
    cols = len(matrix[0])

    if rows*cols != r*c:
        return matrix
    
    flat_mat = []
    new_mat = [[0]*c for _ in range(r)]

    for i in range(rows):
        for j in range(cols):
            flat_mat.append(matrix[i][j])
    print(new_mat)
    print(flat_mat)

    m,n = 0,0
    for i in range(len(flat_mat)):
        print(m,n,i,flat_mat[i])
        if n >= c:
            m+=1
            n=0
        new_mat[m][n] = flat_mat[i]
        n+=1

    return new_mat

print(matrixreshape2(mat, r, c))

    
