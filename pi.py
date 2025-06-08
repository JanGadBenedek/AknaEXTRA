import random

board = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]

boardDisplay = [[-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1]]


def checkMinesAround(row,col):
    t = 0 
    i= row -1
    while i <= row+1:
        if i >= 0 and i<5:
            j = col -1
            while j<= col +1:
                if j>=0 and j<5:
                    t=t+board[i][j]
                j=j+1
        i=i+1
    return t

numMines = int(input("Nehézség?"))
if numMines > 25:
    print("Annyi nem lehet hülye")
    numMines=5
num=0
while num < numMines:
    row = random.randint(0,4)
    col = random.randint(0,4)
    if board[row][col] == 0:
        board [row][col] =1 
        num = num+1

def displaySol():
    print("-" * 29)
    for row in range(0,5):
        print("|", end=" ")
        for col in range(0,5):
            print(board[row][col], end="  |  ")
        print() 
        print("-" * 29)     

def displayBoard():
    print("-" * 29)
    for row in range(5):
        print("|", end=" ")
        for col in range(5):
            if boardDisplay[row][col] == -1:
                print(" ", end="  |  ")
            else:
                print(boardDisplay[row][col], end="  |  ")
        print()  
        print("-" * 29)
displaySol()
displayBoard()

guess = 0
while guess < (25 - numMines):
    row = int(input("guess a row(1-5): ")) - 1
    col = int(input("guess a col(1-5): ")) - 1
    if board[row][col] ==1 :
        print("Gatya Az Egy Bomba Volt")
        displaySol()
    else:boardDisplay[row][col] = checkMinesAround(row,col)
    displayBoard()


