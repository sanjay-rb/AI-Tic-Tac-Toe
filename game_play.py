print("Starting AI-Tic-Tac-Toe....")
from classifier import Classifier
classfier = Classifier()

board = [
    '0', '1', '2',
    '3', '4', '5', 
    '6', '7', '8'
]

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

while True:
    drawBoard(board=board)
    print(f"\n\n{','.join(inBoard(board))}")
    xi = int(input("\nEnter X value : "))
    if xi > len(board): 
        print("Out of board, exiting....")
        break
    if board[xi] in ['o', 'x']: 
        print(f"Already taken by {board[xi]}, please choose different place")
        continue
    board[xi] = 'x'
    oi = classfier.oMove(inBoard(board))[0]
    print(oi)
    oi_count = 0
    while board[oi] in ['o', 'x']:
        oi_count+=1
        print(f"Already taken by {board[oi]}, choosing different place ({oi_count})")
        oi = classfier.oMove(inBoard(board))[0]
        
    board[oi] = 'o'

print("Thank you, Play again")