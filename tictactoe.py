# A simple Tic-Tac-Toe game made in Python, made with TKL keyboards in mind

# Cell definition for empty cells and cells filled by players x and o
# This can all be simplified significantly, but a bit of flair might be nice.
cell_1 = cell_2 = cell_3 = cell_4 = cell_5 = cell_6 = cell_7 = cell_8 = cell_9 = '       \n   f   \n       '
cell_x = '  \\ /  \n   x   \n  / \\  '
cell_o = '  / \\  \n  (o)  \n  \\ /  '


# Cells placed in list for easy access in for loop
listcells = [cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9]

# Quickly make 9 cells with distinct numbers in them
y=1
for x in listcells:
    curnum = str(y)
    print(curnum)
    print(x)
    x=x.replace('f',curnum)
    print(x)
    y+=1

# Place all the cells in a dictionary for easy access
boardState = {'1': cell_1, '2': cell_2, '3': cell_3,
              '4': cell_4, '5': cell_5, '6': cell_6,
              '7': cell_7, '8': cell_8, '9': cell_9}

# Let's try printing the boardState
print(boardState['1'] + '|' + boardState['2'] + '|' + boardState['3'])
print('-------+-------+-------')
print(boardState['4'] + '|' + boardState ['5'] + '|' + boardState['6'])
print('-------+-------+-------')
print(boardState['7'] + '|' + boardState ['8'] + '|' + boardState['9'])
