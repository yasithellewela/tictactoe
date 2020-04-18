board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]


def printBoard(currentboard):
    stop = False
    counter = 0
    while not stop:
        print(currentboard[counter])
        counter += 1
        if counter == 3:
            stop = True


def gamecheck(cboard, player):
    if cboard[0][0] == player and cboard[1][0] == player and cboard[2][0] == player:
        return True
    elif cboard[0][1] == player and cboard[1][1] == player and cboard[2][1] == player:
        return True
    elif cboard[0][2] == player and cboard[1][2] == player and cboard[2][2] == player:
        return True
    elif cboard[0][0] == player and cboard[0][1] == player and cboard[0][2] == player:
        return True
    elif cboard[1][0] == player and cboard[1][1] == player and cboard[1][2] == player:
        return True
    elif cboard[2][0] == player and cboard[2][1] == player and cboard[2][2] == player:
        return True
    elif cboard[0][0] == player and cboard[1][1] == player and cboard[2][2] == player:
        return True
    elif cboard[0][2] == player and cboard[1][1] == player and cboard[2][0] == player:
        return True
    else:
        return False


print("TicTacToe")
print("Instructions: Two player game! Player 1 is X, Player 2 is O. Boxes are in a coordinate system.")
print("              They start from the top left corner at 1, and increase down and to the right.")
print("              To choose top left box, type '1 1'. To choose bottom left right, type '3 3'")
print("              To choose the middle box, type '2 2'")
print("              First person to create a line of three wins! Good luck!")

end = False
count = 0
while not end:
    texit = False
    printBoard(board)
    while not texit:
        if count % 2 == 0:
            turn = input("Player 1's Turn: ")
        else:
            turn = input("Player 2's Turn: ")
        turn = turn.split()
        turn[0] = int(turn[0])
        turn[1] = int(turn[1])
        if board[turn[1]-1][turn[0]-1] == "X" or board[turn[1]-1][turn[0]-1] == "O":
            print("Invalid, try again")
        else:
            if count % 2 == 0:
                board[turn[1]-1][turn[0]-1] = "X"
                texit = True
            else:
                board[turn[1]-1][turn[0]-1] = "O"
                texit = True
    if count >= 8:
        printBoard(board)
        print("Game Over! It's a Draw!")
        end = True
    if gamecheck(board, "X") or gamecheck(board, "O"):
        printBoard(board)
        if gamecheck(board, "X"):
            print("Game over! Player 1 Wins!")
        else:
            print("Game Over! Player 2 Wins!")

        end = True

    count += 1
