import random

# printing board
def printBoard(board):
    print ('   |   |   ')
    print (' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print ('   |   |   ')
    print ('-----------')
    print ('   |   |   ')
    print (' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('   |   |   ')
    print ('-----------')
    print ('   |   |   ')
    print (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print ('   |   |   ')


# inserting key in board
def insertKey(pos,key):
    board[pos]=key

# finding space free or not
def isSpaceFree(pos):
    return board[pos] == ' '


# getting player option
def playerOption():

    while True:
        pos = input("Enter the position (1-9) : ")
        if (pos >=1 and pos <=9):
            if isSpaceFree(pos):
                insertKey(pos, 'X')
                break
            else:
                print ("Sorry, this Position is Occupied.")
        else:
            print ("Please! enter number between (1-9).")


# for check the winner
def isWinner(b, k):
    return (
            (b[1] == k and b[2] == k and b[3] == k) or
            (b[4] == k and b[5] == k and b[6] == k) or
            (b[7] == k and b[8] == k and b[9] == k) or
            (b[1] == k and b[4] == k and b[7] == k) or
            (b[1] == k and b[5] == k and b[9] == k) or
            (b[2] == k and b[5] == k and b[8] == k) or
            (b[3] == k and b[6] == k and b[9] == k) or
            (b[3] == k and b[5] == k and b[7] == k)
    )


# getting computer option (return position)
def computerOption(board):
    possibleMoves = [x for x in range(1,10) if (board[x]==' ')]
    move = 0

    for k in ['O','X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = k
            if isWinner(boardcopy, k):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if (len(cornersOpen)>0):
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if (len(edgesOpen)>0):
        move = selectRandom(edgesOpen)
        return move

# Select random value for computer option list
def selectRandom(value):
    move = random.randrange(0,len(value))
    return value[move]

# finding board or not
def isBoardFull(board):
    if board.count(' ')>=2:
        return False
    else:
        return True

# starting game
def startGame():
    global board
    board = [' ' for x in range(10)]
    # os.system('cls')
    print ("Game Started...")
    print
    gamePlay()

# playing game option
def gamePlay():
    while True:
        printBoard(board)
        playerOption()
        pos = computerOption(board)
        if not isBoardFull(board):
            insertKey(pos, 'O')
        if isWinner(board, 'X'):
            print ("You WIN!")
            break
        if isWinner(board, 'O'):
            printBoard(board)
            print ("You LOST!")
            break
        if isBoardFull(board):
            print ("Match DRAW!")
            break

# main call
while True:
    startGame()
    x = raw_input("Do you want to play again!...(y/n) : ")
    x.lower()
    if not (x=='y' or x=='yes'):
        print ("Game Finished!")
        break

