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


# Merge One Row Left Function
def mergeOneRowL(row):
    for i in range(boardSize - 1):
        for j in range(boardSize - 1, 0, -1):
            if row[j - 1] == 0:
                row[j - 1] = row[j]
                row[j] = 0

    for i in range(boardSize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0

    for i in range(boardSize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row


# Merge Left Function
def merge_left(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])
    return currentBoard


# Reverse Row Function
def reverse(row):
    new = []
    for i in range(boardSize - 1, -1, -1):
        new.append(row[i])
    return new


# Merge Right Function
def merge_right(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard


# Transpose Function
def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard


# Merge Up Function
def merge_up(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard


# Merge Down Function
def merge_down(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard


# Pick New Value Function
def pickNewValue():
    if random.randint(1, 8) - 1:
        return 4
    else:
        return 2


# Add New Value Function
def addNewValue():
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    while not board[rowNum][colNum] == 0:
        rowNum = random.randint(0, boardSize - 1)
        colNum = random.randint(0, boardSize - 1)

    board[rowNum][colNum] = pickNewValue()


#Win Condition Function
def won():
    for row in board:
        if 2048 in row:
            return True
    return False



# No Moves Function
def noMoves():
    tempBoard1 = copy.deepcopy(board)
    tempBoard2 = copy.deepcopy(board)

    tempBoard1 = merge_down(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_up(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_left(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_right(tempBoard1)
    if tempBoard1 == tempBoard2:
        return True
    else:
        return False