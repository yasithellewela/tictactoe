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
count = 0
while not end:
    printBoard(board)
    turn = input("")
    turn = turn.split()
    turn[0] = int(turn[0])
    turn[1] = int(turn[1])
    board[turn[1]-1][turn[0]-1] = "X"
    if count >= 8:
        end = True
    if gamecheck(board):
        end = True

    count += 1
