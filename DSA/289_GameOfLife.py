'''
intial thoughts
    dang

    two big problems
        1. figuring out a wat to look to look at neighbours (without going out of bounds)
        2. determining death or revival
        3. also another problem was the fact that all of the changes must be done simultaneously

    Solutions
        1. subtract or add 1 or 0 to look around i, j
        2. sum neighbours to see whatgoing on
        3. copy initial array

    O(n * m)

'''
import copy 
def gameOfLife(board):
    cop = copy.deepcopy(board)
    rows = len(board)
    cols = len(board[0])

    # These are to be added to the given i, j to simulate looking around
    # They are r, c
    direcitons = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def state(i, j):
        neigh_sum = 0

        # For every offset pair in directions
        for r, c in direcitons:
            # Validate the new indices. 0 <= i + r, j + c < rows, cols
            if 0 <= i + r < rows and 0 <= j + c < cols:
                neigh_sum += cop[i + r][j + c]
        cell = board[i][j]

        # Mutating based on conditions

        # if alive & < 2 neighbors
        if cell == 1 and neigh_sum < 2:
            cell = 0
        # if alive and 2 <= neighbours <= 3, leave as is 
        # Don;t need this clause because you are not changinf anything
        # elif cell == 1 and 2 <= neigh_sum <= 3:
        #     cell == 1
        # dies if neighbours  > 3
        elif cell == 1 and neigh_sum > 3:
            cell = 0
        # revice cell if 3 nrighbours
        elif cell == 0  and neigh_sum == 3:
            cell = 1
        else:
            pass
        
        return cell

    for i in range(rows):
        for j in range(cols):
            board[i][j] = state(i,j)


