X, O, _ = 1, 0, None

board = (
    X, O, O,
    _, O, X,
    X, X, O ) 

def slice3(board):
    
    r = (board[:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[2:7:2], board[::4])
    if (1,1,1) in r:
        return 'X_WIN'
    elif (0,0,0) in r:
        return '0_WIN'
    elif None not in board[::]:
        return 'DRAW'
    else:
        return 'UNDEFINED'

print(slice3(board))

#from timeit import timeit

#print(timeit(lambda: slice3(board)))

'''
def game(g):
    if g[0][0] == g[1][1] == g[2][2]==0:
        return '0_WINS'
    elif g[0][1] == g[1][1] == g[2][1]==0:
        return '0_WINS'
    elif g[0][2] == g[1][1] == g[2][0]==0:
        return '0_WINS'
    elif g[0][2] == g[1][2] == g[2][2]==0:
        return '0_WINS'
    elif g[2][0] == g[2][1] == g[2][2]==0:
        return '0_WINS'
    elif g[1][0] == g[1][1] == g[1][2]==0:
        return '0_WINS'
    elif g[0][0] == g[0][1] == g[0][2]==0:
        return '0_WINS'
    elif g[0][0] == g[1][0] == g[2][0]==0:
        return '0_WINS'

    if g[0][0] == g[1][1] == g[2][2]==1:
        return 'X_WINS'    
    elif g[0][1] == g[1][1] == g[2][1]==1:
        return 'X_WINS'
    elif g[0][2] == g[1][1] == g[2][0]==1:
        return 'X_WINS'
    elif g[0][2] == g[1][2] == g[2][2]==1:
        return 'X_WINS'
    elif g[2][0] == g[2][1] == g[2][2]==1:
        return 'X_WINS'
    elif g[1][0] == g[1][1] == g[1][2]==1:
        return 'X_WINS'
    elif g[0][0] == g[0][1] == g[0][2]==1:
        return 'X_WINS'
    elif g[0][0] == g[1][0] == g[2][0]==1:
        return 'X_WINS'
    elif g[0][0] == None or g[0][1] == None or g[0][2] == None or g[1][0] == None or g[1][1] == None or g[1][2] == None or g[2][0] == None or g[2][1] == None or g[2][2] == None:
        return 'UNDEFINED'
    else:
        return 'DRAW'

print(game(g))

'''



