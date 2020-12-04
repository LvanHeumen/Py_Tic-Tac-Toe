# Python Tic-Tac-Toe for TKL keyboards

'''A simple integration of the classic tic-tac-toe game in Python.
   Several of these integrations exist, often using the numpad on a full-size
   keyboard. This version however is made with TKL in mind.'''

# As this implementation uses distinct cells that can be changed, but shouldn't allow for duplicates, a dictionary is appropriate to use here.
# In this case, every key will initially be linked to a string indicating board position
boardState = {'1':'1', '2':'2', '3':'3',
              '4':'4', '5':'5', '6':'6',
              '7':'7', '8':'8', '9':'9'}

# This implementation requires the board to constantly be redrawn, so this will be relegated to a function
def drawBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

drawBoard(boardState)
