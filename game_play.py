from sqlalchemy import false, true
from classifier import Classifier
print("Starting AI-Tic-Tac-Toe....")
classfier = Classifier()


def getIntex(l, v):
    indices = []
    for i in enumerate(l):
        if i[1] == v:
            indices.append(str(i[0]))
    return indices


board = [
    '0', '1', '2',
    '3', '4', '5',
    '6', '7', '8'
]

x_wins = [
    "0,1,2",
    "3,4,5",
    "6,7,8",
    "0,3,6",
    "1,4,7",
    "2,5,8",
    "0,4,8",
    "2,4,6",
]


def isXWins(board):
    # print(getIntex(board, 'x'))
    xis = ','.join(getIntex(board, 'x'))
    print(xis in x_wins)
    for i in x_wins:
        if i in xis:
            return True
    return False


def inBoard(board):
    new_board = []
    for i in board:
        if i.isnumeric():
            new_board.append('b')
        else:
            new_board.append(i)
    return new_board


def drawBoard(board):
    for i in range(0, len(board)):
        if i % 3 == 0:
            print("\n")
        print("|", board[i], end=' |')
    print("\n")


while True:
    drawBoard(board=board)
    print(','.join(inBoard(board)))
    xi = int(input("\nEnter X value : "))

    if xi > len(board):
        print("Out of board, exiting....")
        break
    if board[xi] in ['o', 'x']:
        print(f"Already taken by {board[xi]}, please choose different place")
        continue
    board[xi] = 'x'

    if isXWins(board):
        print("X Wins")
        drawBoard(board)
        break

    print(f"\n\n{','.join(inBoard(board))}")

    oi = classfier.oMove(inBoard(board))[0]
    if board[oi] in ['o', 'x']:
        print(
            f"Already taken by {board[oi]}, opponent failed to choose correct place")
        break
    board[oi] = 'o'

print("Thank you, Play again")
