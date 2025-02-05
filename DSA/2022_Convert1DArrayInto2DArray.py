'''
Just did this for reshaping matrices

basically loop thorugh the 1d array
    use two pointers m,n
    whenn going thorugh original 1d array with poniter i
        if n == (the new number of columns):
            increment m (meaning move to the next row)
            set n = 0 (meaning set it to the start of the new row)
        
        otherwise increment n by one

'''

def construct2DArray(original, m, n):

    # If the number of elements don't match up. Meaning m*n != length of og
    if len(original) != m*n:
        return []
    
    new_mat = [[0]* n for _ in range(m)]
    r,c =0,0

    for i in range(len(original)):
        if c == n:
            r+=1
            c=0
        new_mat[r][c] = original[i]
        c+=1
    
    return new_mat

# print(construct2DArray([1,2,3,4], 2,2))

# myset = set(['a','b','c'])
# print(myset)
# print('a' in myset)
