# Let's start with the simplest game - tic-tac-toe :)
# Realize the outcome of the game on the board.
# The board is represented by a tuple.
# A cross - 1, a zero - 0, empty cells are designated None.
# For visualization, I defined variables with convenient names.
# None I am here referring to _ (emphasizes a valid name in Python).

X, O, _ = 1, 0, None

TEST_BOARD = (
    X, X, O,
    O, O, X,
    X, X, X
)

# Possible four outcomes,I also defined named constants for them.
O_WINS, X_WINS, UNDEFINED, DRAW = range(4)

# The first subtask and hint is to implement a function 
# that returns all possible combinations of 3 cells in a row: 
# horizontal, vertical, diagonal. 
# In this way, this part of the task comes down to the exercise of slicing a sequence.

def slice3(board):
    """
    Returns all possible combinations of 3 cells in a row:
     horizontal, vertical, diagonal.

    >>> from pprint import pprint
    >>> pprint(list(slice3((
    ... O, X, O,
    ... X, O, X,
    ... _, _, X
    ... ))))
    [(0, 1, 0),
     (1, 0, 1),
     (None, None, 1),
     (0, 1, None),
     (1, 0, None),
     (0, 1, 1),
     (0, 0, 1),
     (0, 0, None)]
    """
    r = (board[:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[2:7:2], board[::4])
    return r



def outcome(board):
    """
    Determination of the outcome.

    Assumption: a board can contain only a lot of correct states, 
    which can result from a fair game.

    1. When the first 3 cells are crossed out on the board, the game is over.
    In this case, you must determine who won and return
    X_WINS or O_WINS.

    >>> outcome((
    ... X, X, O,
    ... O, X, _,
    ... O, _, X))
    1

    2. For simplicity, we assume for now that the game is always played out to the end. 
    As long as there are empty cells and any 3 are not crossed out - 
    the outcome is not determined - UNDEFINED.

    >>> outcome((
    ... X, X, O,
    ... O, O, X,
    ... _, _, X))
    2

    3. If all the cells are filled, and there is not combination of three adjacent ones, 
    winning is impossible for anyone, we award a draw - DRAW

    >>> outcome((
    ... X, X, O,
    ... O, O, X,
    ... X, X, O))
    3
    """
    if (1,1,1) in slice3(board):
        return 'X_WIN'
    elif (0,0,0) in slice3(board):
        return '0_WIN'
    elif None not in board[::]:
        return 'DRAW'
    else:
        return 'UNDEFINED'


print('RESULT: ' + outcome(TEST_BOARD))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
