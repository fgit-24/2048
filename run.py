# 2048 - Key Components

'''
Board Representation: A 4x4 grid initialized with zeros.

User Interaction: Users provide input to merge the board in different directions.

Merging Logic: Functions to handle merging left, right, up, and down.

Game State Management: Functions to check for win and loss conditions, add new values, and display the board.

Game Loop: A loop that continues until the game is won or lost, prompting the user for moves and updating the board accordingly.
'''


# Initialize Board Size and Create Blank Board
boardSize = 4

board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)


# Display Function
def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpaces = len(str(largest))

    for row in board:
        currRow = '|'
        for element in row:
            if element == 0:
                currRow += " " * numSpaces + '|'
            else:
                currRow += (' ' * (numSpaces - len(str(element)))) + str(element) + '|'
        print(currRow)
    print()


# Display Function
def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpaces = len(str(largest))

    for row in board:
        currRow = '|'
        for element in row:
            if element == 0:
                currRow += " " * numSpaces + '|'
            else:
                currRow += (' ' * (numSpaces - len(str(element)))) + str(element) + '|'
        print(currRow)
    print()