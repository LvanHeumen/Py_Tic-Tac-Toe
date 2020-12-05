# Python Tic-Tac-Toe for TKL keyboards

'''A simple integration of the classic tic-tac-toe game in Python.
   Several of these integrations exist, often using the numpad on a full-size
   keyboard. This version however is made with TKL in mind.'''

# As this implementation uses distinct cells that can be changed, but shouldn't allow for duplicates, a dictionary is appropriate to use here.
# In this case, every key will initially be linked to a string indicating board position

boardState = {str(x):str(x) for x in range(1,10)}
# This implementation requires the board to constantly be redrawn, so this will be relegated to a function
def drawBoard(board):
    print(f"{board['1']}|{board['2']}|{board['3']}")
    print('-+-+-')
    print(f"{board['4']}|{board['5']}|{board['6']}")
    print('-+-+-')
    print(f"{board['7']}|{board['8']}|{board['9']}")

drawBoard(boardState)

player_1 = 'X'
player_2 = 'O'

activePlayer = player_1

for i in range(1,10):
    placeAvailable = False
    print(f'Player {activePlayer}, where would you like to place your symbol?')

    while placeAvailable == False:
        move = input()
        if move in boardState.values() and move != (player_1 or player_2):                                         # Opting for values as the keys don't change, so they can be overwritten in theory
            placeAvailable = True
            boardState[move] = activePlayer
        else:
            print('That spot is not available, please select another')

    drawBoard(boardState)

    # Player swap
    activePlayer = player_2 if activePlayer == player_1 else player_1
