import random
import time

def fut():
    board = [[0 for _ in range(5)] for _ in range(5)]
    boardDisplay = [[-1 for _ in range(5)] for _ in range(5)]

    def checkMinesAround(row, col):
        t = 0 
        for i in range(row-1, row+2):
            if 0 <= i < 5:
                for j in range(col-1, col+2):
                    if 0 <= j < 5:
                        t += board[i][j]
        return t

    def displaySol():
        print("-" * 29)
        for row in range(5):
            print("|", end=" ")
            for col in range(5):
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

    numMines = int(input("Nehézség? (1-25): "))
    if numMines > 25 or numMines < 1:
        print("Annyi nem lehet hülye, 5 akna lesz!")
        numMines = 5

    num = 0
    while num < numMines:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if board[row][col] == 0:
            board[row][col] = 1 
            num += 1

    guess = 0
    totalGuesses = 25 - numMines
    start_time = time.time()
    while guess < totalGuesses:
        try:
            row = int(input("guess a row(1-5): ")) - 1
            col = int(input("guess a col(1-5): ")) - 1
            if not (0 <= row < 5 and 0 <= col < 5):
                print("Csak 1 és 5 közötti számot adj meg!")
                continue
        except ValueError:
            print("Érvénytelen szám!")
            continue

        if board[row][col] == 1:
            print("Gatya Az Egy Bomba Volt")
            displaySol()
            end_time = time.time()
            elapsed = end_time - start_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            print(f"Játékidő: {minutes} perc {seconds} másodperc")
            return
        elif boardDisplay[row][col] != -1:
            print("Ezt a mezőt már tippelted!")
            continue
        else:
            boardDisplay[row][col] = checkMinesAround(row, col)
            displayBoard()
            guess += 1

    end_time = time.time()
    elapsed = end_time - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    print(f"Gratulálok, nyertél! Játékidő: {minutes} perc {seconds} másodperc")
    displaySol()

def menu():
    while True:
        kerdes = input("""

        Start(1)
        Leaderboard(2)
        Exit(3)
                    :_____""")
        if kerdes == '1':
            fut()
            break
        elif kerdes == '2':
            print("""
            -Karcsi  király: difficulty: 24  Time: 1s
            -Keve a nyomi:   difficulty: 1   Time: 60000000hour
            -BBB:            difficulty: 10  Time: 2m
                        """)
        elif kerdes == '3':
            print("Faszért mész el?!")
            break
        else:
            print("Nem lehet ilyen számot megadni!")

if __name__ == '__main__':
    menu()