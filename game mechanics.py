board = [['0', '0', '0'],
         ['0', '0', '0'],
         ['0', '0', '0']]


def printBoard(currentboard):
    stop = False
    counter = 0
    while not stop:
        print(currentboard[counter])
        counter += 1
        if counter == 3:
            stop = True


def gamecheck(nope):
    return nope


print("TicTacToe")
end = False
while not end:
    printBoard(board)
    end = True
