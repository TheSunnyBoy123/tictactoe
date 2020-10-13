board=[["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]
isX = True
a=0
def printBoard(board, isX, a):
    for i in range(0, 3):
        for j in range(0,3):
            if j == 2:
                print(board[i][j], end = " ")
            else:
                print(board[i][j], end = "|")

        if (i==2):
            print()
        else:
            print()
            print("-----")

    gameCheck(board, isX, a)
    userInput(board, isX, a)

#user input
def userInput(board, isX, a):
    row=int(input("enter the row to put whatever")) #what the USER chooses
    column=int(input("enter the colum no. to put whatever"))#what the USER chooses


    if(a==9):
        for i in range(0, 3):
            for j in range(0,3):
                print(board[i][j], end = " ")
            print()
        print("Game Drawn")
        exit()
    if board[row-1][column-1] == "-": #if square isnt taken
        if isX : #if x turn
            board[row-1][column-1] = "X" #set square to x
            isX = False
        else: #if O turn
            board[row-1][column-1] = "O" #set square to o
            isX = True
    else:
        userInput(board, isX, a)

    printBoard(board, isX,a)
#check if game has been won
def gameCheck(board, isX, a):

    if(board[0][0]==board[0][1]==board[0][2]!="-"):
        GameWon(isX)

    elif(board[1][0]==board[1][1]==board[1][2]!="-"):
        GameWon(isX)

    elif(board[2][0]==board[2][1]==board[2][2]!="-"):
        GameWon(isX)

    elif(board[0][0]==board[1][1]==board[2][2]!="-"):
        GameWon(isX)


    elif(board[0][0]==board[1][0]==board[2][0]!="-"):
        GameWon(isX)

    elif(board[0][1]==board[1][1]==board[2][1]!="-"):
        GameWon(isX)

    elif(board[0][2]==board[1][2]==board[2][2]!="-"):
        GameWon(isX)
    elif(board[0][2] == board[1][1]==board[2][0]!="-"):
        GameWon(isX)
    else:
        a+=1
        userInput(board, isX, a)



def GameWon(isX):
    if isX:
        print("O won")
    elif isX == False:
        print("X won")
    exit()



printBoard(board, isX,a)
