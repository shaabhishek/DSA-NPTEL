def init_board(n=4):
    board = {}
    # position of the queen
    board['queen'] = [-1]*n
    board['row'] = [0]*n
    board['column'] = [0]*n
    # NW - SE diagonal. The i-j value is invariant for all (i,j) in the diagonal
    # The index of diagonal goes from bottom left = -(N-1) to top right= N-1, so we offset it by N-1 
    # so that index is 0 - 2(N-1) = (0-n+1 + n-1) - (n-1-0 + n-1)
    board['nw_se_diag'] = [0]* (2*n - 1)
    # SW - NE diagonal. The i+j value is invariant for all (i,j) in the diagonal
    # The index is from top left = 0 to bottom right = 2(N-1)
    # the range is (0+0) - (n-1 + n-1)
    board['sw_ne_diag'] = [0]* (2*n - 1)
    return (board)

def checkempty(r, c, board):
    if board['row'][r] == 1 or board['column'][c] == 1 or board['nw_se_diag'][r-c + n-1] == 1 or board['sw_ne_diag'][r+c] == 1:
        return (False)
    else:
        return (True)

def emptycolumns(r, board):
    return [c for c in range(0, n) if checkempty(r,c, board)]

def updatecells(r, c, board, move):
    if move == 'place':
        board['row'][r] = 1
        board['column'][c] = 1
        board['nw_se_diag'][r-c + n-1] = 1
        board['sw_ne_diag'][r+c] = 1
    elif move == 'remove':
        board['row'][r] = 0
        board['column'][c] = 0
        board['nw_se_diag'][r-c + n-1] = 0
        board['sw_ne_diag'][r+c] = 0
    else:
        raise ValueError ('invalid move with the queen')
    # print(move, r,c)
    return (board)
    
def removequeen(r, c, board):
    board['queen'][r] = -1
    board = updatecells(r,c, board, 'remove')
    return (board)

def placequeen(board, i=0):
    # i is the row

    # generate the possible columns available for queen to sit in this row
    cols = emptycolumns(i, board)
    # print('i', i, cols)
    
    if not cols:
        return (False)

    # iterate through the possible columns available for this row
    for c in cols:
        # print('c', c)

    # update cells occupied after 
        board['queen'][i] = c
        board = updatecells(i,c, board, 'place')
    
    # check if it's the last queen. Means we're done!
        if i == n-1:
            # print('done', board)
            possible_config.append(board['queen'][:])
            board = removequeen(i, c, board)
            return (False)
    
    # place queen in row i+1 now
        placed = placequeen (board, i+1)

    # if next queen cannot be placed with this column, backtrack: remove the queen from i,c
        if not placed:
            board = removequeen(i, c, board)
        else:
            return(True)
            
    # Traversed through all columns without success
    else:
        return (False)

n = 8
b = init_board(n)
possible_config = []
placequeen(b)
print(possible_config[0])
# [print(i) for i in possible_config]