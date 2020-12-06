# Python Tic-Tac-Toe for TKL keyboards

'''A simple integration of the classic tic-tac-toe game in Python.
   Several of these integrations exist, often using the numpad on a full-size
   keyboard. This version however is made with TKL in mind.'''

# This implementation requires the board to constantly be redrawn, so this will be relegated to a function
def drawBoard(board):
    print(f"{board['1']}│{board['2']}│{board['3']}")
    print('─┼─┼─')
    print(f"{board['4']}│{board['5']}│{board['6']}")
    print('─┼─┼─')
    print(f"{board['7']}│{board['8']}│{board['9']}")

# Function to print the game winner
def wonGame(player,board):
    drawBoard(board)
    print(f'\n******** Player {player} has won, congratulations! ********\n')

# Define the game itself as a Function
def playGame():
    # Define playing board
    boardState = {str(x):str(x) for x in range(1,10)}

    # Define player names
    player_1 = 'X'
    player_2 = 'O'

    # Set active player
    activePlayer = player_1

    for turn in range(1,10):

        drawBoard(boardState)
        placeAvailable = False
        print(f'Player {activePlayer}, where would you like to place your symbol?')

        while placeAvailable == False:
            move = input()
            if move in boardState.values() and move != (player_1 or player_2):
                placeAvailable = True
                boardState[move] = activePlayer
            else:
                print('That spot is not available, please select another')

        # Checking win conditions on the 5th turn and thereafter
        # Tic-tac-toe has 8 discrete win states, all will be checked
        if turn >= 5:
            if boardState['1'] == boardState['2'] == boardState['3']:
                wonGame(activePlayer,boardState)
                break
            elif boardState['4'] == boardState['5'] == boardState['6']:
                wonGame(activePlayer,boardState)
                break
            elif boardState['7'] == boardState['8'] == boardState['9']:
                wonGame(activePlayer,boardState)
                break
            elif boardState['1'] == boardState['4'] == boardState['7']:
                wonGame(activePlayer,boardState)
                break
            elif boardState['2'] == boardState['5'] == boardState['8']:
                wonGame(activePlayer,boardState)
                break
            elif boardState['3'] == boardState['6'] == boardState['9']:
                wonGame(activePlayer,boardState)
                break
            elif boardState['1'] == boardState['5'] == boardState['9']:
                wonGame(activePlayer,boardState)
                break
            elif boardState['3'] == boardState['5'] == boardState['7']:
                wonGame(activePlayer,boardState)
                break

        # If nobody wins after the 9th token, the game is a tie
        if turn == 9:
            drawBoard(boardState)
            print(f'\nGame Over!\nIt\'s a tie!')
            break
        # Player swap
        activePlayer = player_2 if activePlayer == player_1 else player_1

    # Ask for a restart
    print('Would you like to restart? y/n')
    restartGame = input()

    print()

    if restartGame == 'y' or restartGame == 'Y':
        print('**** Restarting ****')
        playGame()

playGame()
